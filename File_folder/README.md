# PythonLab2

import csv
import os


def make_dir(path_fol: str, path_sc1: str) -> None:
    '''Принимает имя пути, если файла нет создает'''
    if not os.path.isdir(path_fol):
        os.mkdir(path_fol)
    if not os.path.isdir(path_sc1):
        os.mkdir(path_sc1)


def run_1(path_to_csv: str=os.path.join("C:/", "PYTHON", "PythonLab2-1", "File_folder")) -> None:
    '''Основная функция работы скрипта'''
    path_fol, path_sc1 = "File_folder", "File_folder/scrnipt_1"
    make_dir(path_fol, path_sc1)
    list1 = []
    with open(path_to_csv=os.path.join("C:/", "PYTHON", "PythonLab2-1", "File_folder", 
    "dataset.csv", 'r', newline='')) as csvfile: 
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            list1.append(row)

    with open(path_to_csv=os.path.join("C:/", "PYTHON", "PythonLab2-1", "File_folder", 
    "scrnipt_1", "X.csv", 'w', newline="")) as csvfile_x:
        for i in range(0, len(list1)):
            all_data = [list1[i][0]]
            writer = csv.writer(csvfile_x)
            writer.writerow(all_data)

    with open(path_to_csv=os.path.join("C:/", "PYTHON", "PythonLab2-1", "File_folder",
    "scrnipt_1", "Y.csv", "w", newline="")) as csvfile_y:
        for i in range(0, len(list1)):
            all_data = list1[i][1:]
            writer = csv.writer(csvfile_y)
            writer.writerow(all_data)

    print("\nscript_1 has finished working\n")







import csv
import os
import re


# Написать скрипт, который разобъёт исходный csv файл на N файлов,
# где каждый отдельный файл будет соответствовать одному году.
# Файлы называются по первой и последней дате, которую они содержат.
# (если файл содержит данные с первого января 2001 по 31 декабря 2001, то файл назвать 20010101_20011231.csv)

def make_dir(path_sc2: str) -> None:
    '''Принимает имя пути, если файла нет создает'''
    if not os.path.isdir( path_sc2):
        os.mkdir(path_sc2)


def work_file(date_1: str, date_2: str, list1_years: list, path_to_csv: str) -> None:
    '''Принимает имя пути, записывает в список'''
    name_file = path_to_csv + '/scrnipt_2/' + date_1 + "_" + date_2 + ".csv"
    print("create file: ", name_file)
    with open(name_file, 'w', newline='', encoding="utf-8") as namefile:
        writer = csv.writer(namefile)
        for i in range(len(list1_years)):
            writer.writerow(list1_years[i])


def run_2(path_to_csv: str=os.path.join("C:/", "PYTHON", "PythonLab2-1", "File_folder")) -> None:
    '''Основная функция работы скрипта'''
    path_sc2 = "File_folder/scrnipt_2"
    make_dir(path_to_csv, path_sc2)
    set1 = set()
    list1_years = []
    with open(path_to_csv=os.path.join("C:/", "PYTHON", "PythonLab2-1", "File_folder",
     'dataset.csv', 'r', newline='', encoding="utf-8")) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            set1.add(row[0][:4])
    set1 = sorted(list(set1), reverse=True)
    n = len(set1)

    with open(path_to_csv=os.path.join("C:/", "PYTHON", "PythonLab2-1", "File_folder",
     'dataset.csv', 'r', newline='', encoding="utf-8")) as csvfile:
        file_reader = list(csv.reader(csvfile))
        for i in range(n):
            for j in range(len(file_reader)):
                if (file_reader[j][0][:4] == set1[i]): list1_years.append(file_reader[j])
            print(list1_years[0][0])
            date_1 = str(re.sub(r'[-]', '', list1_years[0][0]))
            date_2 = str(re.sub(r'[-]', '', list1_years[-1][0]))
            work_file(date_1, date_2, list1_years, path_to_csv)
            list1_years = []

    print("\nscript_2 has finished working\n")
    
    
    
    
    
    
import csv
import os


# Написать скрипт, который разобъёт исходный csv файл на N файлов, 
# где каждый отдельный файл будет соответствовать одной неделе. 
# Файлы называются по первой и последней дате, которую они содержат.

