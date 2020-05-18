import random

class Placement_option():
    '''класс возможных вариантов размещения'''

    def __init__(self, res_date, sur_name, name, mid_name, num_pers, arr_date, num_days, sum_max):
        self.res_date = res_date
        self.sur_name = sur_name
        self.name = name
        self.mid_name = mid_name
        self.num_pers = num_pers
        self.arr_date = arr_date
        self.num_days = num_days
        self.sum_max = sum_max

    # через словарь значение - название номера, ключ - цена
    # так мы сможем определить название номера, потом обращаться надо по ключам

    def plac_op(self):
        sum_max_int = self.sum_max
        room_rates = []
        for line in open('found.txt', 'r', encoding="utf-8"):
            number, place, person, level = map(str, line.split(' '))
            number = int(number)
            person = int(person)
            if place == 'одноместный':
                rate = 2900
                if level == 'стандарт':
                    rate = int(rate * 1)
                    if person == int(self.num_pers):
                        room_rates.append(rate)
                        print(room_rates)
                elif level == 'стандарт_улучшенный':
                    rate = int(rate * 1.2)
                    if person == int(self.num_pers):
                        room_rates.append(rate)
                        print(room_rates)
                elif level == 'апартамент':
                    rate = int(rate * 1.5)
                    if person == int(self.num_pers):
                        room_rates.append(rate)
                        print(room_rates)
            elif place == 'двухместный':
                rate = 2300
                if level == 'стандарт':
                    rate = int(rate * 1)
                    if person == int(self.num_pers):
                        room_rates.append(rate)
                        print(room_rates)
                elif level == 'стандарт_улучшенный':
                    rate = int(rate * 1.2)
                    if person == int(self.num_pers):
                        room_rates.append(rate)
                        print(room_rates)
                else:
                    rate = int(rate * 1.5)
                    if person == int(self.num_pers):
                        room_rates.append(rate)
                        print(room_rates)
            elif place == 'полулюкс':
                rate = 3200
                if level == 'стандарт':
                    rate = int(rate * 1)
                    if person == int(self.num_pers):
                        room_rates.append(rate)
                        print(room_rates)
                elif level == 'стандарт_улучшенный':
                    rate = int(rate * 1.2)
                    if person == int(self.num_pers):
                        room_rates.append(rate)
                        print(room_rates)
                else:
                    rate = int(rate * 1.5)
                    if person == int(self.num_pers):
                        room_rates.append(rate)
                        print(room_rates)
            elif place == 'люкс':
                rate = 4100
                if level == 'стандарт':
                    rate = int(rate * 1)
                    if person == int(self.num_pers):
                        room_rates.append(rate)
                        print(room_rates)
                elif level == 'стандарт_улучшенный':
                    rate = int(rate * 1.2)
                    if person == int(self.num_pers):
                        room_rates.append(rate)
                        print(room_rates)
                else:
                    rate = int(rate * 1.5)
                    if person == int(self.num_pers):
                        room_rates.append(rate)
                        print(room_rates)


            if len(room_rates) == 0:
                if int(self.num_pers) < person:
                    if place == 'двухместный':
                        rate = 2300
                        if level == 'стандарт':
                            rate = (rate * 1)*70/100
                            room_rates.append(rate)
                        elif level == 'стандарт_улучшенный':
                            rate = (rate * 1.2)*70/100
                            room_rates.append(rate)
                        else:
                            rate = (rate * 1.5)*70/100
                            room_rates.append(rate)
                    if len(room_rates) == 0:
                        if place == 'полулюкс':
                            rate = 3200
                            if level == 'стандарт':
                                rate = (rate * 1)*70/100
                                room_rates.append(rate)
                            elif level == 'стандарт_улучшенный':
                                rate = (rate * 1.2)*70/100
                                room_rates.append(rate)
                            else:
                                rate = (rate * 1.5)*70/100
                                room_rates.append(rate)
                    if len(room_rates) == 0:
                        if place == 'люкс':
                            rate = 4100
                            if level == 'стандарт':
                                rate = (rate * 1)*70/100
                                room_rates.append(rate)
                            elif level == 'стандарт_улучшенный':
                                rate = (rate * 1.2)*70/100
                                room_rates.append(rate)
                            else:
                                rate = (rate * 1.5)*70/100
                                room_rates.append(rate)
        print(room_rates)
        a = 100
        room_rates.append(a)
        # теперь писать на втором уровне
        for price in room_rates:
            if price > sum_max_int:
                room_rates.remove(price)
        for price in room_rates:
            if max(room_rates) + 1000 <= int(self.sum_max):
                total_price = max(room_rates) + 1000
            elif max(room_rates) + 280 <= int(self.sum_max):
                total_price = max(room_rates) + 280
            else:
                total_price = max(room_rates)
        print(total_price)

        probability = ['да', 'да', 'да', 'нет']
        answer = random.choice(probability)

    def __str__(self):
        return self.plac_op()

