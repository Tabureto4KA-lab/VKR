import csv
import random


data = [['Extruder temperature zone 1',
         'Extruder temperature zone 2',
         'Extruder temperature zone 3',
         'Extruder pressure',
         'Chiller temperature',
         'Streighthening temperature',
         'Rolling velocity',

         'Extruder signal zone 1',
         'Extruder signal zone 2',
         'Extruder signal zone 3',
         'Extruder signal pressure',
         'Chiller signal',
         'Streighthening signal',
         'Rolling signal',

         'Defect']]

def fill(list, x_start, x_end):
        for i in range(25000):
                x = random.uniform(x_start, x_end)
                x = float('{:.1f}'.format(x))
                list.append(x)


temp_ex1 = []
temp_ex2 = []
temp_ex3 = []
press_ex = []
temp_chill = []
temp_strong = []
vel = []

ex1_ok = []
ex2_ok = []
ex3_ok = []
ex_press_ok = []
chill_ok = []
strong_ok = []
vel_ok = []

defect = []

fill(temp_ex1, 180, 220)
fill(temp_ex2, 180, 220)
fill(temp_ex3, 180, 220)
fill(press_ex, 0, 120)
fill(temp_chill, 5, 70)
fill(temp_strong, 10, 70)
fill(vel, 0.1, 5)


def quality(list1, list2, x_min, x_max):
        for i in range(25000):
                if (x_min <= list1[i] <= x_max):
                        list2.append(0)
                else: list2.append(1)


quality(temp_ex1, ex1_ok, 190.0, 210.0)
quality(temp_ex2, ex2_ok, 190.0, 210.0)
quality(temp_ex3, ex3_ok, 190.0, 210.0)
quality(press_ex, ex_press_ok, 10.0, 100.0)
quality(temp_chill, chill_ok, 20.0, 50.0)
quality(temp_strong, strong_ok, 20.0, 50.0)
quality(vel, vel_ok, 0.1, 2)

print(len(temp_chill))
print(len(chill_ok))




for i in range(25000):
        sc = 0
        if ex1_ok[i] == 1: sc = sc+1
        if ex2_ok[i] == 1: sc = sc+1
        if ex3_ok[i] == 1: sc = sc+1
        if ex_press_ok[i] == 1: sc = sc+1
        if chill_ok[i] == 1: sc = sc+1
        if strong_ok[i] == 1: sc = sc+1
        if vel_ok[i] == 1: sc = sc+1

        if sc == 0: defect.append(0)
        elif 0<sc<7: defect.append(random.choice([0, 1]))
        elif sc == 7: defect.append(1)


for i in range(25000):
        new_list = [temp_ex1[i], temp_ex2[i], temp_ex3[i], press_ex[i], temp_chill[i], temp_strong[i], vel[i], ex1_ok[i], ex2_ok[i], ex3_ok[i], ex_press_ok[i], chill_ok[i], strong_ok[i], vel_ok[i], defect[i]]
        data.append(new_list)


path = 'dataset.csv'


with open(path, mode='w', newline='') as file:
         writer = csv.writer(file)
         writer.writerows(data)