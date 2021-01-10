import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from MineModel import * 

class MineWindow(QMainWindow):
    def __init__(self):
        super(MineWindow, self).__init__()

        self.width = 10
        self.height = 10
        self.numberOfBombs = 10

        self.model = MineModel(self.width, self.height, self.numberOfBombs)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        widget = QWidget()
        self.setCentralWidget(widget)
        
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')

        widget.setLayout(layout)

        hLayout0 = QHBoxLayout()
        self.newGameButton = QPushButton(str('New Game'))
        self.newGameButton.clicked.connect(self.newGameClicked)
        hLayout0.addWidget(self.newGameButton)

        layout.addLayout(hLayout0)

        hLayout1 = QHBoxLayout()

        self.movesLabel = QLabel("Moves")
        font = QFont("Arial", 24, QFont.Bold)
        self.movesLabel.setFont(font)
        self.movesLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.movesLabel.setAlignment(Qt.AlignCenter)
        hLayout1.addWidget(self.movesLabel)

        self.totalBombsLabel = QLabel("Total Bombs")
        font = QFont("Arial", 24, QFont.Bold)
        self.totalBombsLabel.setFont(font)
        self.totalBombsLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.totalBombsLabel.setAlignment(Qt.AlignCenter)
        hLayout1.addWidget(self.totalBombsLabel)

        layout.addLayout(hLayout1)
        hLayout2 = QHBoxLayout()

        self.moves = QLabel("0")
        font = QFont("Arial", 24, QFont.Bold)
        self.moves.setFont(font)
        self.moves.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.moves.setAlignment(Qt.AlignCenter)
        hLayout2.addWidget(self.moves)

        self.totalBombs = QLabel(str(self.numberOfBombs))
        font = QFont("Arial", 24, QFont.Bold)
        self.totalBombs.setFont(font)
        self.totalBombs.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.totalBombs.setAlignment(Qt.AlignCenter)
        hLayout2.addWidget(self.totalBombs)

        layout.addLayout(hLayout2)

        grid = QGridLayout()
        grid.setSpacing(0)

        self.buttons = []
        for row in range(self.height):
            for col in range(self.width):
                button = QPushButton(str(' '))
                button.clicked.connect(self.buttonClicked)
                button.setProperty("myRow", row)
                button.setProperty("myCol", col)
                grid.addWidget(button,row,col)
                self.buttons.append(button)
           

        layout.addLayout(grid)

        self.setWindowTitle('Mine SweeeepR')

        self.show()

    def buttonClicked(self):
        # sender() tells us who caused the action to take place
        clicked = self.sender()
        if self.model.getGameOver():
            return

        row = clicked.property("myRow")
        col = clicked.property("myCol")

        if not self.model.getCellExposed(row, col):
            self.model.setCellExposed(row, col)
            val = self.model.getCellValue(row, col)

            self.model.incrementTotalMoves()
            self.moves.setText( str(self.model.getTotalMoves()) )
            self.moves.update()

            if val < 0:
                clicked.setText("BOMB")
                self.model.setGameOver()
            else:
                clicked.setText(str(val))
            clicked.update()

    def newGameClicked(self):
        # sender() tells us who caused the action to take place
        clicked = self.sender()
        self.model.reset()

        self.moves.setText( str(self.model.getTotalMoves()) )
        self.moves.update()

        for button in self.buttons:
            button.setText(" ")
            button.update()

app = QApplication(sys.argv)
window = MineWindow()
app.exec_()
