# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/client/./main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 550)
        MainWindow.setMinimumSize(QtCore.QSize(760, 550))
        MainWindow.setMaximumSize(QtCore.QSize(760, 550))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 131, 17))
        font = QtGui.QFont()
        font.setFamily("SquareSlab711 Bd BT")
        font.setPointSize(11)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 60, 91, 17))
        font = QtGui.QFont()
        font.setFamily("SquareSlab711 Bd BT")
        font.setPointSize(11)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("SquareSlab711 Bd BT")
        font.setPointSize(17)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 91, 16))
        font = QtGui.QFont()
        font.setFamily("SquareSlab711 Bd BT")
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 111, 16))
        font = QtGui.QFont()
        font.setFamily("SquareSlab711 Bd BT")
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 110, 61, 16))
        font = QtGui.QFont()
        font.setFamily("SquareSlab711 Bd BT")
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 130, 61, 16))
        font = QtGui.QFont()
        font.setFamily("SquareSlab711 Bd BT")
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(230, 5, 231, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SquareSlab711 Bd BT")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setScaledContents(False)
        self.label_6.setIndent(-1)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 80, 151, 23))
        font = QtGui.QFont()
        font.setFamily("SquareSlab711 Bd BT")
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(230, 470, 511, 23))
        font = QtGui.QFont()
        font.setFamily("SquareSlab711 Bd BT")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(230, 40, 511, 371))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 430, 161, 23))
        font = QtGui.QFont()
        font.setFamily("SquareSlab711 Bd BT")
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 430, 161, 23))
        font = QtGui.QFont()
        font.setFamily("SquareSlab711 Bd BT")
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(570, 430, 171, 23))
        font = QtGui.QFont()
        font.setFamily("SquareSlab711 Bd BT")
        font.setPointSize(13)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(130, 460, 91, 41))
        font = QtGui.QFont()
        font.setFamily("SquareSlab711 Bd BT")
        font.setPointSize(17)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 280, 111, 16))
        font = QtGui.QFont()
        font.setFamily("SquareSlab711 Bd BT")
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 300, 191, 151))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 150, 151, 31))
        font = QtGui.QFont()
        font.setFamily("SquareSlab711 Bd BT")
        font.setPointSize(17)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 180, 81, 23))
        font = QtGui.QFont()
        font.setFamily("SquareSlab711 Bd BT")
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(125, 180, 101, 23))
        font = QtGui.QFont()
        font.setFamily("SquareSlab711 Bd BT")
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 180, 16, 21))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(40, 210, 105, 23))
        font = QtGui.QFont()
        font.setFamily("SquareSlab711 Bd BT")
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 210, 16, 21))
        self.checkBox_2.setObjectName("checkBox_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(40, 240, 91, 23))
        font = QtGui.QFont()
        font.setFamily("SquareSlab711 Bd BT")
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 240, 16, 21))
        self.checkBox_3.setObjectName("checkBox_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 26))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Language = QtWidgets.QAction(MainWindow)
        self.action_Language.setObjectName("action_Language")
        self.action_Author = QtWidgets.QAction(MainWindow)
        self.action_Author.setObjectName("action_Author")
        self.action_Documentation = QtWidgets.QAction(MainWindow)
        self.action_Documentation.setObjectName("action_Documentation")
        self.menu_File.addAction(self.action_Language)
        self.menu_Help.addAction(self.action_Author)
        self.menu_Help.addAction(self.action_Documentation)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Remote Shutdown Client"))
        self.radioButton.setText(_translate("MainWindow", "Local network"))
        self.radioButton_2.setText(_translate("MainWindow", "IP range"))
        self.label.setText(_translate("MainWindow", "Search method:"))
        self.label_2.setText(_translate("MainWindow", "Found hosts:"))
        self.label_3.setText(_translate("MainWindow", "Selected hosts:"))
        self.label_4.setText(_translate("MainWindow", "hosts"))
        self.label_5.setText(_translate("MainWindow", "selected"))
        self.label_6.setText(_translate("MainWindow", "Known hosts:"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.pushButton_2.setText(_translate("MainWindow", "Test"))
        self.pushButton_3.setText(_translate("MainWindow", "Disable"))
        self.pushButton_4.setText(_translate("MainWindow", "Shutdown"))
        self.label_7.setText(_translate("MainWindow", "Progress:"))
        self.label_8.setText(_translate("MainWindow", "Info:"))
        self.label_9.setText(_translate("MainWindow", "Select method:"))
        self.pushButton_5.setText(_translate("MainWindow", "Select all"))
        self.pushButton_6.setText(_translate("MainWindow", "Unselect all"))
        self.pushButton_7.setText(_translate("MainWindow", "Select range"))
        self.checkBox_2.setText(_translate("MainWindow", "Select range"))
        self.pushButton_8.setText(_translate("MainWindow", "Select one"))
        self.checkBox_3.setText(_translate("MainWindow", "Select one"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.action_Language.setText(_translate("MainWindow", "&Language"))
        self.action_Author.setText(_translate("MainWindow", "&Author"))
        self.action_Documentation.setText(_translate("MainWindow", "&Documentation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
