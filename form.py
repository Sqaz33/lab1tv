# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1052, 830)
        self.gridLayout = QtWidgets.QGridLayout(Widget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.selectMethod = QtWidgets.QComboBox(Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectMethod.sizePolicy().hasHeightForWidth())
        self.selectMethod.setSizePolicy(sizePolicy)
        self.selectMethod.setObjectName("selectMethod")
        self.selectMethod.addItem("")
        self.selectMethod.addItem("")
        self.selectMethod.addItem("")
        self.selectMethod.addItem("")
        self.selectMethod.setItemText(3, "")
        self.horizontalLayout.addWidget(self.selectMethod)
        self.formula = QtWidgets.QLabel(Widget)
        self.formula.setObjectName("formula")
        self.horizontalLayout.addWidget(self.formula)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.NNLabel = QtWidgets.QLabel(Widget)
        self.NNLabel.setObjectName("NNLabel")
        self.horizontalLayout_4.addWidget(self.NNLabel)
        self.KKLabel = QtWidgets.QLabel(Widget)
        self.KKLabel.setObjectName("KKLabel")
        self.horizontalLayout_4.addWidget(self.KKLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.NN = QtWidgets.QLineEdit(Widget)
        self.NN.setText("")
        self.NN.setObjectName("NN")
        self.horizontalLayout_2.addWidget(self.NN)
        self.KK = QtWidgets.QLineEdit(Widget)
        self.KK.setObjectName("KK")
        self.horizontalLayout_2.addWidget(self.KK)
        self.calculate = QtWidgets.QPushButton(Widget)
        self.calculate.setObjectName("calculate")
        self.horizontalLayout_2.addWidget(self.calculate)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.answer = QtWidgets.QLabel(Widget)
        self.answer.setObjectName("answer")
        self.verticalLayout.addWidget(self.answer)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.selectMethod.setItemText(0, _translate("Widget", "Количество сочетаний без повторений"))
        self.selectMethod.setItemText(1, _translate("Widget", "Количество размещений с повторениями "))
        self.selectMethod.setItemText(2, _translate("Widget", "Количество перестановок с повторениями "))
        self.selectMethod.setItemText(3, _translate("Widget", "Задача №3 "))
        self.formula.setText(_translate("Widget", "TextLabel"))
        self.NNLabel.setText(_translate("Widget", "TextLabel"))
        self.KKLabel.setText(_translate("Widget", "TextLabel"))
        self.calculate.setText(_translate("Widget", "Вычислить"))
        self.answer.setText(_translate("Widget", "TextLabel"))
