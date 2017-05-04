from pymel.core import *

import maya.OpenMayaUI as OpenMayaUI

from Qt import QtCore, QtGui, QtWidgets
from Qt.QtCore import Slot

try:
    from shiboken2 import wrapInstance
except:
    from shiboken import wrapInstance

from . import core


class Ui_SpaceSwitcherWindow(object):
    def setupUi(self, SpaceSwitcherWindow):
        SpaceSwitcherWindow.setObjectName("SpaceSwitcherWindow")
        SpaceSwitcherWindow.setWindowModality(QtCore.Qt.NonModal)
        SpaceSwitcherWindow.resize(246, 256)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SpaceSwitcherWindow.sizePolicy().hasHeightForWidth())
        SpaceSwitcherWindow.setSizePolicy(sizePolicy)
        SpaceSwitcherWindow.setMinimumSize(QtCore.QSize(246, 256))
        SpaceSwitcherWindow.setMaximumSize(QtCore.QSize(246, 256))
        SpaceSwitcherWindow.setWindowTitle("SpaceSwitcher")
        SpaceSwitcherWindow.setWindowOpacity(1.0)
        SpaceSwitcherWindow.setToolTip("")
        SpaceSwitcherWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralWidget = QtWidgets.QWidget(SpaceSwitcherWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralWidget.setObjectName("centralWidget")
        self.layout_centralWidget = QtWidgets.QHBoxLayout(self.centralWidget)
        self.layout_centralWidget.setSpacing(2)
        self.layout_centralWidget.setContentsMargins(2, 2, 2, 2)
        self.layout_centralWidget.setObjectName("layout_centralWidget")
        self.frame_Root = QtWidgets.QFrame(self.centralWidget)
        self.frame_Root.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_Root.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Root.setObjectName("frame_Root")
        self.layout_Root = QtWidgets.QVBoxLayout(self.frame_Root)
        self.layout_Root.setSpacing(2)
        self.layout_Root.setContentsMargins(2, 2, 2, 2)
        self.layout_Root.setObjectName("layout_Root")
        self.frame_Parent = QtWidgets.QFrame(self.frame_Root)
        self.frame_Parent.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Parent.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Parent.setObjectName("frame_Parent")
        self.layout_Parent = QtWidgets.QVBoxLayout(self.frame_Parent)
        self.layout_Parent.setSpacing(4)
        self.layout_Parent.setContentsMargins(2, 2, 2, 2)
        self.layout_Parent.setObjectName("layout_Parent")
        self.frame_LabelAndButton = QtWidgets.QFrame(self.frame_Parent)
        self.frame_LabelAndButton.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_LabelAndButton.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_LabelAndButton.setObjectName("frame_LabelAndButton")
        self.layout_LabelAndButton = QtWidgets.QHBoxLayout(self.frame_LabelAndButton)
        self.layout_LabelAndButton.setSpacing(2)
        self.layout_LabelAndButton.setContentsMargins(0, 0, 0, 0)
        self.layout_LabelAndButton.setObjectName("layout_LabelAndButton")
        self.label_Parent = QtWidgets.QLabel(self.frame_LabelAndButton)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Parent.sizePolicy().hasHeightForWidth())
        self.label_Parent.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_Parent.setFont(font)
        self.label_Parent.setText("Parent")
        self.label_Parent.setObjectName("label_Parent")
        self.layout_LabelAndButton.addWidget(self.label_Parent)
        self.pushButton_SetParent = QtWidgets.QPushButton(self.frame_LabelAndButton)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_SetParent.sizePolicy().hasHeightForWidth())
        self.pushButton_SetParent.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_SetParent.setFont(font)
        self.pushButton_SetParent.setText("Set")
        self.pushButton_SetParent.setObjectName("pushButton_SetParent")
        self.layout_LabelAndButton.addWidget(self.pushButton_SetParent)
        self.pushButton_ClearParent = QtWidgets.QPushButton(self.frame_LabelAndButton)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_ClearParent.sizePolicy().hasHeightForWidth())
        self.pushButton_ClearParent.setSizePolicy(sizePolicy)
        self.pushButton_ClearParent.setMaximumSize(QtCore.QSize(52, 16777215))
        self.pushButton_ClearParent.setText("Clear")
        self.pushButton_ClearParent.setObjectName("pushButton_ClearParent")
        self.layout_LabelAndButton.addWidget(self.pushButton_ClearParent)
        self.layout_Parent.addWidget(self.frame_LabelAndButton)
        self.lineEdit_Parent = QtWidgets.QLineEdit(self.frame_Parent)
        self.lineEdit_Parent.setText("")
        self.lineEdit_Parent.setObjectName("lineEdit_Parent")
        self.layout_Parent.addWidget(self.lineEdit_Parent)
        self.layout_Root.addWidget(self.frame_Parent)
        self.frame_CreateConstraint = QtWidgets.QFrame(self.frame_Root)
        self.frame_CreateConstraint.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_CreateConstraint.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_CreateConstraint.setObjectName("frame_CreateConstraint")
        self.layout_CreateConstraint = QtWidgets.QVBoxLayout(self.frame_CreateConstraint)
        self.layout_CreateConstraint.setSpacing(0)
        self.layout_CreateConstraint.setContentsMargins(2, 2, 2, 2)
        self.layout_CreateConstraint.setObjectName("layout_CreateConstraint")
        self.label_CreateConstraint = QtWidgets.QLabel(self.frame_CreateConstraint)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_CreateConstraint.sizePolicy().hasHeightForWidth())
        self.label_CreateConstraint.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_CreateConstraint.setFont(font)
        self.label_CreateConstraint.setToolTip("Create constraints: Select nodes to be constrained")
        self.label_CreateConstraint.setText("Create Constraint")
        self.label_CreateConstraint.setObjectName("label_CreateConstraint")
        self.layout_CreateConstraint.addWidget(self.label_CreateConstraint)
        self.frame_TranslateCheckBoxes = QtWidgets.QFrame(self.frame_CreateConstraint)
        self.frame_TranslateCheckBoxes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_TranslateCheckBoxes.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_TranslateCheckBoxes.setObjectName("frame_TranslateCheckBoxes")
        self.layout_TranslateCheckBoxes = QtWidgets.QHBoxLayout(self.frame_TranslateCheckBoxes)
        self.layout_TranslateCheckBoxes.setSpacing(8)
        self.layout_TranslateCheckBoxes.setContentsMargins(0, 6, 0, 0)
        self.layout_TranslateCheckBoxes.setObjectName("layout_TranslateCheckBoxes")
        self.label_Translate = QtWidgets.QLabel(self.frame_TranslateCheckBoxes)
        self.label_Translate.setText("Translate")
        self.label_Translate.setObjectName("label_Translate")
        self.layout_TranslateCheckBoxes.addWidget(self.label_Translate)
        self.checkBox_TranslateX = QtWidgets.QCheckBox(self.frame_TranslateCheckBoxes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_TranslateX.sizePolicy().hasHeightForWidth())
        self.checkBox_TranslateX.setSizePolicy(sizePolicy)
        self.checkBox_TranslateX.setText("X")
        self.checkBox_TranslateX.setChecked(True)
        self.checkBox_TranslateX.setObjectName("checkBox_TranslateX")
        self.layout_TranslateCheckBoxes.addWidget(self.checkBox_TranslateX)
        self.checkBox_TranslateY = QtWidgets.QCheckBox(self.frame_TranslateCheckBoxes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_TranslateY.sizePolicy().hasHeightForWidth())
        self.checkBox_TranslateY.setSizePolicy(sizePolicy)
        self.checkBox_TranslateY.setText("Y")
        self.checkBox_TranslateY.setChecked(True)
        self.checkBox_TranslateY.setObjectName("checkBox_TranslateY")
        self.layout_TranslateCheckBoxes.addWidget(self.checkBox_TranslateY)
        self.checkBox_TranslateZ = QtWidgets.QCheckBox(self.frame_TranslateCheckBoxes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_TranslateZ.sizePolicy().hasHeightForWidth())
        self.checkBox_TranslateZ.setSizePolicy(sizePolicy)
        self.checkBox_TranslateZ.setText("Z")
        self.checkBox_TranslateZ.setChecked(True)
        self.checkBox_TranslateZ.setObjectName("checkBox_TranslateZ")
        self.layout_TranslateCheckBoxes.addWidget(self.checkBox_TranslateZ)
        self.layout_CreateConstraint.addWidget(self.frame_TranslateCheckBoxes)
        self.frame_RotateCheckBoxes = QtWidgets.QFrame(self.frame_CreateConstraint)
        self.frame_RotateCheckBoxes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_RotateCheckBoxes.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_RotateCheckBoxes.setObjectName("frame_RotateCheckBoxes")
        self.layout_RotateCheckBoxes = QtWidgets.QHBoxLayout(self.frame_RotateCheckBoxes)
        self.layout_RotateCheckBoxes.setSpacing(8)
        self.layout_RotateCheckBoxes.setContentsMargins(0, 0, 0, 0)
        self.layout_RotateCheckBoxes.setObjectName("layout_RotateCheckBoxes")
        self.label_Rotate = QtWidgets.QLabel(self.frame_RotateCheckBoxes)
        self.label_Rotate.setText("Rotate")
        self.label_Rotate.setObjectName("label_Rotate")
        self.layout_RotateCheckBoxes.addWidget(self.label_Rotate)
        self.checkBox_RotateX = QtWidgets.QCheckBox(self.frame_RotateCheckBoxes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_RotateX.sizePolicy().hasHeightForWidth())
        self.checkBox_RotateX.setSizePolicy(sizePolicy)
        self.checkBox_RotateX.setText("X")
        self.checkBox_RotateX.setChecked(True)
        self.checkBox_RotateX.setObjectName("checkBox_RotateX")
        self.layout_RotateCheckBoxes.addWidget(self.checkBox_RotateX)
        self.checkBox_RotateY = QtWidgets.QCheckBox(self.frame_RotateCheckBoxes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_RotateY.sizePolicy().hasHeightForWidth())
        self.checkBox_RotateY.setSizePolicy(sizePolicy)
        self.checkBox_RotateY.setText("Y")
        self.checkBox_RotateY.setChecked(True)
        self.checkBox_RotateY.setObjectName("checkBox_RotateY")
        self.layout_RotateCheckBoxes.addWidget(self.checkBox_RotateY)
        self.checkBox_RotateZ = QtWidgets.QCheckBox(self.frame_RotateCheckBoxes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_RotateZ.sizePolicy().hasHeightForWidth())
        self.checkBox_RotateZ.setSizePolicy(sizePolicy)
        self.checkBox_RotateZ.setText("Z")
        self.checkBox_RotateZ.setChecked(True)
        self.checkBox_RotateZ.setObjectName("checkBox_RotateZ")
        self.layout_RotateCheckBoxes.addWidget(self.checkBox_RotateZ)
        self.layout_CreateConstraint.addWidget(self.frame_RotateCheckBoxes)
        self.frame_CreateConstraintButtons = QtWidgets.QFrame(self.frame_CreateConstraint)
        self.frame_CreateConstraintButtons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_CreateConstraintButtons.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_CreateConstraintButtons.setObjectName("frame_CreateConstraintButtons")
        self.layout_CreateConstraintButtons = QtWidgets.QHBoxLayout(self.frame_CreateConstraintButtons)
        self.layout_CreateConstraintButtons.setSpacing(2)
        self.layout_CreateConstraintButtons.setContentsMargins(0, 0, 0, 0)
        self.layout_CreateConstraintButtons.setObjectName("layout_CreateConstraintButtons")
        self.pushButton_CreateConstraint = QtWidgets.QPushButton(self.frame_CreateConstraintButtons)
        self.pushButton_CreateConstraint.setToolTip("")
        self.pushButton_CreateConstraint.setText("Create")
        self.pushButton_CreateConstraint.setObjectName("pushButton_CreateConstraint")
        self.layout_CreateConstraintButtons.addWidget(self.pushButton_CreateConstraint)
        self.pushButton_CreateAndBakeConstraint = QtWidgets.QPushButton(self.frame_CreateConstraintButtons)
        self.pushButton_CreateAndBakeConstraint.setText("Create and Bake")
        self.pushButton_CreateAndBakeConstraint.setObjectName("pushButton_CreateAndBakeConstraint")
        self.layout_CreateConstraintButtons.addWidget(self.pushButton_CreateAndBakeConstraint)
        self.layout_CreateConstraint.addWidget(self.frame_CreateConstraintButtons)
        self.layout_Root.addWidget(self.frame_CreateConstraint)
        self.frame_DeleteConstraint = QtWidgets.QFrame(self.frame_Root)
        self.frame_DeleteConstraint.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_DeleteConstraint.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_DeleteConstraint.setObjectName("frame_DeleteConstraint")
        self.layout_DeleteConstraint = QtWidgets.QVBoxLayout(self.frame_DeleteConstraint)
        self.layout_DeleteConstraint.setSpacing(0)
        self.layout_DeleteConstraint.setContentsMargins(2, 2, 2, 2)
        self.layout_DeleteConstraint.setObjectName("layout_DeleteConstraint")
        self.label_DeleteConstraint = QtWidgets.QLabel(self.frame_DeleteConstraint)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_DeleteConstraint.sizePolicy().hasHeightForWidth())
        self.label_DeleteConstraint.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_DeleteConstraint.setFont(font)
        self.label_DeleteConstraint.setToolTip("Delete constraints: Select constraining locators")
        self.label_DeleteConstraint.setText("Delete Constraint")
        self.label_DeleteConstraint.setObjectName("label_DeleteConstraint")
        self.layout_DeleteConstraint.addWidget(self.label_DeleteConstraint)
        self.frame_DeleteConstraintButtons = QtWidgets.QFrame(self.frame_DeleteConstraint)
        self.frame_DeleteConstraintButtons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_DeleteConstraintButtons.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_DeleteConstraintButtons.setObjectName("frame_DeleteConstraintButtons")
        self.layout_DeleteConstraintButtons = QtWidgets.QHBoxLayout(self.frame_DeleteConstraintButtons)
        self.layout_DeleteConstraintButtons.setSpacing(2)
        self.layout_DeleteConstraintButtons.setContentsMargins(0, 4, 0, 0)
        self.layout_DeleteConstraintButtons.setObjectName("layout_DeleteConstraintButtons")
        self.pushButton_DeleteConstraint = QtWidgets.QPushButton(self.frame_DeleteConstraintButtons)
        self.pushButton_DeleteConstraint.setToolTip("")
        self.pushButton_DeleteConstraint.setText("Delete")
        self.pushButton_DeleteConstraint.setObjectName("pushButton_DeleteConstraint")
        self.layout_DeleteConstraintButtons.addWidget(self.pushButton_DeleteConstraint)
        self.pushButton_BakeAndDeleteConstraint = QtWidgets.QPushButton(self.frame_DeleteConstraintButtons)
        self.pushButton_BakeAndDeleteConstraint.setText("Bake and Delete")
        self.pushButton_BakeAndDeleteConstraint.setObjectName("pushButton_BakeAndDeleteConstraint")
        self.layout_DeleteConstraintButtons.addWidget(self.pushButton_BakeAndDeleteConstraint)
        self.layout_DeleteConstraint.addWidget(self.frame_DeleteConstraintButtons)
        self.layout_Root.addWidget(self.frame_DeleteConstraint)
        self.frame_BakeRange = QtWidgets.QFrame(self.frame_Root)
        self.frame_BakeRange.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_BakeRange.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_BakeRange.setObjectName("frame_BakeRange")
        self.layout_BakeRange = QtWidgets.QVBoxLayout(self.frame_BakeRange)
        self.layout_BakeRange.setSpacing(0)
        self.layout_BakeRange.setContentsMargins(2, 2, 2, 2)
        self.layout_BakeRange.setObjectName("layout_BakeRange")
        self.frame_BakeRangeTop = QtWidgets.QFrame(self.frame_BakeRange)
        self.frame_BakeRangeTop.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_BakeRangeTop.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_BakeRangeTop.setObjectName("frame_BakeRangeTop")
        self.layout_BakeRangeTop = QtWidgets.QHBoxLayout(self.frame_BakeRangeTop)
        self.layout_BakeRangeTop.setSpacing(0)
        self.layout_BakeRangeTop.setContentsMargins(0, 0, 0, 0)
        self.layout_BakeRangeTop.setObjectName("layout_BakeRangeTop")
        self.label_BakeRange = QtWidgets.QLabel(self.frame_BakeRangeTop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_BakeRange.sizePolicy().hasHeightForWidth())
        self.label_BakeRange.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_BakeRange.setFont(font)
        self.label_BakeRange.setText("Bake Range")
        self.label_BakeRange.setObjectName("label_BakeRange")
        self.layout_BakeRangeTop.addWidget(self.label_BakeRange)
        self.pushButton_SetFromTimeline = QtWidgets.QPushButton(self.frame_BakeRangeTop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_SetFromTimeline.sizePolicy().hasHeightForWidth())
        self.pushButton_SetFromTimeline.setSizePolicy(sizePolicy)
        self.pushButton_SetFromTimeline.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_SetFromTimeline.setText("Set from timeline")
        self.pushButton_SetFromTimeline.setObjectName("pushButton_SetFromTimeline")
        self.layout_BakeRangeTop.addWidget(self.pushButton_SetFromTimeline)
        self.layout_BakeRange.addWidget(self.frame_BakeRangeTop)
        self.frame_BakeRangeSpinBoxes = QtWidgets.QFrame(self.frame_BakeRange)
        self.frame_BakeRangeSpinBoxes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_BakeRangeSpinBoxes.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_BakeRangeSpinBoxes.setObjectName("frame_BakeRangeSpinBoxes")
        self.layout_BakeRangeSpinBoxes = QtWidgets.QHBoxLayout(self.frame_BakeRangeSpinBoxes)
        self.layout_BakeRangeSpinBoxes.setSpacing(2)
        self.layout_BakeRangeSpinBoxes.setContentsMargins(0, 4, 0, 0)
        self.layout_BakeRangeSpinBoxes.setObjectName("layout_BakeRangeSpinBoxes")
        self.spinBox_BakeStart = QtWidgets.QSpinBox(self.frame_BakeRangeSpinBoxes)
        self.spinBox_BakeStart.setAccelerated(True)
        self.spinBox_BakeStart.setMinimum(-16777215)
        self.spinBox_BakeStart.setMaximum(16777215)
        self.spinBox_BakeStart.setProperty("value", 1)
        self.spinBox_BakeStart.setObjectName("spinBox_BakeStart")
        self.layout_BakeRangeSpinBoxes.addWidget(self.spinBox_BakeStart)
        self.spinBox_BakeEnd = QtWidgets.QSpinBox(self.frame_BakeRangeSpinBoxes)
        self.spinBox_BakeEnd.setAccelerated(True)
        self.spinBox_BakeEnd.setMinimum(-16777215)
        self.spinBox_BakeEnd.setMaximum(16777215)
        self.spinBox_BakeEnd.setProperty("value", 24)
        self.spinBox_BakeEnd.setObjectName("spinBox_BakeEnd")
        self.layout_BakeRangeSpinBoxes.addWidget(self.spinBox_BakeEnd)
        self.layout_BakeRange.addWidget(self.frame_BakeRangeSpinBoxes)
        self.layout_Root.addWidget(self.frame_BakeRange)
        self.layout_centralWidget.addWidget(self.frame_Root)
        SpaceSwitcherWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(SpaceSwitcherWindow)
        QtCore.QMetaObject.connectSlotsByName(SpaceSwitcherWindow)

    def retranslateUi(self, SpaceSwitcherWindow):
        pass


