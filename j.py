from PyQt5 import QtCore, QtGui, QtWidgets, uic
class MyWind(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWind,self).__init__()
        uic.loadUi('JARI.ui',self)

if __name__=='__main__':
    import sys
    app=QtWidgets.QApplication(sys.argv)
    window = MyWind()
    window.show()
    sys.exit(app.exec_())
