"""
MIT License

Copyright (c) 2017 Tsuyoshi Kobori

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Documentation

Sub module for main class and functions implementation except for UI.

"""


import re

from pymel.core import *

import maya.OpenMaya as OpenMaya
import maya.api.OpenMaya as OpenMaya2

from . import utils


class SpaceSwitcher(object):
    """
    This class encapsulates constraint structure of a target controller and a
    transform which works as temporary "parent".
    Operations such as creating or deleting constraints with or without
    keyframe bake are accessible via instance methods.
    """

    locator_prefix = 'cnst_'

    locator_target_attrname = 'spaceSwitcherTarget'

    locator_startinit_attrname = 'spaceSwitchStartInit'
    locator_start_attrname = 'spaceSwitcherStart'

    locator_endinit_attrname = 'spaceSwitcherEndInit'
    locator_end_attrname = 'spaceSwitcherEnd'

    constraint_types = {'translate':OpenMaya.MFn.kPointConstraint, 'rotate':OpenMaya.MFn.kOrientConstraint}

    @classmethod
    def get_target_from_locator(cls, locator):
        """
        Parameters:
            locator: pymel.core.general.PyNode
                Constraint locator.

        Return value:
            Target transform node. pymel.core.general.PyNode

        Description:
            Obtains target transform from constraint locator.
        """

        if not isinstance(locator, nodetypes.Transform):
            return None
        try:
            attr = locator.attr(cls.locator_target_attrname)
        except:
            return None
        else:
            inputs = attr.inputs(plugs=True)
            if not inputs:
                return None
            if isinstance(inputs[0].node(), nodetypes.Transform) and inputs[0].attrName(longName=True) == 'message':
                return inputs[0].node()
        return None

    @classmethod
    def get_locator_from_target(cls, target):
        """
        Parameters:
            target: pymel.core.general.PyNode
                Target transform.

        Return value:
            Constraint locator node. pymel.core.general.PyNode

        Description:
            Obtains constraint locator from target.
        """

        if not isinstance(target, nodetypes.Transform):
            return None
        try:
            attr = target.attr('message')
        except:
            return None
        else:
            outputs = attr.outputs(plugs=True)
            if not outputs:
                return None
            for output in outputs:
                if isinstance(output.node(), nodetypes.Transform)\
                   and output.attrName(longName=True) == cls.locator_target_attrname:
                    return output.node()
        return None

    @classmethod
    def get_bakerange_from_locator(cls, locator):
        """
        Parameters:
            locator: pymel.core.general.PyNode
                Constraint locator.

        Return value:
            A dictionary containing bake range information. dict

        Description:
            Obtains bake framerange from values stored in constraint locator's
            custom attributes and returns as a dictionary with keys and values
            shown below:

                spaceSwitcherStartInit : True if start is initialized (bool)
                spaceSwitcherStart     : bake start frame             (int)
                spaceSwitcherEndInit   : True if end is initialized   (bool)
                spaceSwitcherEnd       : bake end frame               (int)

        """

        if not isinstance(locator, nodetypes.Transform):
            return {}

        result = {}

        try:
            attr = locator.attr(cls.locator_startinit_attrname)
        except Exception as err:
            print(str(err))
        else:
            result[cls.locator_startinit_attrname] = attr.get()

        try:
            attr = locator.attr(cls.locator_start_attrname)
        except Exception as err:
            print(str(err))
        else:
            result[cls.locator_start_attrname] = attr.get()

        try:
            attr = locator.attr(cls.locator_endinit_attrname)
        except Exception as err:
            print(str(err))
        else:
            result[cls.locator_endinit_attrname] = attr.get()

        try:
            attr = locator.attr(cls.locator_end_attrname)
        except Exception as err:
            print(str(err))
        else:
            result[cls.locator_end_attrname] = attr.get()

        return result

    def __init__(self, target=None, locator=None):
        """
        Parameters:
            target: pymel.core.general.PyNode
                Target transform node you are animating.
            locator: pymel.core.general.PyNode
                Constraint locator node which drives target transform via
                point constraint and orientation constraint.

        For a new constraint structure, a class instance must be constructed
        with a target node before creating constraints:

        switcher = spaceswitcher.SpaceSwitcher(target=target)

        From an existing constraint structure, a class instance can be
        constructed and restored with a target node and/or a
        constraint locator:

        switcher = spaceswitcher.SpaceSwitcher(target=target)

        or

        switcher = spaceswitcher.SpaceSwitcher(locator=locator)

        or

        switcher = spaceswitcher.SpaceSwitcher(target=target, locator=locator)
        """

        # target: target transform
        self.target = None

        # locator: constraint locator
        self.locator = None

        # parent: parent transform
        self.parent = None

        # bake frame range
        self.start = None
        self.end = None

        # Restore instance variables
        self._restore(target=target, locator=locator)

    def _restore(self, target=None, locator=None):
        is_target_set = False
        is_locator_set = False

        # target
        if target:
            if not isinstance(target, nodetypes.Transform):
                raise ValueError('Not a transform node is specified as target: %s' % target.name())
            self.target = target
            is_target_set = True

        # locator
        if locator:
            if not isinstance(locator, nodetypes.Transform):
                raise ValueError('Not a transform node is specified as locator: %s' % locator.name())
            self.locator = locator
            is_locator_set = True

        # get target from locator
        if not is_target_set:
            self.target = SpaceSwitcher.get_target_from_locator(self.locator)

        # get locator from target
        if not is_locator_set:
            self.locator = SpaceSwitcher.get_locator_from_target(self.target)

        # get parent from locator
        if self.locator:
            parent = self.locator.getParent()
            if parent:
                self.parent = parent

        # get bake framerange from locator
        bakerange = SpaceSwitcher.get_bakerange_from_locator(self.locator)

        if bakerange.get(SpaceSwitcher.locator_startinit_attrname, False):
            self.start = bakerange.get(SpaceSwitcher.locator_start_attrname, None)
        else:
            self.start = None

        if bakerange.get(SpaceSwitcher.locator_endinit_attrname, False):
            self.end = bakerange.get(SpaceSwitcher.locator_end_attrname, None)
        else:
            self.end = None

    def _create_constraint_locator(self, parent):
        self.locator = spaceLocator(name='%s%s' % (self.__class__.locator_prefix,
                                                   re.sub(r':', '_', self.target.name())))
        if parent and isinstance(parent, nodetypes.Transform):
            self.locator.setParent(parent)
            self.parent = parent

        # add attribute to link target
        self.locator.addAttr(self.__class__.locator_target_attrname, attributeType='message')
        src_attr = self.target.attr('message')
        src_attr.connect(self.locator.attr(self.__class__.locator_target_attrname))

        # add bake start attributes
        self.locator.addAttr(self.__class__.locator_startinit_attrname, attributeType='bool')
        self.locator.attr(self.__class__.locator_startinit_attrname).set(False)

        self.locator.addAttr(self.__class__.locator_start_attrname, attributeType='float')

        # add bake end attributes
        self.locator.addAttr(self.__class__.locator_endinit_attrname, attributeType='bool')
        self.locator.attr(self.__class__.locator_endinit_attrname).set(False)

        self.locator.addAttr(self.__class__.locator_end_attrname, attributeType='float')

        # Set locator scale to handy value
        scale_x, scale_y, scale_z = self.locator.attr('scale').get()

        self.locator.attr('scale').set(1.0, 1.0, 1.0)

        bb = exactWorldBoundingBox(self.target)
        local_scale = OpenMaya2.MDistance.internalToUI((bb[3] - bb[0] + bb[4] - bb[1] + bb[5] - bb[2]) / 3.25)

        self.locator.getShape().attr('localScale').set(local_scale * scale_x,
                                                       local_scale * scale_y,
                                                       local_scale * scale_z)

    def list_target_constraints(self, typ):
        """
        Parameters:
            typ: unicode
                Constraint type. 'translate' or 'rotate' can be accepted.

        Return value:
            A list of constraint nodes. list of pymel.core.general.PyNode

        Description:
            Obtains constraint nodes which drive the target node's attributes
            which typ specifies.
        """

        if not self.target or not self.locator:
            return []

        constraints = set()
        for r in ['X', 'Y', 'Z']:
            dg_iter = OpenMaya.MItDependencyGraph(self.target.attr('%s%s' % (typ, r)).__apimplug__(),
                                                  self.__class__.constraint_types[typ],
                                                  OpenMaya.MItDependencyGraph.kUpstream,
                                                  OpenMaya.MItDependencyGraph.kBreadthFirst,
                                                  OpenMaya.MItDependencyGraph.kNodeLevel)
            while not dg_iter.isDone():
                try:
                    fn_node = OpenMaya.MFnDependencyNode(dg_iter.currentItem())
                except Exception as err:
                    print(str(err))
                    raise err
                else:
                    if fn_node:
                        constraint = PyNode(fn_node.name())
                        if utils.is_affected(self.locator, constraint):
                            constraints.add(constraint)
                dg_iter.next()

        return list(constraints)

    def list_driven_target_channels(self, typ):
        """
        Parameters:
            typ: unicode
                Constraint type. 'translate' or 'rotate' can be accepted.

        Return value:
            A list of driven attributes. list of pymel.core.general.Attribute

        Description:
            Obtains component attributes of target node's typ attribute which
            are really driven by constraint locator.
        """

        if not self.target or not self.locator:
            return []

        results = []
        for r in ['X', 'Y', 'Z']:
            attr = self.target.attr('%s%s' % (typ, r))
            if utils.is_affected(self.locator, attr):
                results.append(attr)

        return results

    def _create_constraints(self, parent, translate_switches, rotate_switches, for_bake=False):
        self._create_constraint_locator(parent)

        # get target world translation and world rotation
        translation = self.target.getTranslation(space='world')
        rotation = utils.get_rotation(self.target)
        rotation_order = self.target.getRotationOrder()

        # set locator world position and world orientation to target
        xform(self.locator, translation=translation, worldSpace=True)
        self.locator.setRotationOrder(rotation_order, True)
        xform(self.locator, rotation=rotation, worldSpace=True)

        result = {'channels':[], 'translate_constraint':None, 'rotate_constraint':None}

        # create point constraint
        skip_list = [r for i, r in enumerate(['X', 'Y', 'Z'])
                     if not translate_switches[i] or not utils.is_attr_drivable(self.target.attr('translate%s' % r))]
        if len(skip_list) < 3:
            if for_bake:
                result['translate_constraint'] = pointConstraint([self.target], [self.locator],
                                                                 maintainOffset=True, skip=skip_list)
                result['channels'].extend([self.locator.attr('translate%s' % r) for r in ['X', 'Y', 'Z']])
            else:
                pointConstraint([self.locator], [self.target], maintainOffset=True, skip=skip_list)

        # create orient constraint
        skip_list = [r for i, r in enumerate(['X', 'Y', 'Z'])
                     if not rotate_switches[i] or not utils.is_attr_drivable(self.target.attr('rotate%s' % r))]
        if len(skip_list) < 3:
            if for_bake:
                result['rotate_constraint'] = orientConstraint([self.target], [self.locator],
                                                               maintainOffset=True, skip=skip_list)
                result['channels'].extend([self.locator.attr('rotate%s' % r) for r in ['X', 'Y', 'Z']])
            else:
                orientConstraint([self.locator], [self.target], maintainOffset=True, skip=skip_list)

        return result

    def _restore_constraints(self, translate_switches, rotate_switches):
        # restore translate constraint
        skip_list = [r for i, r in enumerate(['X', 'Y', 'Z'])
                     if not translate_switches[i] or not utils.is_attr_drivable(self.target.attr('translate%s' % r))]
        if len(skip_list) < 3:
            for r in ['X', 'Y', 'Z']:
                if not r in skip_list:
                    attr = self.target.attr('translate%s' % r)
                    inputs = attr.inputs(plugs=True)
                    if inputs:
                        inputs[0].disconnect(attr)
            pointConstraint([self.locator], [self.target], maintainOffset=True, skip=skip_list)

        # restore orient constraint
        skip_list = [r for i, r in enumerate(['X', 'Y', 'Z'])
                     if not rotate_switches[i] or not utils.is_attr_drivable(self.target.attr('rotate%s' % r))]
        if len(skip_list) < 3:
            for r in ['X', 'Y', 'Z']:
                if not r in skip_list:
                    attr = self.target.attr('rotate%s' % r)
                    inputs = attr.inputs(plugs=True)
                    if inputs:
                        inputs[0].disconnect(attr)
            orientConstraint([self.locator], [self.target], maintainOffset=True, skip=skip_list)

    def switch_space(self, parent, translate_switches, rotate_switches, bake=False, start=1, end=24):
        """
        Parameters:
            parent: pymel.core.general.PyNode
                A transform node which you want make serve as
                temporary parent.
            translate_switches: [bool, bool, bool]
                Translate constraint switch for x, y and z
                component respectively.
            rotate_switches: [bool, bool, bool]
                Rotate constraint switch for x, y and z
                component respectively.
            bake: bool
                If True, keyframes are baked to constraint locator so that
                target's animation is kept the same after constraints
                are made.
            start: int
                Start frame of keyframe bake.
            end: int
                End frame of keyframe bake.

        Return value:
            Constraint locator, which is created to constrain the target node.
            pymel.core.general.PyNode

        Description:
            Creates a new locator under parent as the constraint locator and
            constraint nodes which drive the target node, according to
            translate_switches and rotate_switches channel settings.
            If bake is True, keyframes are baked to constraint locator so that
            target's animation is kept the same after constraints are made.
        """

        if self.target is None:
            error('Target to switch space is not set yet.')

        if self.locator:
            error('Target already has space-swicth locator.')

        if not translate_switches[0] and not translate_switches[1] and not translate_switches[2] and\
           not rotate_switches[0] and not rotate_switches[1] and not rotate_switches[2]:
               raise Exception('Failed to switch space, since constraint switches are all disabled.')

        result = self._create_constraints(parent, translate_switches, rotate_switches, for_bake=bake)

        if bake:
            self.start = start
            self.locator.attr(SpaceSwitcher.locator_startinit_attrname).set(True)
            self.locator.attr(SpaceSwitcher.locator_start_attrname).set(self.start)

            self.end = end
            self.locator.attr(SpaceSwitcher.locator_endinit_attrname).set(True)
            self.locator.attr(SpaceSwitcher.locator_end_attrname).set(self.end)

            utils.bake_animation(result['channels'], self.start, self.end)

            try:
                delete(result['translate_constraint'])
            except Exception as err:
                print(str(err))
                print('Failed to delete point constraint: %s' % result['translate_constraint'].name())

            try:
                delete(result['rotate_constraint'])
            except Exception as err:
                print(str(err))
                print('Failed to delete orient constraint: %s' % result['rotate_constraint'].name())

            self._restore_constraints(translate_switches, rotate_switches)

        return self.locator

    def delete_constraints(self, bake=False, start=None, end=None):
        """
        Parameters:
            bake: bool
                If True, the resultant animation is baked to the target node
                before constraints are deleted.
            start: NoneType or int
                Start frame of keyframe bake. If None is specified,
                start frame is obtained from the value stored in locator's
                custom attribute.
                A specific integer value can be used to override the start
                frame stored as custom attribute.
            end: NoneType or int
                End frame of keyframe bake. If None is specified, end frame is
                obtained from the value stored in locator's custom attribute.
                A specific integer value can be used to override the end frame
                stored as custom attribute.

        Return value:
            The target node. pymel.core.general.PyNode

        Description:
            Deletes the constraint locator and constraint nodes which drive
            the target.
            If bake is True, the resultant animation is baked to the target
            node before constraint structure is deleted.
        """

        if bake:
            channels = self.list_driven_target_channels('translate') + self.list_driven_target_channels('rotate')
            if channels:
                _start = start
                _end = end
                if start is None:
                    _start = self.start
                if end is None:
                    _end = self.end
                utils.bake_animation(channels, _start, _end)

        for constraint in self.list_target_constraints('translate'):
            try:
                delete(constraint)
            except Exception as err:
                print(str(err))
                print('Failed to delete: %s' % constraint.name())

        for constraint in self.list_target_constraints('rotate'):
            try:
                delete(constraint)
            except Exception as err:
                print(str(err))
                print('Failed to delete: %s' % constraint.name())

        try:
            delete(self.locator)
        except Exception as err:
            print(str(err))
            print('Failed to delete: %s' % self.locator)

        self.locator = None
        self.parent = None
        self.start = None
        self.end = None

        return self.target


