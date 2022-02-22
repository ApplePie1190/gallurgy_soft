from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 146)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_start.setObjectName("btn_start")
        self.gridLayout.addWidget(self.btn_start, 3, 2, 1, 1)
        self.btn_browse = QtWidgets.QPushButton(self.centralwidget)
        self.btn_browse.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.btn_browse.setObjectName("btn_browse")
        self.gridLayout.addWidget(self.btn_browse, 3, 1, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setStyleSheet("background-color: rgb(253, 255, 134);")
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 1, 1, 2)
        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.gridLayout.addWidget(self.progress_bar, 2, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rename PDF files"))
        self.btn_start.setText(_translate("MainWindow", "Переименовать PDF файлы"))
        self.btn_browse.setText(_translate("MainWindow", "Выберите проект"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
