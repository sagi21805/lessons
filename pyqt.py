from PyQt5 import QtWidgets
import sys


def getText():
    print(textBox.toPlainText())
    if checkBox.isChecked():
        print("i am checked")
        
def createWindow():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    
    button = QtWidgets.QPushButton(win)
    button.clicked.connect(getText)
    button.setText("press me")
    button.setGeometry(20, 20, 70, 70)    

    global checkBox
    checkBox = QtWidgets.QCheckBox(win)
    checkBox.setGeometry(190, 80, 80, 80)
    
    global textBox
    textBox = QtWidgets.QTextEdit(win)
    textBox.setGeometry(80, 80, 80, 80)
    win.show()
    sys.exit(app.exec_())
    
createWindow()