def switch_space(targets, parent, translate_switches=[True, True, True], rotate_switches=[True, True, True],
                 bake=False, start=1, end=24):
    """
    Parameters:
        targets: list of PyNode or PyNode or list of unicode or unicode or
                 NoneType
            Target transform node(s).
            If None is specified, current selection is used as targets.
        parent: PyNode or unicode
            A transform node which you want to make serve as temporary parent.
        translate_switches: [bool, bool, bool]
            Translate constraint switch for x, y and z component respectively.
        rotate_switches: [bool, bool, bool]
            Rotate constraint switch for x, y and z component respectively.
        bake : bool
            If True, keyframes are baked to constraint locators so that
            targets' animations are kept the same after constraints are made.
        start: int
            Start frame of keyframe bake.
        end: int
            End frame of keyframe bake.

    Return value
        A list of constraint locaros, which are created to constrain the
        target nodes. list of PyNode

    Description:
        Creates a new locator under parent as the constraint locator and
        constraint nodes which drive each target node according to
        translate_switches and rotate_switches channel settings.  
        If bake is True, keyframes are baked to each constraint locator
        so that each target's animation is kept the same after constraints
        are made.
        As parameter targets, several argument types can be accepted and
        if None is specified, current selected nodes are considered as
        targets.
    """

    _targets = None
    if targets is None:
        selections = ls(selection=1)
        if not selections:
            raise Exception('Current selection is empty.')
        _targets = selections
    else:
        _targets = utils.get_pynodes(targets, nodetype=nodetypes.Transform)

    _parent = None
    if parent:
        try:
            _parent = PyNode(parent)
        except Exception as err:
            print(str(err))
            print('Failed to obtain PyNode("%s")' % str(parent))
            raise err
        else:
            if not isinstance(_parent, nodetypes.Transform):
                raise ValueError('argument "parent" must be a transform or None.')

    if not translate_switches[0] and not translate_switches[1] and not translate_switches[2] and\
       not rotate_switches[0] and not rotate_switches[1] and not rotate_switches[2]:
           raise Exception('Failed to switch space, since constraint switches are all disabled.')

    locators = [SpaceSwitcher(target=target).switch_space(_parent, translate_switches, rotate_switches,
                                                          bake=bake, start=start, end=end) for target in _targets]

    select(locators, replace=True)

    return locators


