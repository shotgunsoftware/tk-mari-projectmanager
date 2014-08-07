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
        NewProjectForm.resize(466, 242)
        self.verticalLayout = QtGui.QVBoxLayout(NewProjectForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setContentsMargins(12, 12, 12, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.info_label = QtGui.QLabel(NewProjectForm)
        self.info_label.setMinimumSize(QtCore.QSize(0, 32))
        self.info_label.setWordWrap(True)
        self.info_label.setObjectName("info_label")
        self.verticalLayout_2.addWidget(self.info_label)
        self.name_edit = QtGui.QLineEdit(NewProjectForm)
        self.name_edit.setMinimumSize(QtCore.QSize(0, 22))
        self.name_edit.setEchoMode(QtGui.QLineEdit.Password)
        self.name_edit.setObjectName("name_edit")
        self.verticalLayout_2.addWidget(self.name_edit)
        self.preview_label = QtGui.QLabel(NewProjectForm)
        self.preview_label.setMinimumSize(QtCore.QSize(0, 32))
        self.preview_label.setWordWrap(True)
        self.preview_label.setObjectName("preview_label")
        self.verticalLayout_2.addWidget(self.preview_label)
        spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(12, 8, 12, 12)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
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

        self.retranslateUi(NewProjectForm)
        QtCore.QMetaObject.connectSlotsByName(NewProjectForm)

    def retranslateUi(self, NewProjectForm):
        NewProjectForm.setWindowTitle(QtGui.QApplication.translate("NewProjectForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.info_label.setText(QtGui.QApplication.translate("NewProjectForm", "Enter a name for the new project:", None, QtGui.QApplication.UnicodeUTF8))
        self.preview_label.setText(QtGui.QApplication.translate("NewProjectForm", "[name preview]", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("NewProjectForm", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.create_btn.setText(QtGui.QApplication.translate("NewProjectForm", "Create", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
