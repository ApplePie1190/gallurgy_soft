import os


class PdfClass:
    progress = 0

    def __init__(self, dir):
        self.dir = dir  # путь к проекту
        self.files_count = len(self.easy_pdf_files()) + len(self.hard_pdf_files())  # количество ПДФ файлов

    def easy_pdf_files(self):  # создаем список простых ПДФ файлов
        pdf_files = [file for file in os.listdir(self.dir) if
                     (((file.count('-') > 4) and (file.count('-') < 6)) or (('.Н' in file) and (file.count('-') != 3)))
                     and (file.endswith('.pdf'))
                     and ('ОЛ' not in file)
                     and ('ИСХ' not in file)
                     and ('.С' not in file)]
        return pdf_files

    def hard_pdf_files(self):  # создаем список файлов со сложным номером
        pdf_files = [file for file in os.listdir(self.dir) if file.count('-') > 5 and
                     file.endswith('.pdf')]
        return pdf_files

    def rename_easy_file(self):  # ренейм простых файлов
        for file_name in self.easy_pdf_files():
            name_set = file_name.split('-')  # делим имя по "-"
            name_set.pop()  # удаляем конец
            full_dir = os.path.join(self.dir, file_name)
            if '.Н' in file_name and file_name.count('-') != 3:  # именуем Нки
                true_name = f'{self.dir}/{name_set[0]}-{name_set[1]}-{name_set[2]}-{name_set[3]}.pdf'
                os.rename(full_dir, true_name)
            else:
                true_name = self.dir + '/' + '-'.join(name_set) + '.pdf'  # именуем все остальное
                os.rename(full_dir, true_name)

    def rename_hard_file(self):  # ренейм сложных файлов
        if len(self.hard_pdf_files()) != 0:
            j = 0
            name_set = self.hard_pdf_files()[0].split('-')
            clean_number = name_set[3]
            basic_number = clean_number.split('.')[0]
            for file in self.hard_pdf_files()[:]:
                name_set = file.split('-')
                name_set.pop()
                name_set.pop(4)
                full_dir = os.path.join(self.dir, file)
                clean_number = name_set[3]
                true_number = clean_number.split('.')
                if true_number[0] == basic_number:
                    true_number[1] = str(int(true_number[1]) + j)
                    clean_number = '.'.join(true_number)
                    name_set[3] = clean_number
                    true_name = self.dir + '/' + '-'.join(name_set) + '.pdf'
                    os.rename(full_dir, true_name)
                    j += 1
                else:
                    j = 0
                    basic_number = clean_number.split('.')[0]
                    true_number[1] = str(int(true_number[1]) + j)
                    clean_number = '.'.join(true_number)
                    name_set[3] = clean_number
                    true_name = self.dir + '/' + '-'.join(name_set) + '.pdf'
                    os.rename(full_dir, true_name)
                    j += 1


if __name__ == '__main__':
    path = '/temp'
    a = PdfClass(path)
    print(a.easy_pdf_files())
    print(a.hard_pdf_files())
    a.rename_easy_file()
    a.rename_hard_file()

