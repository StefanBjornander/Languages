import math;
T = 5730;
lamda = math.log(2) / T;
S = float(input("Time: "));
percent = math.exp(-lamda * S);
print(f'Percent: {percent:.3f}');
