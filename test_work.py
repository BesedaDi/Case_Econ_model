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

    def client(self, nums, numbers):
        busy_numbers = []
        booking = open('booking.txt', 'r', encoding="utf-8")

        for i in booking:
            res_date, sur_name, name, mid_name, num_pers, arr_date, num_days, sum_max = map(str, i.split(
                ' '))
            print(res_date, sur_name, name, mid_name, num_pers, arr_date, num_days, sum_max)
            tek_price = 0

            for num in numbers:

                for k, v in num.items():
                    type = v[0]
                    people_number = v[1]
                    comfort = v[2]
                    price = v[3]

                    if int(people_number) == int(self.num_pers) and price <= int(self.sum_max):
                        if tek_price < price:
                            tek_price = price
                        if tek_price + 1000 <= int(self.sum_max):
                            tek_price = tek_price + 1000
                        elif tek_price + 280 <= int(self.sum_max):
                            tek_price = tek_price + 280
                            probability = ['да', 'да', 'да', 'нет']
                            answer = random.choice(probability)
                    elif int(people_number) < int(self.num_pers) and price <= int(self.sum_max):
                        if tek_price < price:
                            tek_price = price * 70 / 100
                        if tek_price + 1000 <= int(self.sum_max):
                            tek_price = tek_price + 1000
                        elif tek_price + 280 <= int(self.sum_max):
                            tek_price = tek_price + 280
                            probability = ['да', 'да', 'да', 'нет']
                            answer = random.choice(probability)

            print(tek_price)
            print('')

        for num in numbers:
            lst = dict.values()
            print(lst)






    # если согласен, то берем номер номера, создаем новый словарь, добавляем туда даты по количеству дней
    # потом по дате выводим через счетчик считаем номера на заданное число. из общего - занятые
    #

