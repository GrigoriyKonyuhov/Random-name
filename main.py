import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint


class Yellow_circles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'UI.ui', self)
        self.pushButton.clicked.connect(self.btn_clicked)
        self.painted = False

    def paintEvent(self, event):
        if self.painted:
            painter = QPainter()
            painter.begin(self)
            painter.setBrush(QColor(255, 255, 0))
            for i in range(7):
                x, y = randint(7, 418), randint(7, 418)
                rad = randint(8, 748)
                painter.drawEllipse(x, y, rad, rad)
            painter.end()

    def btn_clicked(self):
        self.painted = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Yellow_circles()
    ex.show()
    sys.exit(app.exec())
