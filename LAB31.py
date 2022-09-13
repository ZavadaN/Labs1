Rost = float(input('Какой у вас рост?'))
Ves = float(input('Какой у вас вес?'))
KolSh = float(input('Сколько шагов?'))
Time = float(input('Время активности'))
DlSh = Rost/4+0.37
S = DlSh*KolSh
V = S/Time
calories = 0.035*Ves + V*V/Rost*0.029*Ves
print("Количество сожженных каллорий", calories)
print("Пройденное расстояние", S)