class ControlMainWindow(QtWidgets.QMainWindow):
    def __init__(self, window_title, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.window_title = window_title
        self.ui = Ui_SpaceSwitcherWindow()
        self.ui.setupUi(self)

        # signal - slot connections
        self.ui.pushButton_SetParent.clicked.connect(self.setParent_cliciked)
        self.ui.pushButton_ClearParent.clicked.connect(self.clearParent_clicked)
        self.ui.pushButton_CreateConstraint.clicked.connect(self.createConstraint_clicked)
        self.ui.pushButton_CreateAndBakeConstraint.clicked.connect(self.createAndBakeConstraint_clicked)
        self.ui.pushButton_DeleteConstraint.clicked.connect(self.deleteConstraint_clicked)
        self.ui.pushButton_BakeAndDeleteConstraint.clicked.connect(self.bakeAndDeleteConstraint_clicked)
        self.ui.pushButton_SetFromTimeline.clicked.connect(self.setBakeRange_clicked)

    #
    # UI query methods
    #
    def get_parentname(self):
        return self.ui.lineEdit_Parent.text()

    def get_translate_switches(self):
        return (self.ui.checkBox_TranslateX.isChecked(),
                self.ui.checkBox_TranslateY.isChecked(),
                self.ui.checkBox_TranslateZ.isChecked())

    def get_rotate_switches(self):
        return (self.ui.checkBox_RotateX.isChecked(),
                self.ui.checkBox_RotateY.isChecked(),
                self.ui.checkBox_RotateZ.isChecked())

    def get_bakestart(self):
        return self.ui.spinBox_BakeStart.value()

    def get_bakeend(self):
        return self.ui.spinBox_BakeEnd.value()

    #
    # UI edit methods
    #
    def set_parentname(self, name=None):
        _name = name
        if name is None:
            selections = ls(selection=True)
            if selections:
                _name = selections[0].name()
        if _name is not None:
            self.ui.lineEdit_Parent.setText(_name)

    def set_bakestart(self, value):
        self.ui.spinBox_BakeStart.setValue(value)

    def set_bakeend(self, value):
        self.ui.spinBox_BakeEnd.setValue(value)

    #
    # UI update methods
    #
    def update_bakerange(self):
        self.set_bakestart(playbackOptions(q=1, minTime=True))
        self.set_bakeend(playbackOptions(q=1, maxTime=True))

    def update_all(self):
        self.update_bakerange()

    #
    # slot callback functions
    #
    @Slot()
    def setParent_cliciked(self):
        self.set_parentname()

    @Slot()
    def clearParent_clicked(self):
        self.set_parentname(name = '')

    @Slot()
    def createConstraint_clicked(self):
        undoInfo(openChunk=True)

        parent = None
        try:
            parent = PyNode(self.get_parentname())
        except:
            pass

        try:
            core.switch_space(None, parent,
                              translate_switches=self.get_translate_switches(),
                              rotate_switches=self.get_rotate_switches())
        except Exception as err:
            print(str(err))
        finally:
            undoInfo(closeChunk=True)

    @Slot()
    def createAndBakeConstraint_clicked(self):
        undoInfo(openChunk=True)

        parent = None
        try:
            parent = PyNode(self.get_parentname())
        except:
            pass

        try:
            core.switch_space(None, parent, self.get_translate_switches(), self.get_rotate_switches(),
                              bake=True, start=self.get_bakestart(), end=self.get_bakeend())
        except Exception as err:
            print(str(err))
        finally:
            undoInfo(closeChunk=True)

    @Slot()
    def deleteConstraint_clicked(self):
        undoInfo(openChunk=True)
        try:
            core.delete_switch_space_constraints()
        except Exception as err:
            print(str(err))
        finally:
            undoInfo(closeChunk=True)

    @Slot()
    def bakeAndDeleteConstraint_clicked(self):
        undoInfo(openChunk=True)
        try:
            core.delete_switch_space_constraints(bake=True, start=self.get_bakestart(), end=self.get_bakeend())
        except Exception as err:
            print(str(err))
        finally:
            undoInfo(closeChunk=True)

    @Slot()
    def setBakeRange_clicked(self):
        self.update_bakerange()


def launch_ui(window_title='SpaceSwitcher'):
    existing_win_ptr = OpenMayaUI.MQtUtil.findWindow('SpaceSwitcherWindow')
    if existing_win_ptr:
        existing_win = wrapInstance(long(existing_win_ptr), QtWidgets.QMainWindow)
        if existing_win:
            if existing_win.windowTitle() == window_title:
                existing_win.close()

    main_win = ControlMainWindow(window_title,
                                 parent=wrapInstance(long(OpenMayaUI.MQtUtil.mainWindow()), QtWidgets.QWidget))
    main_win.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    main_win.setWindowTitle(window_title)
    main_win.update_all()
    main_win.show()
