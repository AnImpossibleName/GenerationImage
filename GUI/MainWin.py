# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(906, 746)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.settingArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.settingArea.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingArea.sizePolicy().hasHeightForWidth())
        self.settingArea.setSizePolicy(sizePolicy)
        self.settingArea.setMinimumSize(QtCore.QSize(200, 0))
        self.settingArea.setWidgetResizable(True)
        self.settingArea.setObjectName("settingArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 270, 726))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.Title = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents_3)
        self.Title.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title.sizePolicy().hasHeightForWidth())
        self.Title.setSizePolicy(sizePolicy)
        self.Title.setMaximumSize(QtCore.QSize(16777215, 45))
        self.Title.setObjectName("Title")
        self.verticalLayout_3.addWidget(self.Title)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_3.addItem(spacerItem1)
        self.AccountTitle = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccountTitle.sizePolicy().hasHeightForWidth())
        self.AccountTitle.setSizePolicy(sizePolicy)
        self.AccountTitle.setMinimumSize(QtCore.QSize(0, 0))
        self.AccountTitle.setMaximumSize(QtCore.QSize(16777215, 40))
        self.AccountTitle.setObjectName("AccountTitle")
        self.verticalLayout_3.addWidget(self.AccountTitle, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.AccountName = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccountName.sizePolicy().hasHeightForWidth())
        self.AccountName.setSizePolicy(sizePolicy)
        self.AccountName.setMaximumSize(QtCore.QSize(16777215, 40))
        self.AccountName.setObjectName("AccountName")
        self.verticalLayout_3.addWidget(self.AccountName, 0,
                                        QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_3.addItem(spacerItem2)
        self.KeyTitle = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.KeyTitle.sizePolicy().hasHeightForWidth())
        self.KeyTitle.setSizePolicy(sizePolicy)
        self.KeyTitle.setMaximumSize(QtCore.QSize(16777215, 40))
        self.KeyTitle.setObjectName("KeyTitle")
        self.verticalLayout_3.addWidget(self.KeyTitle)
        self.KeyContent = QtWidgets.QTextEdit(parent=self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.KeyContent.sizePolicy().hasHeightForWidth())
        self.KeyContent.setSizePolicy(sizePolicy)
        self.KeyContent.setMaximumSize(QtCore.QSize(16777215, 150))
        self.KeyContent.setObjectName("KeyContent")
        self.verticalLayout_3.addWidget(self.KeyContent)
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_3.addItem(spacerItem3)
        self.PathTitle = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PathTitle.sizePolicy().hasHeightForWidth())
        self.PathTitle.setSizePolicy(sizePolicy)
        self.PathTitle.setMaximumSize(QtCore.QSize(16777215, 40))
        self.PathTitle.setObjectName("PathTitle")
        self.verticalLayout_3.addWidget(self.PathTitle)
        self.PathContent = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents_3)
        self.PathContent.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.PathContent.setObjectName("PathContent")
        self.verticalLayout_3.addWidget(self.PathContent)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.LogoutButton = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_3)
        self.LogoutButton.setStyleSheet("background-color:rgb(255, 0, 0);\n"
                                        "color:rgb(255, 255, 255)")
        icon_logout = QtGui.QIcon()
        icon_logout.addPixmap(QtGui.QPixmap("./Icon/退出登录.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.LogoutButton.setIcon(icon_logout)
        self.LogoutButton.setObjectName("LogoutButton")
        self.verticalLayout_3.addWidget(self.LogoutButton)
        self.settingArea.setWidget(self.scrollAreaWidgetContents_3)
        self.horizontalLayout.addWidget(self.settingArea)
        self.showButton = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showButton.sizePolicy().hasHeightForWidth())
        self.showButton.setSizePolicy(sizePolicy)
        self.showButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.showButton.setText("")
        icon_show = QtGui.QIcon()
        icon_show.addPixmap(QtGui.QPixmap("Icon/展开.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.icon_show = icon_show
        icon_hide = QtGui.QIcon()
        icon_hide.addPixmap(QtGui.QPixmap("Icon/收回.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.icon_hide = icon_hide
        self.showButton.setIcon(icon_hide)
        self.showButton.setObjectName("showButton")
        self.horizontalLayout.addWidget(self.showButton)
        self.imageShow = QtWidgets.QWidget(parent=self.centralwidget)
        self.imageShow.setObjectName("imageShow")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.imageShow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.imageView = QtWidgets.QGraphicsView(parent=self.imageShow)
        self.imageView.setObjectName("imageView")
        self.verticalLayout.addWidget(self.imageView)
        self.pushButton = QtWidgets.QPushButton(parent=self.imageShow)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton.setStyleSheet("font: 16pt \"Microsoft YaHei UI\";\n"
                                      "background-color:rgb(0, 255, 0)")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addWidget(self.imageShow)
        self.postArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.postArea.sizePolicy().hasHeightForWidth())
        self.postArea.setSizePolicy(sizePolicy)
        self.postArea.setMinimumSize(QtCore.QSize(300, 0))
        self.postArea.setWidgetResizable(True)
        self.postArea.setObjectName("postArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 298, 726))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem5)
        self.promptTitle = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.promptTitle.sizePolicy().hasHeightForWidth())
        self.promptTitle.setSizePolicy(sizePolicy)
        self.promptTitle.setMaximumSize(QtCore.QSize(16777215, 40))
        self.promptTitle.setObjectName("promptTitle")
        self.verticalLayout_2.addWidget(self.promptTitle)
        self.promptEdit = QtWidgets.QTextEdit(parent=self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.promptEdit.sizePolicy().hasHeightForWidth())
        self.promptEdit.setSizePolicy(sizePolicy)
        self.promptEdit.setMaximumSize(QtCore.QSize(16777215, 300))
        self.promptEdit.setObjectName("promptEdit")
        self.verticalLayout_2.addWidget(self.promptEdit)
        spacerItem6 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem6)
        self.negative_promptTitle = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.negative_promptTitle.sizePolicy().hasHeightForWidth())
        self.negative_promptTitle.setSizePolicy(sizePolicy)
        self.negative_promptTitle.setMaximumSize(QtCore.QSize(16777215, 40))
        self.negative_promptTitle.setObjectName("negative_promptTitle")
        self.verticalLayout_2.addWidget(self.negative_promptTitle)
        self.negative_promptEdit = QtWidgets.QTextEdit(parent=self.scrollAreaWidgetContents)
        self.negative_promptEdit.setObjectName("negative_promptEdit")
        self.verticalLayout_2.addWidget(self.negative_promptEdit)
        spacerItem7 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem7)
        self.num_outputsTitle = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_outputsTitle.sizePolicy().hasHeightForWidth())
        self.num_outputsTitle.setSizePolicy(sizePolicy)
        self.num_outputsTitle.setMaximumSize(QtCore.QSize(16777215, 40))
        self.num_outputsTitle.setObjectName("num_outputsTitle")
        self.verticalLayout_2.addWidget(self.num_outputsTitle)
        self.num_outputs = QtWidgets.QSpinBox(parent=self.scrollAreaWidgetContents)
        self.num_outputs.setMinimum(1)
        self.num_outputs.setMaximum(4)
        self.num_outputs.setObjectName("num_outputs")
        self.verticalLayout_2.addWidget(self.num_outputs)
        spacerItem8 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem8)
        self.guidance_scaleTitle = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guidance_scaleTitle.sizePolicy().hasHeightForWidth())
        self.guidance_scaleTitle.setSizePolicy(sizePolicy)
        self.guidance_scaleTitle.setMaximumSize(QtCore.QSize(16777215, 40))
        self.guidance_scaleTitle.setObjectName("guidance_scaleTitle")
        self.verticalLayout_2.addWidget(self.guidance_scaleTitle)
        self.guidance_scale = QtWidgets.QSpinBox(parent=self.scrollAreaWidgetContents)
        self.guidance_scale.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.guidance_scale.setMinimum(1)
        self.guidance_scale.setMaximum(20)
        self.guidance_scale.setObjectName("guidance_scale")
        self.verticalLayout_2.addWidget(self.guidance_scale)
        spacerItem9 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem9)
        self.imagePromptTitle = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagePromptTitle.sizePolicy().hasHeightForWidth())
        self.imagePromptTitle.setSizePolicy(sizePolicy)
        self.imagePromptTitle.setMaximumSize(QtCore.QSize(16777215, 40))
        self.imagePromptTitle.setObjectName("imagePromptTitle")
        self.verticalLayout_2.addWidget(self.imagePromptTitle)
        self.imagePromptPath = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.imagePromptPath.setObjectName("imagePromptPath")
        self.verticalLayout_2.addWidget(self.imagePromptPath)
        self.imagePromptButton = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.imagePromptButton.setObjectName("imagePromptButton")
        self.verticalLayout_2.addWidget(self.imagePromptButton)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem10)
        self.postArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.postArea)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.showButton.clicked.connect(self.sidebarIsShow)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setHtml(_translate("MainWindow",
                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                      "p, li { white-space: pre-wrap; }\n"
                                      "hr { height: 1px; border-width: 0; }\n"
                                      "li.unchecked::marker { content: \"\\2610\"; }\n"
                                      "li.checked::marker { content: \"\\2612\"; }\n"
                                      "</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:11.25pt; font-weight:400; font-style:normal;\">\n"
                                      "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:700;\">应用设置</span></p></body></html>"))
        self.AccountTitle.setHtml(_translate("MainWindow",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "hr { height: 1px; border-width: 0; }\n"
                                             "li.unchecked::marker { content: \"\\2610\"; }\n"
                                             "li.checked::marker { content: \"\\2612\"; }\n"
                                             "</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:11.25pt; font-weight:400; font-style:normal;\">\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700;\">当前登录账号</span></p></body></html>"))
        self.AccountName.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "hr { height: 1px; border-width: 0; }\n"
                                            "li.unchecked::marker { content: \"\\2610\"; }\n"
                                            "li.checked::marker { content: \"\\2612\"; }\n"
                                            "</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:11.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">显示昵称</span></p></body></html>"))
        self.KeyTitle.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "hr { height: 1px; border-width: 0; }\n"
                                         "li.unchecked::marker { content: \"\\2610\"; }\n"
                                         "li.checked::marker { content: \"\\2612\"; }\n"
                                         "</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:11.25pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700;\">API密钥</span></p></body></html>"))
        self.KeyContent.setPlaceholderText(_translate("MainWindow", "输入用户密钥"))
        self.PathTitle.setHtml(_translate("MainWindow",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "hr { height: 1px; border-width: 0; }\n"
                                          "li.unchecked::marker { content: \"\\2610\"; }\n"
                                          "li.checked::marker { content: \"\\2612\"; }\n"
                                          "</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:11.25pt; font-weight:400; font-style:normal;\">\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700;\">存储路径</span></p></body></html>"))
        self.PathContent.setPlaceholderText(_translate("MainWindow", "显示用户存储路径"))
        self.LogoutButton.setText(_translate("MainWindow", "退出登录"))
        self.pushButton.setText(_translate("MainWindow", "开始生成"))
        self.promptTitle.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "hr { height: 1px; border-width: 0; }\n"
                                            "li.unchecked::marker { content: \"\\2610\"; }\n"
                                            "li.checked::marker { content: \"\\2612\"; }\n"
                                            "</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:11.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">英文提示词</span><span style=\" font-size:18pt; font-weight:700; color:#818181;\">（必填）</span></p></body></html>"))
        self.promptEdit.setPlaceholderText(_translate("MainWindow", "请输入英文提示词，暂不支持中文"))
        self.negative_promptTitle.setHtml(_translate("MainWindow",
                                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "hr { height: 1px; border-width: 0; }\n"
                                                     "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                     "li.checked::marker { content: \"\\2612\"; }\n"
                                                     "</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:11.25pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">逆提示词</span></p></body></html>"))
        self.negative_promptEdit.setPlaceholderText(_translate("MainWindow", "请输入逆提示词（不想生成出的内容）"))
        self.num_outputsTitle.setHtml(_translate("MainWindow",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "hr { height: 1px; border-width: 0; }\n"
                                                 "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                 "li.checked::marker { content: \"\\2612\"; }\n"
                                                 "</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:11.25pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">生成数量</span></p></body></html>"))
        self.guidance_scaleTitle.setHtml(_translate("MainWindow",
                                                    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                    "p, li { white-space: pre-wrap; }\n"
                                                    "hr { height: 1px; border-width: 0; }\n"
                                                    "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                    "li.checked::marker { content: \"\\2612\"; }\n"
                                                    "</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:11.25pt; font-weight:400; font-style:normal;\">\n"
                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">相似度</span><span style=\" font-size:14pt; font-weight:700; color:#818181;\">（越高越接近提示）</span></p></body></html>"))
        self.imagePromptTitle.setHtml(_translate("MainWindow",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "hr { height: 1px; border-width: 0; }\n"
                                                 "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                 "li.checked::marker { content: \"\\2612\"; }\n"
                                                 "</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:11.25pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">提示图</span></p></body></html>"))
        self.imagePromptPath.setPlaceholderText(_translate("MainWindow", "图片路径"))
        self.imagePromptButton.setText(_translate("MainWindow", "选择文件"))

    def sidebarIsShow(self):
        if self.settingArea.isVisible():
            self.settingArea.hide()
            self.showButton.setIcon(self.icon_show)
        else:
            self.settingArea.show()
            self.showButton.setIcon(self.icon_hide)

