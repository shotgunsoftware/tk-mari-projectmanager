# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_project_form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from sgtk.platform.qt import QtCore
for name, cls in QtCore.__dict__.items():
    if isinstance(cls, type): globals()[name] = cls

from sgtk.platform.qt import QtGui
for name, cls in QtGui.__dict__.items():
    if isinstance(cls, type): globals()[name] = cls


from ..publish_list_view import PublishListView

from  . import resources_rc

class Ui_NewProjectForm(object):
    def setupUi(self, NewProjectForm):
        if not NewProjectForm.objectName():
            NewProjectForm.setObjectName(u"NewProjectForm")
        NewProjectForm.resize(604, 473)
        self.verticalLayout = QVBoxLayout(NewProjectForm)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 4)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.info_label = QLabel(NewProjectForm)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setMinimumSize(QSize(0, 0))
        self.info_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.info_label.setWordWrap(False)

        self.verticalLayout_5.addWidget(self.info_label)

        self.name_line = QFrame(NewProjectForm)
        self.name_line.setObjectName(u"name_line")
        self.name_line.setFrameShadow(QFrame.Plain)
        self.name_line.setFrameShape(QFrame.HLine)

        self.verticalLayout_5.addWidget(self.name_line)

        self.verticalLayout_2.addLayout(self.verticalLayout_5)

        self.gridLayout = QGridLayout()
#ifndef Q_OS_MAC
        self.gridLayout.setSpacing(-1)
#endif
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(NewProjectForm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMargin(1)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.name_edit = QLineEdit(NewProjectForm)
        self.name_edit.setObjectName(u"name_edit")

        self.gridLayout.addWidget(self.name_edit, 0, 1, 1, 1)

        self.name_preview_label = QLabel(NewProjectForm)
        self.name_preview_label.setObjectName(u"name_preview_label")
        self.name_preview_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.name_preview_label.setMargin(1)
        self.name_preview_label.setIndent(-1)

        self.gridLayout.addWidget(self.name_preview_label, 1, 1, 1, 1)

        self.label_4 = QLabel(NewProjectForm)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_4.setMargin(1)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(NewProjectForm)
        self.label.setObjectName(u"label")

        self.verticalLayout_6.addWidget(self.label)

        self.publishes_line = QFrame(NewProjectForm)
        self.publishes_line.setObjectName(u"publishes_line")
        self.publishes_line.setFrameShadow(QFrame.Plain)
        self.publishes_line.setFrameShape(QFrame.HLine)

        self.verticalLayout_6.addWidget(self.publishes_line)

        self.verticalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.publish_list = PublishListView(NewProjectForm)
        self.publish_list.setObjectName(u"publish_list")
        self.publish_list.setStyleSheet(u"#publish_list {\n"
"background-color: rgb(255, 128, 0);\n"
"}")

        self.verticalLayout_4.addWidget(self.publish_list)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.add_publish_btn = QPushButton(NewProjectForm)
        self.add_publish_btn.setObjectName(u"add_publish_btn")
        self.add_publish_btn.setMinimumSize(QSize(32, 0))

        self.horizontalLayout.addWidget(self.add_publish_btn)

        self.horizontalLayout.setStretch(0, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_4.setStretch(0, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.break_line = QFrame(NewProjectForm)
        self.break_line.setObjectName(u"break_line")
        self.break_line.setFrameShadow(QFrame.Plain)
        self.break_line.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.break_line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(12, 8, 12, 12)
        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.cancel_btn = QPushButton(NewProjectForm)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_3.addWidget(self.cancel_btn)

        self.create_btn = QPushButton(NewProjectForm)
        self.create_btn.setObjectName(u"create_btn")
        self.create_btn.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_3.addWidget(self.create_btn)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(NewProjectForm)
        self.cancel_btn.clicked.connect(NewProjectForm.close)

        self.create_btn.setDefault(True)

        QMetaObject.connectSlotsByName(NewProjectForm)
    # setupUi

    def retranslateUi(self, NewProjectForm):
        NewProjectForm.setWindowTitle(QCoreApplication.translate("NewProjectForm", u"Form", None))
        self.info_label.setText(QCoreApplication.translate("NewProjectForm", u"Please enter a name below to be used as part of the project name", None))
        self.label_2.setText(QCoreApplication.translate("NewProjectForm", u"Name:", None))
        self.name_preview_label.setText("")
        self.label_4.setText(QCoreApplication.translate("NewProjectForm", u"Preview:", None))
        self.label.setText(QCoreApplication.translate("NewProjectForm", u"Add publishes you would like to include in the new project", None))
        self.add_publish_btn.setText(QCoreApplication.translate("NewProjectForm", u"Add Publish...", None))
        self.cancel_btn.setText(QCoreApplication.translate("NewProjectForm", u"Cancel", None))
        self.create_btn.setText(QCoreApplication.translate("NewProjectForm", u"Create Project", None))
    # retranslateUi
