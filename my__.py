import random
numbers = []
individual_number = []
dict = {}
a = []
with open('found.txt', 'r', encoding="utf-8") as found:
        for line in found:
            number, type, people_number, comfort = map(str, line.split())
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

                    if int(people_number) == int(num_pers) and price <= int(sum_max) and 2300 < int(sum_max):

                        if tek_price < price:
                            tek_price = price
                            name = type + ' ' + comfort
                            if tek_price + 1000 <= int(sum_max):
                                tek_price = tek_price + 1000
                                tek_tek_price = tek_price * int(num_pers)
                                food = 'полупонсион'
                            elif tek_price + 280 <= int(sum_max):
                                tek_price = tek_price + 280
                                tek_tek_price = tek_price * int(num_pers)
                                food = 'завтрак'
                            else:
                                tek_price = tek_price
                                tek_tek_price = tek_price * int(num_pers)
                                food = 'без питания'
                        probability = ['да', 'да', 'да', 'нет']
                        answer = random.choice(probability)

                    elif int(people_number) > int(num_pers) and price <= int(sum_max) and 2300 < int(sum_max):
                        if tek_price < price:
                            tek_price = (price * 70 / 100)
                            name = type + ' ' + comfort
                            if tek_price + 1000 <= int(sum_max):
                                tek_price = tek_price + 1000
                                tek_tek_price = tek_price * int(num_pers)
                                food = 'полупонсион'
                            elif tek_price + 280 <= int(sum_max):
                                tek_price = tek_price + 280
                                tek_tek_price = tek_price * int(num_pers)
                                food = 'завтрак'
                            else:
                                tek_price = tek_price
                                food = 'без питания'

                        probability = ['да', 'да', 'да', 'нет']
                        answer = random.choice(probability)

            print(answer)

            print(name)
            print(food)
            print(tek_price)
            print(num_pers)
            print(tek_tek_price)
            print('')
            stroka = 'Ответ на предложение: ' + answer + ';' + ' ' + 'Номер: ' + name + ';' + ' ' + \
                  'Тип питания: ' + food + ';' + ' ' + 'Цена на одного: ' + \
                     str(tek_price) + ', за всех ' + str(tek_tek_price)
            print(stroka)
            print('')
