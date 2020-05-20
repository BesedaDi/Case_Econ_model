import random

class Placement_option():
    '''Класс возможных вариантов размещения'''

    def __init__(self, reservation_date, surname, name, mid_name, num_pers, arr_date, num_days, sum_max):
        self.reservation_date = reservation_date
        self.surname = surname
        self.name = name
        self.mid_name = mid_name
        self.num_pers = num_pers
        self.arr_date = arr_date
        self.num_days = num_days
        self.sum_max = sum_max

    def nums(self):  # Хранение данных о каждом номере (с ценой проживания, но без учета питания)
        numbers = []
        individual_number = []
        with open('found.txt', 'r', encoding="utf-8") as found:
            for line in found:
                number, type, people_number, comfort = map(str, line.split())
                number = int(number)
                people_number = int(people_number)
                if type == 'одноместный':
                    price = 2900.00
                elif type == 'двухместный':
                    price = 2300.00
                elif type == 'люкс':
                    price = 4100.00
                elif type == 'полулюкс':
                    price = 3200.00

                if comfort == 'стандарт':
                    price = price * 1
                elif comfort == 'стандарт_улучшенный':
                    price = price * 1.2
                elif comfort == 'апартамент':
                    price = price * 1.5

                individual_number.append(type)
                individual_number.append(people_number)
                individual_number.append(comfort)
                individual_number.append(price)
                dict[number] = individual_number
                numbers.append(dict)
                individual_number = []
                dict = {}
            print(numbers)

    # в словаре в значениях смотрим по цене и количеству человек, добавляем импорт рандом

    def client(self, nums):
        busy_numbers = []

        for num in numbers





    # если согласен, то берем номер номера, создаем новый словарь, добавляем туда даты по количеству дней
    # потом по дате выводим через счетчик считаем номера на заданное число. из общего - занятые
    # 





