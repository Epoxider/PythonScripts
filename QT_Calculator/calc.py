from PyQt5.QtWidgets import QApplication, QMainWindow
from temp import Ui_MainWindow


class DemoWindow(QMainWindow):
	def __init__(self):
		super(DemoWindow, self).__init__()
		
			
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		
		self.ui.One.clicked.connect(self.print1)
		self.ui.Two.clicked.connect(self.print2)
		self.ui.Three.clicked.connect(self.print3)
		self.ui.Four.clicked.connect(self.print4)
		self.ui.Five.clicked.connect(self.print5)
		self.ui.Six.clicked.connect(self.print6)
		self.ui.Seven.clicked.connect(self.print7)
		self.ui.Eight.clicked.connect(self.print8)
		self.ui.Nine.clicked.connect(self.print9)
		self.ui.Plus.clicked.connect(self.printplus)
		self.ui.Sub.clicked.connect(self.printsub)
		self.ui.Div.clicked.connect(self.printdiv)
		self.ui.Mul.clicked.connect(self.printmul)
		self.ui.Eq.clicked.connect(self.printeq)
		self.ui.Dot.clicked.connect(self.printDot)
		self.ui.DONT.clicked.connect(self.printDONT)
		self.ui.sign.clicked.connect(self.printSign)
		self.ui.AC.clicked.connect(self.printAC)


	def printAC(self):
		self.ui.label.setText('Heres your clear')
	def printDONT(self):
		self.ui.label.setText('Why are you the way that you are')
	def printDot(self):
		self.ui.label.setText('.')
	def printSign(self):
		self.ui.label.setText('\-|')
	def print1(self):
		self.ui.label.setText('1')
	def print2(self):
		self.ui.label.setText('2')
	def print3(self):
		self.ui.label.setText('3')
	def print4(self):
		self.ui.label.setText('4')
	def print5(self):
		self.ui.label.setText('5')
	def print6(self):
		self.ui.label.setText('6')
	def print7(self):
		self.ui.label.setText('7')
	def print8(self):
		self.ui.label.setText('8')
	def print9(self):
		self.ui.label.setText('9')
	def printplus(self):
		self.ui.label.setText('+')
	def printsub(self):
		self.ui.label.setText('-')
	def printdiv(self):
		self.ui.label.setText('%')
	def printmul(self):
		self.ui.label.setText('x')
	def printeq(self):
		self.ui.label.setText('=')


app = QApplication([])
window = DemoWindow()
window.show()
app.exec_()