def make_dir(path_sc3: str) -> None:
    '''Принимает имя пути, если файла нет создает'''
    if not os.path.isdir(path_sc3):
        os.mkdir(path_sc3)


def sort_week(all_data: list, path_to_csv: str) -> None:
    '''Принимает данные, сортирует по неделям'''
    day = len(all_data)
    week = []
    count = 0
    while (day != 0):
        if (day >= 7):
            for i in range(7):
                week.append(all_data[count])
                count += 1
            work_file(week, path_to_csv)
            day -= 7
        elif (day < 7):
            for i in range(day):
                week.append(all_data[count])
                count += 1
            work_file(week, path_to_csv)
            day = 0
        week = []


def work_file(week: list, path_to_csv: str) -> None:
    '''Принимает недели, сортирует по файлам'''
    date_1 = week[0][0][8:10]
    date_2 = week[-1][0][8:10]
    name_file = path_to_csv + '/scrnipt_3/' + str(week[0][0][:4]) + "_" + str(
        week[0][0][5:7]) + "_" + date_1 + "_" + date_2 + ".csv"
    print(name_file)
    with open(name_file, 'w', newline='', encoding="utf-8") as file_scr3:
        writer = csv.writer(file_scr3)
        for i in range(len(week)):
            writer.writerow(week[i])


def run_3(path_to_csv: str=os.path.join("C:/", "PYTHON", "PythonLab2-1", "File_folder")) -> None:
    '''Основная функция работы скрипта'''
    path_sc3 = "File_folder/scrnipt_3"
    make_dir(path_sc3)
    set1 = set()
    with open(path_to_csv=os.path.join("C:/", "PYTHON", "PythonLab2-1", "File_folder",
     'dataset.csv', 'r', newline='', encoding="utf-8")) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            set1.add(row[0][:4])
    set1 = sorted(list(set1), reverse=True)
    n = len(set1)

    with open(path_to_csv=os.path.join("C:/", "PYTHON", "PythonLab2-1", "File_folder",
     'dataset.csv', 'r', newline='', encoding="utf-8")) as csvfile:
        file_reader = list(csv.reader(csvfile))
        all_data = []
        month, year = 9, 2022
        while (year != 2009):
            for row in file_reader:
                if (int(row[0][5:7]) == month):
                    all_data.append(row)
                elif (int(row[0][5:7]) > month):
                    month = int(row[0][5:7])
                    year -= 1
                elif (int(row[0][5:7]) < month):
                    print(month, year)
                    month -= 1
                    if (month == 1):
                        pass
                    sort_week(all_data, path_to_csv)
                    all_data = []
                    all_data.append(row)

    print("\nscript_3 has finished working\n")



import os
import csv
import re
import datetime
from typing import List, Optional


# Написать скрипт, содержащий функцию, 
# принимающую на вход дату (тип datetime) и возвращающий данные для этой даты (из файла) или 
# None если данных для этой даты нет. Функция должна быть представлена в четырёх версиях в зависимости от 
# типа входных файлов, из которых будут прочитаны данные (пункты 0–3). 
# 
# Написать функцию next(), 
# которая будет при первом вызове возвращать данные для самой ранней возможной даты (возвращается кортеж (дата, данные)), 
# а при каждом следующем вызове данные для следующей по порядку даты. Если попадается дата, для которой данные отсутствуют, 
# то она игнориуруется и возвращаются данные для следующей валидной даты.


def next(count: int) -> Optional[List[str]]: # Union[None, List[int]]
    '''функция next, принимает count, выводит значение по индексу'''
    with open(path_to_csv=os.path.join("C:/", "PYTHON", "PythonLab2-1", "File_folder",
     'dataset.csv', 'r', newline='', encoding="utf-8")) as csvfile:
        file_reader = list(csv.reader(csvfile))
        if (file_reader[count] == None):
            return None
        else:
            return file_reader[count]
            #print(*file_reader[count])


def work_0(date: datetime.dat) -> None:
    "принимает данные, ищет их в файле соответствующего скрипта"
    with open(path_to_csv=os.path.join("C:/", "PYTHON", "PythonLab2-1", "File_folder",
     'dataset.csv', 'r', newline='', encoding="utf-8")) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            if (row[0] == str(date)):  # если одинаковые даты - выводим
                print(*row)
                break
        else:
            return None


