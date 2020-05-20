from new import Placement_option
with open('booking.txt', 'r', encoding="utf-8") as infile:
    for line in infile:
        res_date, sur_name, name, mid_name, num_pers, arr_date, num_days, sum_max = map(str, line.split(' '))
        num_pers = int(num_pers)
        num_days = int(num_days)
        sum_max = int(sum_max)
        small_dog = Placement_option(res_date, sur_name, name, mid_name, num_pers, arr_date, num_days, int(sum_max))
        print(small_dog)
