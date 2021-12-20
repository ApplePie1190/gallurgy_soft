import os
import shutil

def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)

# def change_name_new():
#     result = os.listdir()
#     for temp in result:
#         if (temp.count('-') >= 4) and ('.pdf' in temp) and ('ОЛ' not in temp) and ('ИСХ' not in temp) and and ('.С' not in temp):
#             test_set = temp.split('-')





def change_name():
    result = os.listdir()
    for temp in result:
        if (temp.count('-') >= 5) and ('.pdf' in temp) and ('ОЛ' not in temp):
            a = temp.rindex('-')
            b = temp[:a] + '.pdf'
            shutil.copy(temp, b)
            os.remove(temp)

def true_list_number():
    result = os.listdir()
    i = 0
    for temp in result:
        if (temp.count('-') >= 5) and ('.pdf' in temp) and ('_' in temp) :
            test_set = temp.split('-')
            problem_index = test_set[3].rindex('_')
            clean_number = test_set[3][:problem_index]
            true_number = clean_number.split('.')
            true_number[1] = str(int(true_number[1]) + i)
            clean_number = '.'.join(true_number)
            test_set[3] = clean_number
            clean_name = '-'.join(test_set)
            shutil.copy(temp, clean_name)
            os.remove(temp)
            i += 1


if __name__ == '__main__':

    result = os.listdir()
    i = 0
    print(result)
    for temp in result:
        if (temp.count('-') >= 4) and ('.pdf' in temp) and ('ОЛ' not in temp) and ('ИСХ' not in temp) and ('.С' not in temp):
            test_set = temp.split('-')
            print(test_set)
            test_set.pop()
            print(test_set)
            if len(test_set) >= 6:
                test_set.pop(4)
                print(test_set)
                clean_number = test_set[3]
                true_number = clean_number.split('.')
                true_number[1] = str(int(true_number[1]) + i)
                clean_number = '.'.join(true_number)
                test_set[3] = clean_number
                i += 1
                print(test_set)
            print(test_set)
            true_name = '-'.join(test_set) + '.pdf'
            shutil.copy(temp, true_name)
            os.remove(temp)







