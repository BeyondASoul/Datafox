# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'apriori.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AprioriWidget(object):
    def setupUi(self, AprioriWidget):
        AprioriWidget.setObjectName("AprioriWidget")
        AprioriWidget.resize(952, 333)
        self.gridLayout = QtWidgets.QGridLayout(AprioriWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.soporte_in = QtWidgets.QDoubleSpinBox(AprioriWidget)
        self.soporte_in.setDecimals(4)
        self.soporte_in.setMinimum(0.01)
        self.soporte_in.setMaximum(1.0)
        self.soporte_in.setSingleStep(0.1)
        self.soporte_in.setObjectName("soporte_in")
        self.gridLayout.addWidget(self.soporte_in, 7, 0, 1, 1)
        self.lift_in = QtWidgets.QDoubleSpinBox(AprioriWidget)
        self.lift_in.setDecimals(4)
        self.lift_in.setMinimum(1.0)
        self.lift_in.setMaximum(10.0)
        self.lift_in.setSingleStep(0.1)
        self.lift_in.setObjectName("lift_in")
        self.gridLayout.addWidget(self.lift_in, 7, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(AprioriWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.btn_gen_reglas = QtWidgets.QPushButton(AprioriWidget)
        self.btn_gen_reglas.setObjectName("btn_gen_reglas")
        self.gridLayout.addWidget(self.btn_gen_reglas, 7, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(AprioriWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 1, 1, 1)
        self.rule_table = QtWidgets.QTableWidget(AprioriWidget)
        self.rule_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.rule_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.rule_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.rule_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.rule_table.setTabKeyNavigation(False)
        self.rule_table.setProperty("showDropIndicator", False)
        self.rule_table.setDragEnabled(False)
        self.rule_table.setDragDropOverwriteMode(False)
        self.rule_table.setAlternatingRowColors(False)
        self.rule_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.rule_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.rule_table.setRowCount(0)
        self.rule_table.setColumnCount(4)
        self.rule_table.setObjectName("rule_table")
        self.rule_table.horizontalHeader().setSortIndicatorShown(True)
        self.gridLayout.addWidget(self.rule_table, 8, 0, 1, 4, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.confianza_in = QtWidgets.QDoubleSpinBox(AprioriWidget)
        self.confianza_in.setDecimals(4)
        self.confianza_in.setMinimum(0.01)
        self.confianza_in.setMaximum(1.0)
        self.confianza_in.setSingleStep(0.1)
        self.confianza_in.setObjectName("confianza_in")
        self.gridLayout.addWidget(self.confianza_in, 7, 1, 1, 1)
        self.label = QtWidgets.QLabel(AprioriWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(AprioriWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(AprioriWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(AprioriWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(AprioriWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(AprioriWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 1, 1, 1)

        self.retranslateUi(AprioriWidget)
        QtCore.QMetaObject.connectSlotsByName(AprioriWidget)

    def retranslateUi(self, AprioriWidget):
        _translate = QtCore.QCoreApplication.translate
        AprioriWidget.setWindowTitle(_translate("AprioriWidget", "Form"))
        self.label_3.setText(_translate("AprioriWidget", "Soporte"))
        self.btn_gen_reglas.setText(_translate("AprioriWidget", "Buscar"))
        self.label_2.setText(_translate("AprioriWidget", "Confianza"))
        self.rule_table.setSortingEnabled(True)
        self.label.setText(_translate("AprioriWidget", "Lift"))
        self.label_6.setText(_translate("AprioriWidget", "Indica que tan fiable \n"
"es una regla."))
        self.label_4.setText(_translate("AprioriWidget", "Algoritmo A Priori"))
        self.label_7.setText(_translate("AprioriWidget", "Indica el nivel de relaci??n \n"
"(aumento de posibilidad) \n"
"entre el antecedente \n"
"y consecuente de la regla."))
        self.label_5.setText(_translate("AprioriWidget", "Indica cuan importante\n"
" es una regla dentro \n"
"del total de transacciones."))
        self.label_8.setText(_translate("AprioriWidget", "Selecciona las caracteristicas buscadas\n"
"en tus reglas de asociadion."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AprioriWidget = QtWidgets.QWidget()
    ui = Ui_AprioriWidget()
    ui.setupUi(AprioriWidget)
    AprioriWidget.show()
    sys.exit(app.exec_())
