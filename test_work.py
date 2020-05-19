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


    def plac_op(self):
        room_rates = []
        new_room_rates = []
        new_new_room_rates = []
        room = []

        with open('found.txt', 'r', encoding="utf-8") as found:
            for line in found:
                number, place, person, level = map(str, line.split())
                number = int(number)
                person = int(person)
                if place == 'одноместный':
                    rate = 2900
                    if level == 'стандарт':
                        rate = int(rate * 1)
                        room_rates.append(rate)
                        m1 = 'одноместный стандарт'
                        n1 = rate

                    elif level == 'стандарт_улучшенный':
                        rate = int(rate * 1.2)
                        room_rates.append(rate)
                        m2 = 'одноместный стандарт_улучшенный'
                        n2 = rate

                    elif level == 'апартамент':
                        rate = int(rate * 1.5)
                        room_rates.append(rate)
                        m3 = 'одноместный апартамент'
                        n3 = rate
                elif place == 'двухместный':
                    rate = 2300
                    if level == 'стандарт':
                        rate = int(rate * 1)
                        room_rates.append(rate)
                        m = 'двухместный стандарт'
                        n = rate
                    elif level == 'стандарт_улучшенный':
                        rate = int(rate * 1.2)
                        room_rates.append(rate)
                        m = 'двухместный стандарт_улучшенный'
                        n = rate
                    elif level == 'апартамент':
                        rate = int(rate * 1.5)
                        room_rates.append(rate)
                        m = 'двухместный апартамент'
                        n = rate
                elif place == 'полулюкс':
                    rate = 3200
                    if level == 'стандарт':
                        rate = int(rate * 1)
                        room_rates.append(rate)
                        m = 'полулюкс стандарт'
                        n = rate
                    elif level == 'стандарт_улучшенный':
                        rate = int(rate * 1.2)
                        room_rates.append(rate)
                        m = 'полулюкс стандарт_улучшенный'
                        n = rate
                    elif level == 'апартамент':
                        rate = int(rate * 1.5)
                        room_rates.append(rate)
                        m = 'полулюкс апартамент'
                        n = rate
                elif place == 'люкс':
                    rate = 4100
                    if level == 'стандарт':
                        rate = int(rate * 1)
                        room_rates.append(rate)
                        m = 'люкс стандарт'
                        n = rate
                    elif level == 'стандарт_улучшенный':
                        rate = int(rate * 1.2)
                        room_rates.append(rate)
                        m = 'люкс стандарт_улучшенный'
                        n = rate
                    elif level == 'апартамент':
                        rate = int(rate * 1.5)
                        room_rates.append(rate)
                        m = 'люкс апартамент'
                        n = rate

                if len(room_rates) == 0:
                    if int(self.num_pers) < person:
                        if place == 'двухместный':
                            rate = 2300
                            if level == 'стандарт':
                                rate = (rate * 1) * 70 / 100
                                room_rates.append(rate)
                                m = 'двухместный стандарт'
                                n = rate
                            elif level == 'стандарт_улучшенный':
                                rate = (rate * 1.2) * 70 / 100
                                room_rates.append(rate)
                                m = 'двухместный стандарт_улучшенный'
                                n = rate
                            elif level == 'апартамент':
                                rate = (rate * 1.5) * 70 / 100
                                room_rates.append(rate)
                                m = 'двухместный апартамент'
                                n = rate
                        if len(room_rates) == 0:
                            if place == 'полулюкс':
                                rate = 3200
                                if level == 'стандарт':
                                    rate = (rate * 1) * 70 / 100
                                    room_rates.append(rate)
                                    m = 'полулюкс стандарт'
                                    n = rate
                                elif level == 'стандарт_улучшенный':
                                    rate = (rate * 1.2) * 70 / 100
                                    room_rates.append(rate)
                                    m = 'полулюкс стандарт_улучшенный'
                                    n = rate
                                elif level == 'апартамент':
                                    rate = (rate * 1.5) * 70 / 100
                                    room_rates.append(rate)
                                    m = 'полулюкс апартамент'
                                    n = rate
                        if len(room_rates) == 0:
                            if place == 'люкс':
                                rate = 4100
                                if level == 'стандарт':
                                    rate = (rate * 1) * 70 / 100
                                    room_rates.append(rate)
                                    a = 19
                                    room_rates.append(a)
                                    m = 'люкс стандарт'
                                    n = rate
                                elif level == 'стандарт_улучшенный':
                                    rate = (rate * 1.2) * 70 / 100
                                    room_rates.append(rate)
                                    a = 20
                                    room_rates.append(a)
                                    m = 'люкс стандарт_улучшенный'
                                    n = rate
                                elif level == 'апартамент':
                                    rate = (rate * 1.5) * 70 / 100
                                    room_rates.append(rate)
                                    a = 21
                                    room_rates.append(a)
                                    m = 'люкс апартамент'
                                    n = rate
            print(room_rates)
            # теперь писать на втором уровне
            for price in room_rates:
                if price <= int(self.sum_max):
                    new_room_rates.append(price)
            new_room_rates = sorted(new_room_rates, reverse=True)
            print(new_room_rates)

            for i in new_room_rates:
                el1 = i + 1000
                el2 = i + 280
                el3 = i
                if el1 > el2 and el1 <= int(self.sum_max):
                    total_price = el1
                new_new_room_rates.append(el1)
                new_new_room_rates.append(el2)
                new_new_room_rates.append(el3)
            print(new_new_room_rates)
            for price in new_new_room_rates:
                if price <= int(self.sum_max):
                    room.append(price)
            total_price = str(max(room))
            print(total_price)

            probability = ['да', 'да', 'да', 'нет']
            answer = random.choice(probability)


    def __str__(self):
        return self.plac_op()


