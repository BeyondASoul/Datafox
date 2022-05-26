# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loading_screen.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoadingScreen(object):
    def setupUi(self, LoadingScreen):
        LoadingScreen.setObjectName("LoadingScreen")
        LoadingScreen.setWindowModality(QtCore.Qt.WindowModal)
        LoadingScreen.resize(757, 437)
        LoadingScreen.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        LoadingScreen.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(LoadingScreen)
        self.gridLayout.setObjectName("gridLayout")
        self.loading_bar = QtWidgets.QProgressBar(LoadingScreen)
        self.loading_bar.setProperty("value", 0)
        self.loading_bar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.loading_bar.setObjectName("loading_bar")
        self.gridLayout.addWidget(self.loading_bar, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(LoadingScreen)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 1, 1, 1)

        self.retranslateUi(LoadingScreen)
        QtCore.QMetaObject.connectSlotsByName(LoadingScreen)

    def retranslateUi(self, LoadingScreen):
        _translate = QtCore.QCoreApplication.translate
        LoadingScreen.setWindowTitle(_translate("LoadingScreen", "Cargando"))
        self.label.setText(_translate("LoadingScreen", "Cargando el cojunto de datos, esto podría demorar unos segundos..."))