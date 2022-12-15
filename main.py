import sys
import random
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Окружности')
        self.allow = False
        self.X = range(30, 730)
        self.Y = range(30, 670)
        self.R = range(10, 250)
        self.col = range(256)

        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        if self.allow:
            self.allow = False

            qp = QPainter()
            qp.begin(self)
            pen = QPen()
            pen.setWidth(3)

            for i in range(random.choice(range(3, 15))):
                pen.setColor(QColor(random.choice(self.col), random.choice(self.col), random.choice(self.col)))
                qp.setPen(pen)
                r = random.choice(self.R)
                qp.drawEllipse(random.choice(self.X), random.choice(self.Y), r, r)

            qp.end()

    def run(self):
        self.allow = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())