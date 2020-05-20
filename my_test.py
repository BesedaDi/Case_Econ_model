numbers = []
individual_number = []
dict = {}
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

