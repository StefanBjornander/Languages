tid = int(input("Seconds: "));
hours = tid // 3600;
minutes = (tid % 3600) // 60;
seconds = (tid % 3600) % 60;
print(f'Hours: {hours:06d}, Minutes: {minutes:06d}, Seconds: {seconds:06d}');
