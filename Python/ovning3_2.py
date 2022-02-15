import math;
radius = int(input("Radius: "));
if (radius > 0):
    area = radius * radius * math.pi; # calculate the area
    circumference = 2 * radius * math.pi; # calculate the circumference
    print(f'Area: {area:06.3f}, Circumference: {circumference:06.3f}');
else:
    print("Radius must be greater than zero.")
