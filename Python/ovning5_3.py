import datetime;
person = input("Person Number: ");

if (len(person) != 10):
    print("Wrong Length");
else:
    digit = int(person[8]);

    if ((digit % 2) == 0):
        print("Women");
    else:
        print("Man");
        