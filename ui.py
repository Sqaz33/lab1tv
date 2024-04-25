import PyQt5.QtGui

import combinatorics
from form import *
import sys
import probability


class UI:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.Widget = QtWidgets.QWidget()
        self.ui = Ui_Widget()
        self.ui.setupUi(self.Widget)
        self.comb = combinatorics.Combinatorics()
        self.probab = probability.Probability()
        self.inpts = [
            "Введите число n, чило должно быть больше 0",
            "Введите число k, число должно быть больше 0, но меньше n",
            "Введите число n, чило должно быть больше 0",
            "Введите число k, число должно быть больше 0",
            "Введите n объектов n-ых типов через запятую",
            "Введите число каналов n",
            "Введите число телеграмм m, m > n"
        ]
        self.taskTxt = ("Задача: В отделение связи поступило m телеграмм, которые случайным образом "
                        "распределяются по n каналам связи (n>m). "
                        "Найти вероятность события А – на каждый канал придется "
                        "не больше одной телеграммы"
                        )
        self.answerTxt = "Здесь будет выводится ответ"
        # ---------коннекты----------
        self.ui.selectMethod.currentIndexChanged.connect(self.change_method)
        self.change_method()
        self.ui.calculate.clicked.connect(self.calculate)

    def run(self):
        self.Widget.show()
        sys.exit(self.app.exec_())

    def change_method(self):
        formulas = ["cnk.png", "ank.png", "p.png", "P(A).png"]
        pixMap = QtGui.QPixmap()
        pixMap.load(f"formulas/{formulas[self.ui.selectMethod.currentIndex()]}")
        self.ui.formula.setPixmap(pixMap)
        self.ui.answer.setText(self.answerTxt)

        self.ui.KK.clear()
        self.ui.NN.clear()

        method_index = self.ui.selectMethod.currentIndex()

        self.ui.KK.setVisible(True)
        self.ui.KKLabel.setVisible(True)
        if self.ui.selectMethod.currentIndex() < 2:
            self.ui.NNLabel.setText(self.inpts[method_index * 2])
            self.ui.KKLabel.setText(self.inpts[method_index * 2 + 1])
        elif method_index == 2:
            self.ui.KK.setVisible(False)
            self.ui.KKLabel.setVisible(False)
            self.ui.NNLabel.setText(self.inpts[4])
        else:
            self.ui.answer.setText(f'{self.taskTxt}\n{self.answerTxt}')
            self.ui.NNLabel.setText(self.inpts[5])
            self.ui.KKLabel.setText(self.inpts[6])

    def calculate(self):
        n_txt = self.ui.NN.text().replace(' ', '')
        k_txt = self.ui.KK.text().replace(' ', '')

        n = 0 if (not n_txt.isdigit()) or len(n_txt) == 0 else int(n_txt)
        k = 0 if (not k_txt.isdigit()) or len(k_txt) == 0 else int(k_txt)

        method_index = self.ui.selectMethod.currentIndex()

        if method_index < 2 or method_index == 3:
            if n <= 0:
                self.ui.answer.setText("Ошибка: n <= 0")
                return
            elif k <= 0:
                self.ui.answer.setText(f"Ошибка: {'k' if method_index < 2 else 'm'} <= 0")
                return
            elif k > n and (method_index == 0 or method_index == 3):
                self.ui.answer.setText(f"Ошибка: {'k' if method_index < 2 else 'm'} > n")
                return
        elif (len(n_txt) == 0 or any(a != ',' and not a.isdigit() for a in n_txt)
              and method_index == 2):
            self.ui.answer.setText("Ошибка: неверный ввод n-ых типов")
            return

        answer = ""
        if method_index == 0:
            answer = str(self.comb.combinations(n, k))
        elif method_index == 1:
            answer = str(self.comb.partial_permut_rep(n, k))
        elif method_index == 2:
            counts = [int(i) for i in n_txt.split(',')]
            answer = str(self.comb.permutation_rep(counts))
        else:
            answer = f'{self.taskTxt}\nОтвет: {self.probab.calculate(n, k)}'

        self.ui.answer.setText(answer)
