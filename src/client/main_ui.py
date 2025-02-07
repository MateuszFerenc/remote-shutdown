# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/client/main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 500)
        MainWindow.setMinimumSize(QtCore.QSize(770, 500))
        MainWindow.setMaximumSize(QtCore.QSize(770, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(240, 0, 231, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setScaledContents(False)
        self.label_6.setIndent(-1)
        self.label_6.setObjectName("label_6")
        self.FoundHosts_list = QtWidgets.QListWidget(self.centralwidget)
        self.FoundHosts_list.setGeometry(QtCore.QRect(240, 33, 511, 371))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.FoundHosts_list.setFont(font)
        self.FoundHosts_list.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.FoundHosts_list.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.FoundHosts_list.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.FoundHosts_list.setAlternatingRowColors(True)
        self.FoundHosts_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.FoundHosts_list.setObjectName("FoundHosts_list")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(230, 415, 531, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.TestHosts_button = QtWidgets.QPushButton(self.groupBox)
        self.TestHosts_button.setGeometry(QtCore.QRect(10, 20, 161, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TestHosts_button.sizePolicy().hasHeightForWidth())
        self.TestHosts_button.setSizePolicy(sizePolicy)
        self.TestHosts_button.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.TestHosts_button.setFont(font)
        self.TestHosts_button.setAutoDefault(False)
        self.TestHosts_button.setObjectName("TestHosts_button")
        self.DisableHosts_button = QtWidgets.QPushButton(self.groupBox)
        self.DisableHosts_button.setGeometry(QtCore.QRect(180, 20, 161, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.DisableHosts_button.setFont(font)
        self.DisableHosts_button.setObjectName("DisableHosts_button")
        self.ShutdownHosts_button = QtWidgets.QPushButton(self.groupBox)
        self.ShutdownHosts_button.setGeometry(QtCore.QRect(350, 20, 171, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(13)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ShutdownHosts_button.setFont(font)
        self.ShutdownHosts_button.setObjectName("ShutdownHosts_button")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 263, 211, 201))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.ClearStatus = QtWidgets.QRadioButton(self.groupBox_2)
        self.ClearStatus.setGeometry(QtCore.QRect(10, 178, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ClearStatus.setFont(font)
        self.ClearStatus.setCheckable(True)
        self.ClearStatus.setAutoExclusive(False)
        self.ClearStatus.setObjectName("ClearStatus")
        self.StatusIndicator = QtWidgets.QCheckBox(self.groupBox_2)
        self.StatusIndicator.setEnabled(True)
        self.StatusIndicator.setGeometry(QtCore.QRect(80, 178, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.StatusIndicator.setFont(font)
        self.StatusIndicator.setCheckable(False)
        self.StatusIndicator.setObjectName("StatusIndicator")
        self.StatusInfoBox = QtWidgets.QTextEdit(self.groupBox_2)
        self.StatusInfoBox.setGeometry(QtCore.QRect(10, 20, 191, 151))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.StatusInfoBox.setFont(font)
        self.StatusInfoBox.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.StatusInfoBox.setUndoRedoEnabled(False)
        self.StatusInfoBox.setReadOnly(True)
        self.StatusInfoBox.setOverwriteMode(True)
        self.StatusInfoBox.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.StatusInfoBox.setObjectName("StatusInfoBox")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 153, 221, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.SelectOne_button = QtWidgets.QPushButton(self.groupBox_3)
        self.SelectOne_button.setGeometry(QtCore.QRect(120, 70, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.SelectOne_button.setFont(font)
        self.SelectOne_button.setObjectName("SelectOne_button")
        self.SelectOne_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.SelectOne_checkBox.setEnabled(False)
        self.SelectOne_checkBox.setGeometry(QtCore.QRect(100, 70, 16, 21))
        self.SelectOne_checkBox.setCheckable(False)
        self.SelectOne_checkBox.setObjectName("SelectOne_checkBox")
        self.SelectRange_button = QtWidgets.QPushButton(self.groupBox_3)
        self.SelectRange_button.setGeometry(QtCore.QRect(30, 53, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.SelectRange_button.setFont(font)
        self.SelectRange_button.setObjectName("SelectRange_button")
        self.SelectAll_button = QtWidgets.QPushButton(self.groupBox_3)
        self.SelectAll_button.setGeometry(QtCore.QRect(30, 23, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.SelectAll_button.setFont(font)
        self.SelectAll_button.setObjectName("SelectAll_button")
        self.UnselectAll_button = QtWidgets.QPushButton(self.groupBox_3)
        self.UnselectAll_button.setGeometry(QtCore.QRect(115, 23, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.UnselectAll_button.setFont(font)
        self.UnselectAll_button.setObjectName("UnselectAll_button")
        self.SelectAllActive_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.SelectAllActive_checkBox.setEnabled(False)
        self.SelectAllActive_checkBox.setGeometry(QtCore.QRect(10, 23, 16, 21))
        self.SelectAllActive_checkBox.setText("")
        self.SelectAllActive_checkBox.setCheckable(False)
        self.SelectAllActive_checkBox.setAutoRepeat(False)
        self.SelectAllActive_checkBox.setAutoExclusive(False)
        self.SelectAllActive_checkBox.setObjectName("SelectAllActive_checkBox")
        self.SelectRange_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.SelectRange_checkBox.setEnabled(False)
        self.SelectRange_checkBox.setGeometry(QtCore.QRect(10, 70, 16, 21))
        self.SelectRange_checkBox.setCheckable(False)
        self.SelectRange_checkBox.setObjectName("SelectRange_checkBox")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 3, 221, 151))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.PortEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.PortEdit.setGeometry(QtCore.QRect(130, 47, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.PortEdit.setFont(font)
        self.PortEdit.setAcceptDrops(False)
        self.PortEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PortEdit.setAutoFillBackground(False)
        self.PortEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.PortEdit.setMaxLength(5)
        self.PortEdit.setFrame(True)
        self.PortEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.PortEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PortEdit.setClearButtonEnabled(True)
        self.PortEdit.setObjectName("PortEdit")
        self.getLocalAddr = QtWidgets.QRadioButton(self.groupBox_4)
        self.getLocalAddr.setGeometry(QtCore.QRect(10, 24, 131, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.getLocalAddr.setFont(font)
        self.getLocalAddr.setCheckable(True)
        self.getLocalAddr.setAutoExclusive(False)
        self.getLocalAddr.setObjectName("getLocalAddr")
        self.AddrEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.AddrEdit.setGeometry(QtCore.QRect(10, 47, 115, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.AddrEdit.setFont(font)
        self.AddrEdit.setAcceptDrops(False)
        self.AddrEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AddrEdit.setAutoFillBackground(False)
        self.AddrEdit.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.AddrEdit.setMaxLength(12)
        self.AddrEdit.setFrame(True)
        self.AddrEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.AddrEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.AddrEdit.setClearButtonEnabled(True)
        self.AddrEdit.setObjectName("AddrEdit")
        self.SearchButton = QtWidgets.QPushButton(self.groupBox_4)
        self.SearchButton.setGeometry(QtCore.QRect(9, 70, 203, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.SearchButton.setFont(font)
        self.SearchButton.setFlat(False)
        self.SearchButton.setObjectName("SearchButton")
        self.SelectedHosts_label = QtWidgets.QLabel(self.groupBox_4)
        self.SelectedHosts_label.setGeometry(QtCore.QRect(150, 120, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.SelectedHosts_label.setFont(font)
        self.SelectedHosts_label.setObjectName("SelectedHosts_label")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.FoundHosts_label = QtWidgets.QLabel(self.groupBox_4)
        self.FoundHosts_label.setGeometry(QtCore.QRect(130, 98, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.FoundHosts_label.setFont(font)
        self.FoundHosts_label.setObjectName("FoundHosts_label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(10, 98, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.groupBox_3.raise_()
        self.groupBox.raise_()
        self.groupBox_4.raise_()
        self.groupBox_2.raise_()
        self.label_6.raise_()
        self.FoundHosts_list.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 26))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.action_Language = QtWidgets.QAction(MainWindow)
        self.action_Language.setObjectName("action_Language")
        self.action_Author = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.action_Author.setFont(font)
        self.action_Author.setObjectName("action_Author")
        self.action_Documentation = QtWidgets.QAction(MainWindow)
        self.action_Documentation.setObjectName("action_Documentation")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.action_Exit_2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.action_Exit_2.setFont(font)
        self.action_Exit_2.setObjectName("action_Exit_2")
        self.menu_File.addAction(self.action_Language)
        self.menu_File.addAction(self.action_Exit_2)
        self.menu_Help.addAction(self.action_Author)
        self.menu_Help.addAction(self.action_Documentation)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.getLocalAddr, self.AddrEdit)
        MainWindow.setTabOrder(self.AddrEdit, self.PortEdit)
        MainWindow.setTabOrder(self.PortEdit, self.SearchButton)
        MainWindow.setTabOrder(self.SearchButton, self.SelectAllActive_checkBox)
        MainWindow.setTabOrder(self.SelectAllActive_checkBox, self.SelectAll_button)
        MainWindow.setTabOrder(self.SelectAll_button, self.UnselectAll_button)
        MainWindow.setTabOrder(self.UnselectAll_button, self.SelectRange_checkBox)
        MainWindow.setTabOrder(self.SelectRange_checkBox, self.SelectRange_button)
        MainWindow.setTabOrder(self.SelectRange_button, self.SelectOne_checkBox)
        MainWindow.setTabOrder(self.SelectOne_checkBox, self.SelectOne_button)
        MainWindow.setTabOrder(self.SelectOne_button, self.StatusInfoBox)
        MainWindow.setTabOrder(self.StatusInfoBox, self.ClearStatus)
        MainWindow.setTabOrder(self.ClearStatus, self.StatusIndicator)
        MainWindow.setTabOrder(self.StatusIndicator, self.FoundHosts_list)
        MainWindow.setTabOrder(self.FoundHosts_list, self.TestHosts_button)
        MainWindow.setTabOrder(self.TestHosts_button, self.DisableHosts_button)
        MainWindow.setTabOrder(self.DisableHosts_button, self.ShutdownHosts_button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Remote Shutdown Client"))
        self.label_6.setText(_translate("MainWindow", "Known hosts"))
        self.groupBox.setTitle(_translate("MainWindow", "Actions"))
        self.TestHosts_button.setText(_translate("MainWindow", "Test Connection"))
        self.DisableHosts_button.setText(_translate("MainWindow", "Disable"))
        self.ShutdownHosts_button.setText(_translate("MainWindow", "Shutdown"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Status"))
        self.ClearStatus.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.ClearStatus.setText(_translate("MainWindow", "Clear"))
        self.StatusIndicator.setText(_translate("MainWindow", "Status"))
        self.StatusInfoBox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\',\'Segoe UI Semibold\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Select method"))
        self.SelectOne_button.setText(_translate("MainWindow", "Select one"))
        self.SelectOne_checkBox.setText(_translate("MainWindow", "Select one"))
        self.SelectRange_button.setText(_translate("MainWindow", "Select\n"
"range"))
        self.SelectAll_button.setText(_translate("MainWindow", "Select all"))
        self.UnselectAll_button.setText(_translate("MainWindow", "Unselect all"))
        self.SelectRange_checkBox.setText(_translate("MainWindow", "Select range"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Search IP"))
        self.PortEdit.setText(_translate("MainWindow", "8080"))
        self.getLocalAddr.setText(_translate("MainWindow", "Local network"))
        self.AddrEdit.setText(_translate("MainWindow", "255.255.255"))
        self.SearchButton.setText(_translate("MainWindow", "Search"))
        self.SelectedHosts_label.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Selected hosts:"))
        self.FoundHosts_label.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "Found hosts:"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.action_Language.setText(_translate("MainWindow", "&Language"))
        self.action_Author.setText(_translate("MainWindow", "&Author"))
        self.action_Documentation.setText(_translate("MainWindow", "&Documentation"))
        self.action_Exit.setText(_translate("MainWindow", "&Select port"))
        self.action_Exit_2.setText(_translate("MainWindow", "&Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
