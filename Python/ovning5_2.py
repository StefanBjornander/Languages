import datetime;
person = input("Person Number: ");

if (len(person) != 10):
    print("Wrong Length");
else:
    month = int(person[2:4]);
    day = int(person[4:6]);
    today = datetime.datetime.now();

    if ((month == today.month) and (day == today.day)):
        print("Congratulations.");