def work_1(date: datetime.dat) -> None:
    "принимает данные, ищет их в файле соответствующего скрипта"
    with open(path_to_csv=os.path.join("C:/", "PYTHON", "PythonLab2-1", "File_folder",
    'scrnipt_1', 'X.csv', 'r', newline='', encoding="utf-8")) as csvfile:
        file_reader = list(csv.reader(csvfile))
        for i in range(len(file_reader)):
            if (file_reader[i][0] == str(
                    date)):  # ищем в фале Х запоминаем номер строки, выводим данные по номеру строки в фале Y
                tmp = i
                break
        else:
            return None
    with open(path_to_csv=os.path.join("C:/", "PYTHON", "PythonLab2-1", "File_folder",
    'scrnipt_1', 'Y.csv', 'r', newline='', encoding="utf-8")) as csvfile:
        file_reader = list(csv.reader(csvfile))
        print(*file_reader[tmp])



def work_2(date: datetime.date, path_to_csv: str) -> None:
    "принимает данные, ищет их в файле соответствующего скрипта"
    ways = os.listdir(path_to_csv=os.path.join("C:/", "PYTHON", "PythonLab2-1", "File_folder", 'scrnipt_2'))
    date = str(date)
    for i in range(len(ways)):
        if (ways[i][:4] == date[:4]):  # Ищем файл у которого аткой же год
            with open(path_to_csv + "/scrnipt_2/" + ways[i], 'r', newline='', encoding="utf-8") as csvfile:
                file_reader = csv.reader(csvfile)
                for row in file_reader:
                    if (row[0] == date):
                        print(*row)
                        csvfile.close()
                        break
    else:
        csvfile.close()
        return None


def work_3(date: datetime.date, path_to_csv: str) -> None:
    "принимает данные, ищет их в файле соответствующего скрипта"
    ways = os.listdir(path_to_csv=os.path.join("C:/", "PYTHON", "PythonLab2-1", "File_folder", 'scrnipt_3'))
    list1 = []
    date = str(date)
    date = re.sub(r'[-]', '_', date)
    for i in range(len(ways)):  # выбираем одинаковые года и месяцы, записываем файлы в лист
        if (ways[i][:7] == date[:7]):
            list1.append(ways[i])
    if (list1 == None): return None
    for i in range(len(list1)):
        if (int(list1[i][11:13]) >= int(date[8:10]) >= int(
                list1[i][8:10])):  # если число находится в диапозоне недели то выводим его
            with open(path_to_csv + "/scrnipt_3/" + list1[i], 'r', newline='', encoding="utf-8") as csvfile:
                file_reader = csv.reader(csvfile)
                date = re.sub(r'[_]', '-', date)
                for row in file_reader:
                    if (row[0] == date):
                        print(*row)
                        csvfile.close()
                        break
    else:
        csvfile.close()
        return None


def run_4(path_to_csv: str=os.path.join("C:/", "PYTHON", "PythonLab2-1", "File_folder")) -> None:
    '''Основная функция работы скрипта'''
    date = datetime.date(2022, 9, 7)
    work_0(date, path_to_csv)
    work_1(date, path_to_csv)
    work_2(date, path_to_csv)
    work_3(date, path_to_csv)

    with open(path_to_csv=os.path.join("C:/", "PYTHON", "PythonLab2-1", "File_folder",
     'dataset.csv', 'r', newline='', encoding="utf-8")) as csvfile:
        count = 0
        while (count != 50):
            next(count, path_to_csv)
            count += 1

    print("\nscript_4 has finished working\n")



from typing import Self
import os


class Iterator:

    def __init__(self, name_of_file: str) -> None:
        self.name_of_file = name_of_file
        self.counter = 0
        self.list = []
        file = open(self.name_of_file, "r", encoding="utf-8")
        for row in file:
            self.list.append(row)
        file.close

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> int:
        if self.counter < len(self.list):
            tmp = self.list[self.counter]
            self.counter += 1
            return tmp
        else:
            raise StopIteration


def run_5(path_to_csv: str=os.path.join("C:/", "PYTHON", "PythonLab2-1", "File_folder")) -> None:
    '''Основная функция работы скрипта'''
    file_name = path_to_csv + "/scrnipt_2/20220901_20220130.csv"
    s_iter1 = Iterator(file_name)
    for val in s_iter1:
        print(val, end="")
    print("\nscript_5 has finished working\n")
