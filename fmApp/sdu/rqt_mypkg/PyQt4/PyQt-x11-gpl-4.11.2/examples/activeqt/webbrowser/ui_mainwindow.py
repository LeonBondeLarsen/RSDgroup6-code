# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Mar 20 11:28:33 2013
#      by: PyQt4 UI code generator snapshot-4.10.1-90522b46ebd0
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(812, 605)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.hboxlayout = QtGui.QHBoxLayout(self.centralWidget)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.Frame3 = QtGui.QFrame(self.centralWidget)
        self.Frame3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.Frame3.setFrameShadow(QtGui.QFrame.Sunken)
        self.Frame3.setObjectName(_fromUtf8("Frame3"))
        self.vboxlayout = QtGui.QVBoxLayout(self.Frame3)
        self.vboxlayout.setMargin(1)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.WebBrowser = QAxContainer.QAxWidget(self.Frame3)
        self.WebBrowser.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.WebBrowser.setControl(_fromUtf8("{8856F961-340A-11D0-A96B-00C04FD705A2}"))
        self.WebBrowser.setObjectName(_fromUtf8("WebBrowser"))
        self.vboxlayout.addWidget(self.WebBrowser)
        self.hboxlayout.addWidget(self.Frame3)
        MainWindow.setCentralWidget(self.centralWidget)
        self.tbNavigate = QtGui.QToolBar(MainWindow)
        self.tbNavigate.setOrientation(QtCore.Qt.Horizontal)
        self.tbNavigate.setObjectName(_fromUtf8("tbNavigate"))
        MainWindow.addToolBar(4, self.tbNavigate)
        self.tbAddress = QtGui.QToolBar(MainWindow)
        self.tbAddress.setOrientation(QtCore.Qt.Horizontal)
        self.tbAddress.setObjectName(_fromUtf8("tbAddress"))
        MainWindow.addToolBar(4, self.tbAddress)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.PopupMenu = QtGui.QMenu(self.menubar)
        self.PopupMenu.setObjectName(_fromUtf8("PopupMenu"))
        self.FileNewGroup_2 = QtGui.QMenu(self.PopupMenu)
        self.FileNewGroup_2.setObjectName(_fromUtf8("FileNewGroup_2"))
        self.unnamed = QtGui.QMenu(self.menubar)
        self.unnamed.setObjectName(_fromUtf8("unnamed"))
        MainWindow.setMenuBar(self.menubar)
        self.actionGo = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addFile(_fromUtf8(":/icons/image0.xpm"))
        self.actionGo.setIcon(icon)
        self.actionGo.setObjectName(_fromUtf8("actionGo"))
        self.actionBack = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addFile(_fromUtf8(":/icons/image1.xpm"))
        self.actionBack.setIcon(icon1)
        self.actionBack.setObjectName(_fromUtf8("actionBack"))
        self.actionForward = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addFile(_fromUtf8(":/icons/image2.xpm"))
        self.actionForward.setIcon(icon2)
        self.actionForward.setObjectName(_fromUtf8("actionForward"))
        self.actionStop = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addFile(_fromUtf8(":/icons/image3.xpm"))
        self.actionStop.setIcon(icon3)
        self.actionStop.setObjectName(_fromUtf8("actionStop"))
        self.actionRefresh = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addFile(_fromUtf8(":/icons/image4.xpm"))
        self.actionRefresh.setIcon(icon4)
        self.actionRefresh.setObjectName(_fromUtf8("actionRefresh"))
        self.actionHome = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addFile(_fromUtf8(":/icons/image5.xpm"))
        self.actionHome.setIcon(icon5)
        self.actionHome.setObjectName(_fromUtf8("actionHome"))
        self.actionFileClose = QtGui.QAction(MainWindow)
        self.actionFileClose.setObjectName(_fromUtf8("actionFileClose"))
        self.actionSearch = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addFile(_fromUtf8(":/icons/image6.xpm"))
        self.actionSearch.setIcon(icon6)
        self.actionSearch.setObjectName(_fromUtf8("actionSearch"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAboutQt = QtGui.QAction(MainWindow)
        self.actionAboutQt.setObjectName(_fromUtf8("actionAboutQt"))
        self.FileNewGroup = QtGui.QActionGroup(MainWindow)
        self.FileNewGroup.setObjectName(_fromUtf8("FileNewGroup"))
        self.actionNewWindow = QtGui.QAction(self.FileNewGroup)
        self.actionNewWindow.setObjectName(_fromUtf8("actionNewWindow"))
        self.tbNavigate.addAction(self.actionBack)
        self.tbNavigate.addAction(self.actionForward)
        self.tbNavigate.addAction(self.actionStop)
        self.tbNavigate.addAction(self.actionRefresh)
        self.tbNavigate.addAction(self.actionHome)
        self.tbNavigate.addSeparator()
        self.tbNavigate.addAction(self.actionSearch)
        self.tbAddress.addAction(self.actionGo)
        self.FileNewGroup_2.addAction(self.actionNewWindow)
        self.PopupMenu.addAction(self.FileNewGroup_2.menuAction())
        self.PopupMenu.addSeparator()
        self.PopupMenu.addAction(self.actionFileClose)
        self.unnamed.addAction(self.actionAbout)
        self.unnamed.addAction(self.actionAboutQt)
        self.menubar.addAction(self.PopupMenu.menuAction())
        self.menubar.addAction(self.unnamed.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Qt WebBrowser", None))
        self.tbNavigate.setWindowTitle(_translate("MainWindow", "Navigation", None))
        self.tbAddress.setWindowTitle(_translate("MainWindow", "Address", None))
        self.PopupMenu.setTitle(_translate("MainWindow", "&File", None))
        self.FileNewGroup_2.setTitle(_translate("MainWindow", "New", None))
        self.unnamed.setTitle(_translate("MainWindow", "&Help", None))
        self.actionGo.setIconText(_translate("MainWindow", "Go", None))
        self.actionBack.setIconText(_translate("MainWindow", "Back", None))
        self.actionBack.setShortcut(_translate("MainWindow", "Backspace", None))
        self.actionForward.setIconText(_translate("MainWindow", "Forward", None))
        self.actionStop.setIconText(_translate("MainWindow", "Stop", None))
        self.actionRefresh.setIconText(_translate("MainWindow", "Refresh", None))
        self.actionHome.setIconText(_translate("MainWindow", "Home", None))
        self.actionFileClose.setText(_translate("MainWindow", "C&lose", None))
        self.actionFileClose.setIconText(_translate("MainWindow", "Close", None))
        self.actionSearch.setIconText(_translate("MainWindow", "Search", None))
        self.actionAbout.setIconText(_translate("MainWindow", "About", None))
        self.actionAboutQt.setIconText(_translate("MainWindow", "About Qt", None))
        self.actionNewWindow.setIconText(_translate("MainWindow", "Window", None))
        self.actionNewWindow.setShortcut(_translate("MainWindow", "Ctrl+N", None))

from PyQt4 import QAxContainer