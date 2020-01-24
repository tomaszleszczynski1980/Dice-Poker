# musimy stworzyć listę paternów, którą kość przerzucamy, a którą nie.

number_of_dices = 5

pattern_list = []

for i in (bin(x) for x in range(0, 2 ** number_of_dices)):
    pattern = str(i)[2:]
    pattern_list.append(pattern.zfill(number_of_dices))
