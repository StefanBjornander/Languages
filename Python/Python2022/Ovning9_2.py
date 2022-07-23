list = []

def observation(timmar, minuter, temperatur):
    list.append((timmar, minuter, temperatur))

def obs_tim():
    tim, min, temp = list[-1]
    return tim

def obs_min():
    tim, min, temp = list[-1]
    return min

def obs_temp():
    tim, min, temp = list[-1]
    return temp

tim = int(input('tim: '))
min = int(input('tim: '))
temp = int(input('tim: '))

observation(tim, min, temp)
print('tim', obs_tim())
print('min', obs_min())
print('temp', obs_temp())


