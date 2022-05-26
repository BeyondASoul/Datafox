# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Prediction.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PredictionWidget(object):
    def setupUi(self, PredictionWidget):
        PredictionWidget.setObjectName("PredictionWidget")
        PredictionWidget.resize(827, 328)
        self.gridLayout = QtWidgets.QGridLayout(PredictionWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scroll = QtWidgets.QScrollArea(PredictionWidget)
        self.scroll.setWidgetResizable(True)
        self.scroll.setObjectName("scroll")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 825, 326))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 3, 1, 1, 1)
        self.btn_conf = QtWidgets.QCommandLinkButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_conf.sizePolicy().hasHeightForWidth())
        self.btn_conf.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_conf.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/arrow_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_conf.setIcon(icon)
        self.btn_conf.setObjectName("btn_conf")
        self.gridLayout_2.addWidget(self.btn_conf, 0, 1, 1, 1)
        self.lab_variable = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_variable.sizePolicy().hasHeightForWidth())
        self.lab_variable.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lab_variable.setFont(font)
        self.lab_variable.setObjectName("lab_variable")
        self.gridLayout_2.addWidget(self.lab_variable, 9, 1, 1, 1, QtCore.Qt.AlignRight)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 8, 1, 1, 1)
        self.entradas_grid = QtWidgets.QGridLayout()
        self.entradas_grid.setObjectName("entradas_grid")
        self.gridLayout_2.addLayout(self.entradas_grid, 7, 1, 1, 2)
        self.btn_prediction = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn_prediction.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_prediction.setFlat(True)
        self.btn_prediction.setObjectName("btn_prediction")
        self.gridLayout_2.addWidget(self.btn_prediction, 10, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 4, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lab_resultado = QtWidgets.QLabel(self.frame)
        self.lab_resultado.setTextFormat(QtCore.Qt.AutoText)
        self.lab_resultado.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_resultado.setObjectName("lab_resultado")
        self.gridLayout_3.addWidget(self.lab_resultado, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.frame, 9, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 11, 2, 1, 1)
        self.scroll.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scroll, 0, 0, 1, 1)

        self.retranslateUi(PredictionWidget)
        QtCore.QMetaObject.connectSlotsByName(PredictionWidget)

    def retranslateUi(self, PredictionWidget):
        _translate = QtCore.QCoreApplication.translate
        PredictionWidget.setWindowTitle(_translate("PredictionWidget", "Form"))
        self.label_3.setText(_translate("PredictionWidget", "En esta pantalla, puedes probar la predicción de resultados con el modelo generado anteriormente."))
        self.label_2.setText(_translate("PredictionWidget", "Predicción de un resultado"))
        self.label.setText(_translate("PredictionWidget", "Inserta los siguientes valores, posteriormente haz cick en \"Predecir\"."))
        self.btn_conf.setText(_translate("PredictionWidget", "Regresar"))
        self.lab_variable.setText(_translate("PredictionWidget", "Resultado:"))
        self.btn_prediction.setText(_translate("PredictionWidget", "Predecir"))
        self.lab_resultado.setText(_translate("PredictionWidget", "-"))


from res import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PredictionWidget = QtWidgets.QWidget()
    ui = Ui_PredictionWidget()
    ui.setupUi(PredictionWidget)
    PredictionWidget.show()
    sys.exit(app.exec_())
