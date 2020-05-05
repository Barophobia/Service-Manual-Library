import sys
import qdarkstyle
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QPushButton, QToolTip, QMessageBox, QLabel, QMenu
import webbrowser

#HP WINDOWS
class Hpmain(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HP")
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        
        self.pushButton = QPushButton("Back", self)
        self.pushButton.move(300, 450)
        self.pushButton.setToolTip("<h3>Go back a page</h3>")
        self.pushButton.clicked.connect(self.back)

        self.label = QLabel('Different generations of a product are under the overall models',self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.move(175,50)
        self.label.adjustSize()

        self.pushButton = QPushButton("Laptops", self)
        self.pushButton.move(375, 200)
        self.pushButton.setToolTip("<h3>HP Laptops</h3>")
        self.pushButton.clicked.connect(self.hplap)

        self.hpmain()

    def hpmain(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def back(self):
        self.w = Window()
        self.w.show()
        self.hide()

    def hplap(self):
        self.w = Hplap()
        self.w.show()
        self.hide()

class Hplap(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HP Laptop Docs")
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.pushButton = QPushButton("250", self)
        self.pushButton.move(375, 200)
        self.pushButton.setToolTip("<h3>HP 250 Notebook PC</h3>")
        self.pushButton.clicked.connect(self.hp250)
        
        self.pushButton = QPushButton("Back", self)
        self.pushButton.move(300, 450)
        self.pushButton.setToolTip("<h3>Go back a page</h3>")
        self.pushButton.clicked.connect(self.back)

        self.hplap()

    def hplap(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def back(self):
        self.w = Hpmain()
        self.w.show()
        self.hide()

    def hp250(self):
        self.w = Hp250()
        self.w.show()
        self.hide()


class Hp250(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HP 250 Docs")
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500


        self.pushButton = QPushButton("250 G1 HMM", self)
        self.pushButton.move(300, 50)
        self.pushButton.setToolTip("<h3>250 G1 Hardware Maintenance Manual</h3>")
        self.pushButton.clicked.connect(self.hp250g1hmm)

        self.pushButton = QPushButton("250 G2 HMM", self)
        self.pushButton.move(300, 100)
        self.pushButton.setToolTip("<h3>250 G2 Hardware Maintenance Manual</h3>")
        self.pushButton.clicked.connect(self.hp250g2hmm)

        self.pushButton = QPushButton("250 G3 HMM", self)
        self.pushButton.move(300, 150)
        self.pushButton.setToolTip("<h3>250 G3 Hardware Maintenance Manual</h3>")
        self.pushButton.clicked.connect(self.hp250g3hmm)

        self.pushButton = QPushButton("250 G4 HMM", self)
        self.pushButton.move(300, 200)
        self.pushButton.setToolTip("<h3>250 G4 Hardware Maintenance Manual</h3>")
        self.pushButton.clicked.connect(self.hp250g4hmm)

        self.pushButton = QPushButton("250 G5 HMM", self)
        self.pushButton.move(300, 250)
        self.pushButton.setToolTip("<h3>250 G5 Hardware Maintenance Manual</h3>")
        self.pushButton.clicked.connect(self.hp250g5hmm)

        self.pushButton = QPushButton("250 G6 HMM", self)
        self.pushButton.move(300, 300)
        self.pushButton.setToolTip("<h3>250 G6 Hardware Maintenance Manual</h3>")
        self.pushButton.clicked.connect(self.hp250g6hmm)
        
        self.pushButton = QPushButton("250 G7 HMM", self)
        self.pushButton.move(300, 350)
        self.pushButton.setToolTip("<h3>250 G7 Hardware Maintenance Manual</h3>")
        self.pushButton.clicked.connect(self.hp250g7hmm)


        self.pushButton = QPushButton("Back", self)
        self.pushButton.move(300, 450)
        self.pushButton.setToolTip("<h3>Go back a page</h3>")
        self.pushButton.clicked.connect(self.back)

        self.hp250()

    def hp250g1hmm(self):
        webbrowser.open_new(r'.\Docs\HP\Laptops\250\250g1_hmm.pdf')

    def hp250g2hmm(self):
        webbrowser.open_new(r'.\Docs\HP\Laptops\250\250g2_hmm.pdf')

    def hp250g3hmm(self):
        webbrowser.open_new(r'.\Docs\HP\Laptops\250\250g3_hmm.pdf')

    def hp250g4hmm(self):
        webbrowser.open_new(r'.\Docs\HP\Laptops\250\250g4_hmm.pdf')

    def hp250g5hmm(self):
        webbrowser.open_new(r'.\Docs\HP\Laptops\250\250g5_hmm.pdf')

    def hp250g6hmm(self):
        webbrowser.open_new(r'.\Docs\HP\Laptops\250\250g6_hmm.pdf')
    
    def hp250g7hmm(self):
        webbrowser.open_new(r'.\Docs\HP\Laptops\250\250g7_hmm.pdf')

    def back(self):
        self.w = Hplap()
        self.w.show()
        self.hide()

    def hp250(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
        self.hide()

#LENOVO DESIGNS
class Lenovomain(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lenovo")
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.pushButton = QPushButton("Laptop", self)
        self.pushButton.move(375, 200)
        self.pushButton.setToolTip("<h3>Lenovo Laptop Docs</h3>")
        self.pushButton.clicked.connect(self.lenovolap)

        self.pushButton = QPushButton("Back", self)
        self.pushButton.move(300, 450)
        self.pushButton.setToolTip("<h3>Go back a page</h3>")
        self.pushButton.clicked.connect(self.back)

        self.lenovomain()

    def lenovomain(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def back(self):
        self.w = Window()
        self.w.show()
        self.hide()

    def lenovolap(self):
        self.w = Lenovolap()
        self.w.show()
        self.hide()


class Lenovolap(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lenovo Laptop Docs")
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        
        self.pushButton = QPushButton("T450", self)
        self.pushButton.move(150, 100)
        self.pushButton.setToolTip("<h3>T450</h3>")
        self.pushButton.clicked.connect(self.lenovot450)

        self.pushButton = QPushButton("T460", self)
        self.pushButton.move(250, 100)
        self.pushButton.setToolTip("<h3>T460</h3>")
        self.pushButton.clicked.connect(self.lenovot460)

        self.pushButton = QPushButton("T470", self)
        self.pushButton.move(350, 100)
        self.pushButton.setToolTip("<h3>T470</h3>")
        self.pushButton.clicked.connect(self.lenovot470)

        self.pushButton = QPushButton("T480", self)
        self.pushButton.move(450, 100)
        self.pushButton.setToolTip("<h3>T480</h3>")
        self.pushButton.clicked.connect(self.lenovot480)
        
        self.pushButton = QPushButton("Back", self)
        self.pushButton.move(300, 450)
        self.pushButton.setToolTip("<h3>Go back a page</h3>")
        self.pushButton.clicked.connect(self.back)

        self.lenovolap()

    def lenovolap(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def back(self):
        self.w = Lenovomain()
        self.w.show()
        self.hide()

    def lenovot480(self):
        self.w = Lenovot480()
        self.w.show()
        self.hide()

    def lenovot470(self):
        self.w = Lenovot470()
        self.w.show()
        self.hide()

    def lenovot460(self):
        self.w = Lenovot460()
        self.w.show()
        self.hide()

    def lenovot450(self):
        self.w = Lenovot450()
        self.w.show()
        self.hide()

class Lenovot450(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lenovo T450 Docs")
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.pushButton = QPushButton("Hardware Manual", self)
        self.pushButton.move(375, 200)
        self.pushButton.setToolTip("<h3>Hardware Maintenance Manual</h3>")
        self.pushButton.clicked.connect(self.t450hmm)

        self.pushButton = QPushButton("Back", self)
        self.pushButton.move(300, 450)
        self.pushButton.setToolTip("<h3>Go back a page</h3>")
        self.pushButton.clicked.connect(self.back)

        self.lenovot450()

    def t450hmm(self):
        webbrowser.open_new(r'.\Docs\Lenovo\Laptops\T450\t450_hmm.pdf')

    def back(self):
        self.w = Lenovolap()
        self.w.show()
        self.hide()

    def lenovot450(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
        self.hide()


class Lenovot460(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lenovo T460 Docs")
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.pushButton = QPushButton("Hardware Manual", self)
        self.pushButton.move(375, 200)
        self.pushButton.setToolTip("<h3>Hardware Maintenance Manual</h3>")
        self.pushButton.clicked.connect(self.t460hmm)

        self.pushButton = QPushButton("Back", self)
        self.pushButton.move(300, 450)
        self.pushButton.setToolTip("<h3>Go back a page</h3>")
        self.pushButton.clicked.connect(self.back)

        self.lenovot460()

    def t460hmm(self):
        webbrowser.open_new(r'.\Docs\Lenovo\Laptops\T460\t460_hmm.pdf')

    def back(self):
        self.w = Lenovolap()
        self.w.show()
        self.hide()

    def lenovot460(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
        self.hide()

class Lenovot470(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lenovo T470 Docs")
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.pushButton = QPushButton("Hardware Manual", self)
        self.pushButton.move(375, 200)
        self.pushButton.setToolTip("<h3>Hardware Maintenance Manual</h3>")
        self.pushButton.clicked.connect(self.t470hmm)

        self.pushButton = QPushButton("Back", self)
        self.pushButton.move(300, 450)
        self.pushButton.setToolTip("<h3>Go back a page</h3>")
        self.pushButton.clicked.connect(self.back)

        self.lenovot470()

    def t470hmm(self):
        webbrowser.open_new(r'.\Docs\Lenovo\Laptops\T470\t470_hmm.pdf')

    def back(self):
        self.w = Lenovolap()
        self.w.show()
        self.hide()

    def lenovot470(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
        self.hide()

class Lenovot480(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lenovo T480 Docs")
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.pushButton = QPushButton("Hardware Manual", self)
        self.pushButton.move(375, 200)
        self.pushButton.setToolTip("<h3>Hardware Maintenance Manual</h3>")
        self.pushButton.clicked.connect(self.t480hmm)

        self.pushButton = QPushButton("Back", self)
        self.pushButton.move(300, 450)
        self.pushButton.setToolTip("<h3>Go back a page</h3>")
        self.pushButton.clicked.connect(self.back)

        self.lenovot480()

    def t480hmm(self):
        webbrowser.open_new(r'.\Docs\Lenovo\Laptops\T480\t480_hmm.pdf')

    def back(self):
        self.w = Lenovolap()
        self.w.show()
        self.hide()

    def lenovot480(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
        self.hide()

#FIRST WINDOW
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Service Manual Library"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.pushButton = QPushButton("HP", self)
        self.pushButton.move(205, 200)
        self.pushButton.setToolTip("<h3>HP Docs</h3>")
        self.pushButton.clicked.connect(self.hpmain)

        self.pushButton = QPushButton("Lenovo", self)
        self.pushButton.move(405, 200)
        self.pushButton.setToolTip("<h3>Lenovo Docs</h3>")
        self.pushButton.clicked.connect(self.lenovomain)

        self.pushButton = QPushButton("Exit", self)
        self.pushButton.move(300, 440)
        self.pushButton.setToolTip("<h3>Lenovo Docs</h3>")
        self.pushButton.clicked.connect(self.mainexit)

        self.statusBar().showMessage('V0.1, Created by George Rose')

        self.main_window()

    def main_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def hpmain(self):
        self.w = Hpmain()
        self.w.show()
        self.hide()

    def lenovomain(self):
        self.w = Lenovomain()
        self.w.show()
        self.hide()

    def mainexit(self):
        sys.exit()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = Window()
    sys.exit(app.exec())