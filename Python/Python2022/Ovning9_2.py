g_timmar = 0
g_minuter = 0
g_temperatur = 0

def observation(timmar, minuter, temperatur):
    g_timmar = timmar
    g_minuter = minuter
    g_temperatur = temperatur
    print(g_temperatur)

def obs_tim():
    return g_timmar

def obs_min():
    return g_minuter

def obs_temp():
    return g_temperatur
