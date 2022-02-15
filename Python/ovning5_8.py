time1 = input("Time 1: ");
hour1 = int(time1[:2]);
minute1 = int(time1[3:]);

time2 = input("Time 2: ");
hour2 = int(time2[:2]);
minute2 = int(time2[3:]);

minutes1 = 60 * hour1 + minute1;
minutes2 = 60 * hour2 + minute2;

if (minutes2 < minutes1):
    minutes2 += 24 * 60;

minutes = minutes2 - minutes1;
print(f"{minutes} minutes.");