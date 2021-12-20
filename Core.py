import os
import shutil


def change_name():
    result = os.listdir()
    i = 0
    for temp in result:
        if ((temp.count('-') > 4) or (('.Н' in temp) and (temp.count('-') != 3))) and ('.pdf' in temp) and (
                'ОЛ' not in temp) and ('ИСХ' not in temp) and ('.С' not in temp):
            test_set = temp.split('-')
            test_set.pop()
            if len(test_set) >= 6:
                test_set.pop(4)
                clean_number = test_set[3]
                true_number = clean_number.split('.')
                true_number[1] = str(int(true_number[1]) + i)
                clean_number = '.'.join(true_number)
                test_set[3] = clean_number
                i += 1
            true_name = '-'.join(test_set) + '.pdf'
            shutil.copy(temp, true_name)
            os.remove(temp)


if __name__ == '__main__':
    change_name()
