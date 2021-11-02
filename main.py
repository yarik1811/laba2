import json
import re
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('path_in', help='Get path file input')
parser.add_argument('path_out', help='Get path file output')
args = parser.parse_args()


class validator:
    def __init__(self):
        pass

    def check_telephone(telephone: str) -> bool:
        """
                Выполняет проверку корректности номера телефона
                Если нормер соответствует формату +7-(xxx)-xxx-xx-xx то будет возвращено False

                Параметры
                ---------
                    telephone : str
                        Строка для проверки корректности

                    Return
                    ------
                        bool:
                        Булевый результат на корректность
        """
        if type(telephone) != str:
            return False
        pattern = "^\+\d-\(\d{3}\)-\d{3}-\d{2}-\d{2}"
        if re.match(pattern, telephone):
            return True
        return False

    def check_height(height: str) -> bool:
        """
                Выполняет проверку корректности массы
                Если значение массы не строковое, состоит из букв, разделено (,), или 1<x<3 то будет ворвращено False

                Параметры
                ---------
                  height : str
                    Параметр для проверки корректности

                Return
                ------
                  bool:
                    Булевый результат на коррестность
                """
        if type(height) != str:
            return False
        if re.findall(',|[a-zA-Z]|[а-яёА-ЯЁ]]', height):
            return False
        if float(height) < 1.00 or float(height) > 2.30:
            return False
        return True

    def check_inn(inn: str) -> bool:
        """
                Выполняет проверку корректности ИНН
                Если ИНН не состоит из последовательности 12 цифр то будет возвращено False

                Параметры
                ---------
                  inn : str
                    Строка для проверки корректности

                Return
                ------
                  bool:
                    Булевый результат на корректность
                """
        if type(inn) != str:
            return False
        if len(inn) == 12:
            return True
        return False

    def check_passport_series(series: str) -> bool:
        """
                Выполняет проверку корректности номера паспорта
                Если серия паспорта не состоит из последовательности (xx xx) то будет возвращено False

                Параметры
                ---------
                passport : str
                    Целое число для проверки корректности

                Return
                ------
                    bool:
                    Булевый результат на корректность
                """
        pattern = "\d{2}\s\d{2}"
        if re.match(pattern, series):
            return True
        return False

    def check_occupation(occupation: str) -> bool:
        """
                  Выполняет проверку типа данных параметра
                  Если пераметр не имеет тип данных str возвращено False

                  Параметры
                  ---------
                    string:
                      Параметр для проверки типа данных

                  Return
                  ------
                    bool:
                      Булевый результат на корректность
                """
        if type(occupation) != str:
            return False
        return True

    def check_work_experience(work_experience: int) -> bool:
        """
            Выполняет проверку типа данных параметра
            Если пераметр не имеет тип данных int и его значение лежит между 14 и 80 то возвращено False

                Параметры
                ---------
                number:
                Параметр для проверки типа данных и диапозона

                Return
                ------
                bool:
                Булевый результат на корректность
        """
        if type(work_experience) != int:
            return False
        if work_experience < 0 or work_experience > 60:
            return False
        return True

    def check_views(views: str) -> bool:
        """
                  Выполняет проверку типа данных параметра
                  Если пераметр не имеет тип данных str возвращено False

                  Параметры
                  ---------
                    string:
                      Параметр для проверки типа данных

                  Return
                  ------
                    bool:
                      Булевый результат на корректность
                """
        if type(views) != str:
            return False
        return True

    def check_worldview(worldview: str) -> bool:
        """
                Выполняет проверку типа данных параметра
                Если пераметр не имеет тип данных str возвращено False

                Параметры
                ---------
                string:
                    Параметр для проверки типа данных

                Return
                ------
                bool:
                    Булевый результат на корректность
        """
        if type(worldview) != str:
            return False
        return True

    def check_address(address: str) -> bool:
        """
                Выполняет проверку корректности адреса
                Если адрес нет строки или указан не в формате "улица пробел номер дома" то возвращено False

                Параметры
                ---------
                address:
                    Параметр для проверки корректности

                Return
                ------
                bool:
                    Булевый результат на корректность
        """
        if type(address) == str:
            pattern = '[а-яА-Я.\s\d-]+\s+[0-9]+$'
            if re.match(pattern, address):
                return True
        return False


data = json.load(open(args.path_in, encoding='windows-1251'))

true_data = list()
telephone = 0
height = 0
inn = 0
passport_series = 0
occupation = 0
work_experience = 0
political_views = 0
worldview = 0
address = 0

with tqdm(total=len(data)) as progressbar:
    for person in data:
        temp = True
        if not validator.check_telephone(person['telephone']):
            telephone += 1
            temp = False
        if not validator.check_height(person['height']):
            height += 1
            temp = False
        if not validator.check_inn(person['inn']):
            inn += 1
            temp = False
        if not validator.check_passport_series(person['passport_series']):
            passport_series += 1
            temp = False
        if not validator.check_occupation(person["occupation"]):
            occupation += 1
            temp = False
        if not validator.check_work_experience(person['work_experience']):
            work_experience += 1
            temp = False
        if not validator.check_views(person['political_views']):
            political_views += 1
            temp = False
        if not validator.check_worldview(person['worldview']):
            worldview += 1
            temp = False
        if not validator.check_address(person["address"]):
            address += 1
            temp = False
        if temp:
            true_data.append(person)
        progressbar.update(1)

out_put = open(args.path_out, 'w', encoding='utf-8')
beauty_data = json.dumps(true_data, ensure_ascii=False, indent=4)
out_put.write(beauty_data)
out_put.close()

print(f'Число валидных записей: {len(true_data)}')
print(f'Число невалидных записей: {len(data) - len(true_data)}')
print(f'  - Число невалидных номеров телефона:  {telephone}')
print(f'  - Число невалидных ростовых замеров: {height}')
print(f'  - Число невалидных ИНН: {inn}')
print(f'  - Число невалидных серий паспорта: {passport_series}')
print(f'  - Число невалидных политических взглядов: {occupation}')
print(f'  - Число невалидных опытов работы:  {work_experience}')
print(f'  - Число невалидных политических взглядов: {political_views}')
print(f'  - Число невалидных мировоззрений: {worldview}')
print(f'  - Число невалидных адрессов: {address}')


print('Вы закончили мучение над моей лабой, вот вам коровка')
print(' /-----------\\')
print('<    му-му    >')
print(' \\-----------/')
print('                \\')
print('                 \\')
print('                   ^__^')
print('                   (oo)\_______')
print('                   (__)\\       )\\/\\')
print('                       ||----w |')
print('                       ||     ||\n')