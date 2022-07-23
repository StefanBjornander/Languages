a = ' Erik Andersson 990314-2714 '
j = a.find('-')
b = a[j - 2:j] + '/' + a[j - 4:j - 2]
print(b)