def delete_switch_space_constraints(targets=None, locators=None, bake=False, start=None, end=None):
    """
    Parameters:
        targets: list of PyNode or PyNode or list of unicode or unicode or
                 NoneType
            Target transform node(s).
        locators: list of PyNode or PyNode or list of unicode or unicode or
                  NoneType
            Constraint locator node(s).
        bake: bool
            If True, the resultant animation is baked to the target node
            before constraints are deleted.
        start: NoneType or int
            Start frame of keyframe bake. If None is specified, start frame is
            obtained from the value stored in locator's custom attribute.
            A specific integer value can be used to override the start frame
            stored as custom attribute.
        end: NoneType or int
            End frame of keyframe bake. If `None` is specified, end frame is
            obtained from the value stored in locator's custom attribute.
            A specific integer value can be used to override the end frame
            stored as custom attribute.

    Return value:
        A list of target nodes. list of PyNode

    Description:
        Deletes the specified constraint locator nodes and their constraint
        nodes.
        Constraint locator nodes can be obtained by specifying target nodes
        also.
        If both targets and locators is None, constraint locators are obtained
        from current selection.
        If bake is True, the resultant animation is baked to each target node
        before constraint structure is deleted.
    """

    _locators = []
    if targets is None and locators is None:
        selections = ls(selection=1)
        if not selections:
            raise Exception('Current selection is empty.')
        for selection in selections:
            if SpaceSwitcher.get_target_from_locator(selection) and not selection in _locators:
                _locators.append(selection)
            else:
                locator = SpaceSwitcher.get_locator_from_target(selection)
                if locator and not locator in _locators:
                    _locators.append(locator)
    else:
        if locators:
            _locators = utils.get_pynodes(locators, nodetype=nodetypes.Transform)
        if targets:
            for target in utils.get_pynodes(targets, nodetype=nodetypes.Transform):
                locator = SpaceSwitcher.get_locator_from_target(target)
                if locator and not locator in _locators:
                    _locators.append(locator)

    results = [SpaceSwitcher(locator=locator).delete_constraints(bake=bake, start=start, end=end)
               for locator in _locators]

    if results:
        select(results, replace=True)

    return results
