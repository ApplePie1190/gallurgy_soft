import sys
from PyQt5 import QtWidgets
import maket  # Это наш конвертированный файл дизайна
import core_new


class ExampleApp(QtWidgets.QMainWindow, maket.Ui_MainWindow):
    directory = ''

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле maket.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.btn_browse.clicked.connect(self.browse_folder)  # Выполнить функцию browse_folder
        self.btn_start.clicked.connect(self.pdf_rename)  # Выполнить функцию при нажатии кнопки переименовать

    def browse_folder(self):
        self.listWidget.clear()  # На случай, если в списке уже есть элементы
        self.directory = QtWidgets.QFileDialog.getExistingDirectory()
        self.progress_bar.setValue(0)
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории

        if self.directory != '':  # не продолжать выполнение, если пользователь не выбрал директорию
            self.listWidget.addItem(self.directory)  # добавить файл в listWidget
            self.my_files = core_new.PdfClass(self.directory)  # создали объект класса PDF

    def pdf_rename(self):
        if self.my_files.files_count == 0:  # если нужных файлов нет выводим сообщение
            self.listWidget.clear()
            self.listWidget.addItem('Отсутствуют файлы')
        else:  # если есть запускаем методы ренейма
            self.my_files.rename_easy_file()
            self.progress_bar.setValue(50)  # заполняем прогрес
            self.my_files.rename_hard_file()
            self.progress_bar.setValue(100)
            self.listWidget.clear()
            self.listWidget.addItem(f'Успешно переименовано {self.my_files.files_count} файлов')


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':
    main()
