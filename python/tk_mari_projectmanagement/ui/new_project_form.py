# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_project_form.ui'
#
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from sgtk.platform.qt import QtCore, QtGui

class Ui_NewProjectForm(object):
    def setupUi(self, NewProjectForm):
        NewProjectForm.setObjectName("NewProjectForm")
        NewProjectForm.resize(540, 447)
        self.verticalLayout = QtGui.QVBoxLayout(NewProjectForm)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.info_label = QtGui.QLabel(NewProjectForm)
        self.info_label.setMinimumSize(QtCore.QSize(0, 0))
        self.info_label.setWordWrap(False)
        self.info_label.setObjectName("info_label")
        self.verticalLayout_2.addWidget(self.info_label)
        self.name_edit = QtGui.QLineEdit(NewProjectForm)
        self.name_edit.setMinimumSize(QtCore.QSize(0, 22))
        self.name_edit.setEchoMode(QtGui.QLineEdit.Normal)
        self.name_edit.setObjectName("name_edit")
        self.verticalLayout_2.addWidget(self.name_edit)
        self.name_preview_label = QtGui.QLabel(NewProjectForm)
        self.name_preview_label.setMinimumSize(QtCore.QSize(0, 0))
        self.name_preview_label.setWordWrap(True)
        self.name_preview_label.setObjectName("name_preview_label")
        self.verticalLayout_2.addWidget(self.name_preview_label)
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.label = QtGui.QLabel(NewProjectForm)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.publish_list = PublishListView(NewProjectForm)
        self.publish_list.setStyleSheet("#publish_list {\n"
"background-color: rgb(255, 128, 0);\n"
"}")
        self.publish_list.setObjectName("publish_list")
        self.verticalLayout_4.addWidget(self.publish_list)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.add_publish_btn = QtGui.QPushButton(NewProjectForm)
        self.add_publish_btn.setMinimumSize(QtCore.QSize(32, 0))
        self.add_publish_btn.setObjectName("add_publish_btn")
        self.horizontalLayout.addWidget(self.add_publish_btn)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.break_line = QtGui.QFrame(NewProjectForm)
        self.break_line.setFrameShape(QtGui.QFrame.HLine)
        self.break_line.setFrameShadow(QtGui.QFrame.Sunken)
        self.break_line.setObjectName("break_line")
        self.verticalLayout.addWidget(self.break_line)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(12, 8, 12, 12)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.cancel_btn = QtGui.QPushButton(NewProjectForm)
        self.cancel_btn.setMinimumSize(QtCore.QSize(90, 0))
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_3.addWidget(self.cancel_btn)
        self.create_btn = QtGui.QPushButton(NewProjectForm)
        self.create_btn.setMinimumSize(QtCore.QSize(90, 0))
        self.create_btn.setDefault(True)
        self.create_btn.setObjectName("create_btn")
        self.horizontalLayout_3.addWidget(self.create_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(NewProjectForm)
        QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL("clicked()"), NewProjectForm.close)
        QtCore.QMetaObject.connectSlotsByName(NewProjectForm)

    def retranslateUi(self, NewProjectForm):
        NewProjectForm.setWindowTitle(QtGui.QApplication.translate("NewProjectForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.info_label.setText(QtGui.QApplication.translate("NewProjectForm", "Please enter a name to use for the new project", None, QtGui.QApplication.UnicodeUTF8))
        self.name_preview_label.setText(QtGui.QApplication.translate("NewProjectForm", "Your new project will be called: <b>prefix_blah_blah</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("NewProjectForm", "Add publishes you would like to include in the project", None, QtGui.QApplication.UnicodeUTF8))
        self.add_publish_btn.setText(QtGui.QApplication.translate("NewProjectForm", "Add Publish...", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("NewProjectForm", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.create_btn.setText(QtGui.QApplication.translate("NewProjectForm", "Create Project", None, QtGui.QApplication.UnicodeUTF8))

from ..publish_list_view import PublishListView
from . import resources_rc
