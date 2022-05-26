# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VisualEvaluation.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VisualEvaluation(object):
    def setupUi(self, VisualEvaluation):
        VisualEvaluation.setObjectName("VisualEvaluation")
        VisualEvaluation.resize(640, 480)
        self.gridLayout = QtWidgets.QGridLayout(VisualEvaluation)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(VisualEvaluation)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 638, 478))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scroll_grid = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.scroll_grid.setContentsMargins(5, 5, 5, 5)
        self.scroll_grid.setObjectName("scroll_grid")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.eje_x_box = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.eje_x_box.setObjectName("eje_x_box")
        self.verticalLayout.addWidget(self.eje_x_box)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.eje_y_box = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.eje_y_box.setObjectName("eje_y_box")
        self.verticalLayout_2.addWidget(self.eje_y_box)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.dependiente_box = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.dependiente_box.setObjectName("dependiente_box")
        self.verticalLayout_4.addWidget(self.dependiente_box)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.scroll_grid.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.scroll_grid.addItem(spacerItem, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(VisualEvaluation)
        QtCore.QMetaObject.connectSlotsByName(VisualEvaluation)

    def retranslateUi(self, VisualEvaluation):
        _translate = QtCore.QCoreApplication.translate
        VisualEvaluation.setWindowTitle(_translate("VisualEvaluation", "Form"))
        self.label.setText(_translate("VisualEvaluation", "Variable X-Axis"))
        self.label_2.setText(_translate("VisualEvaluation", "Variable Y-Axis"))
        self.label_3.setText(_translate("VisualEvaluation", "Variable dependiente"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VisualEvaluation = QtWidgets.QWidget()
    ui = Ui_VisualEvaluation()
    ui.setupUi(VisualEvaluation)
    VisualEvaluation.show()
    sys.exit(app.exec_())
