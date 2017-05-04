from pymel.core import *

import maya.OpenMaya as OpenMaya
import maya.api.OpenMaya as OpenMaya2


def is_affected(upstream_obj, downstream_obj, dg_filter=OpenMaya.MFn.kInvalid):
    root = None
    if isinstance(upstream_obj, general.Attribute):
        root = upstream_obj.__apimplug__()
    elif isinstance(upstream_obj, nt.DependNode):
        root = upstream_obj.__apimobject__()

    if root is None:
        raise Exception('Invalid object: %s' % str(upstream_obj))

    end = None
    level = None
    if isinstance(downstream_obj, Attribute):
        end = downstream_obj.__apimplug__()
        level = OpenMaya.MItDependencyGraph.kPlugLevel
    elif isinstance(downstream_obj, nt.DependNode):
        end = downstream_obj.__apimobject__()
        level = OpenMaya.MItDependencyGraph.kNodeLevel

    if end is None:
        raise Exception('Invalid object: %s' % str(downstream_obj))

    try:
        dg_iter = OpenMaya.MItDependencyGraph(root,
                                              dg_filter,
                                              OpenMaya.MItDependencyGraph.kDownstream,
                                              OpenMaya.MItDependencyGraph.kBreadthFirst,
                                              level)
    except Exception as err:
        print('Failed obtain dg_iter')
        raise err

    while not dg_iter.isDone():
        if level == OpenMaya.MItDependencyGraph.kPlugLevel:
            if end == dg_iter.thisPlug():
                return True
        else:
            if end == dg_iter.currentItem():
                return True
        dg_iter.next()

    return False


def get_rotation(node):
    rotation = xform(node, q=1, rotation=True, worldSpace=True)
    rotation_order = node.getRotationOrder()
    er = OpenMaya2.MEulerRotation([OpenMaya2.MAngle(r, OpenMaya2.MAngle.uiUnit()).asRadians()
                                   for r in (rotation[0], rotation[1], rotation[2])],
                                  rotation_order.index - 1)
    return (OpenMaya2.MAngle.internalToUI(er.x),
            OpenMaya2.MAngle.internalToUI(er.y),
            OpenMaya2.MAngle.internalToUI(er.z))


def is_attr_drivable(attr):
    if not attr.isKeyable() or attr.isLocked():
        return False

    inputs = attr.inputs()
    if not inputs:
        return True

    if isinstance(inputs[0], nt.AnimCurve):
        return True

    return False


def bake_animation(channels, start, end):
    if not channels:
        return

    suspend = False
    if not about(batch=True):
        refresh(suspend=True)
        suspend = True

    bakeResults(channels,
                simulation=True,
                time=(start, end), sampleBy=1,
                disableImplicitControl=True, preserveOutsideKeys=True,
                sparseAnimCurveBake=True, removeBakedAttributeFromLayer=False,
                bakeOnOverrideLayer=False, minimizeRotation=False)

    if suspend:
        refresh(suspend=False)

def get_pynodes(nodes, nodetype=None):
    if nodes is None:
        return None

    _nodes = []
    if isinstance(nodes, list) or isinstance(nodes, tuple):
        _nodes = nodes
    else:
        _nodes = [nodes]

    pynodes = []
    for _node in _nodes:
        try:
            pynode = PyNode(_node)
        except Exception as err:
            print(str(err))
            print('Failed to obtain PyNode("%s")' % str(_node))
            raise err
        else:
            if pynode:
                if nodetype is None or isinstance(pynode, nodetype):
                    pynodes.append(pynode)

    return pynodes
