import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.f = False
        self.btn.clicked.connect(self.flag)

    def paintEvent(self, event):
        if self.f:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        self.size = random.randint(5, 300)
        self.coords = [random.randrange(300), random.randrange(300)]
        self.qp.setBrush(QColor(255, 255, 0))
        self.qp.drawEllipse(*self.coords, self.size, self.size)

    def flag(self):
        self.f = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

