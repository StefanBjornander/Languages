sign = 1;
term = 1;
sum = 0;

while (abs(term) >= 0.00001):
    sum += sign * term;
    sign *= -1;
    term /= 2;
    #print(f"Sign: {sign}, Term: {term}, Sum: {sum}");
print(f"Sum: {sum}");
