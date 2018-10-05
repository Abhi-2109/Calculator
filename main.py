import  sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Button :
    def __init__(self,text,results):
        self.b = QPushButton(str(text))
        self.text = text
        self.results = results
        self.b.clicked.connect(lambda : self.handleInput(self.text))  # Important because we need to pass only function name with arguments here that is why we use lambda here

    def handleInput(self,v):
        if self.results.text() != "":
            if self.results.text()[-1] == '+' or self.results.text()[-1] == '-' or self.results.text()[-1] == '*' or self.results.text()[-1] == '/' or self.results.text()[-1] == '√':
                if v == '+' or v == '-' or v == '*' or v == '/' or v == '√':
                    return
            if self.results.text()[-1] == '/' and v == 0 :
                return
        if v == "=":
            if self.results.text()[-1] in ['*','-','.','+','/']:
                return
            res = eval(self.results.text())
            self.results.setText(str(res))
        elif v == "AC":
            self.results.setText("")
        elif v == "DEL" :
            self.results.setText(self.results.text()[:-1])
        elif v == "√" and self.results.text() != '':
            self.results.setText(str(float(self.results.text())**0.5))
        elif v == "√" and self.results.text() == '':
            return
        else:
            current_value = self.results.text()
            new_value = current_value + str(v)
            self.results.setText(new_value)





class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.CreateApp()

    def CreateApp(self):

        # Create our Grid

        grid = QGridLayout()
        results = QLineEdit()

        buttons = ["AC","DEL","√","/",
                   7,8,9,"*",
                   4,5,6,"-",
                   1,2,3,"+",
                   0,".","="]

        row = 1
        col = 0

        grid.addWidget(results,0,0,1,4)

        for button in buttons :
            if col > 3:
                col = 0
                row +=1

            buttonObject = Button(button,results)

            if button == 0:
                grid.addWidget(buttonObject.b,row,col,1,2)
                col+=1
            else:
                grid.addWidget(buttonObject.b,row,col,1,1)

            col += 1

        self.setLayout(grid)
        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    #window.setGeometry(0,0,500,1000)
    sys.exit(app.exec_())
