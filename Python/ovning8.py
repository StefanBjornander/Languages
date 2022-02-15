#8.1
def moms(price, percent):
    return price * (1 + (percent / 100));
print(moms(100, 20));
print();

#8.2
def mult(number):
    for index in range(1, 11):
        print(index, index * number);
mult(6);
print();

#8.3
def letters(text):
    small = 0;
    large = 0;
    for c in text:
        if ((c == c.lower()) and (c != c.upper())):
            small += 1;
        if ((c == c.upper()) and (c != c.lower())):
            large += 1;
    return (small, large);
print(letters("aBC!#deFG"));
print();
        
#8.4
def prime(number):
    index = 2;
    for index in range(2, (number // 2) + 1):
        if ((number % index) == 0):
            return False;
    return True;
print(prime(5));
print(prime(6));
print();

#8.5
def relativeprime(number1, number2):
    index = 2;
    m = max(number1, number2);
    for index in range(2, (m // 2) + 1):
        if (((number1 % index) == 0) and ((number2 % index) == 0)):
            return False;            
    return True;
print(relativeprime(16, 21));
print(relativeprime(18, 21));
print();

#8.6
def rotate(list):
    last = list[len(list) - 1];
    for index in range(len(list) - 1, 0, -1):
        list[index] = list[index - 1];
    list[0] = last;
    return list;
print(rotate([1,2,3,4,5]));
print();

#8.7
def nfak(n):
    if (n == 0):
        return 1;
    else:
        return n * nfak(n - 1);        
def binomial(n, k):
    return nfak(n) // (nfak(k) * nfak(n - k));
print(binomial(6, 5));
print();

#8.8
def maclaurin(x):
    sum = 1;
    nom = x;
    den = 1;
    index = 1;
    while (True):
        term = nom / den;
        #print(nom, den, term);
        sum += term;
        if (abs(term) < 1e-7):
            break;
        nom *= x;
        den *= index;
        index += 1;
    return sum;
print(maclaurin(10));
print();

#8.9
def newton(x):
    lastValue = 1;
    while (True):
        newValue = (lastValue + x / lastValue) / 2;
        if (abs(newValue - lastValue) < 1e-6):
            return newValue;
        lastValue = newValue;
print(newton(4));
print(newton(2));
print();

#8.11
def sudoku(matrix):
    list = [];

#8.11
def sort(list):
    return sorted(list, key=len);
print(sort(["abcdef", "abc", "ab", "abcd"]));
print();

#8.12
def fack(year):
    if (year == 1):
        return 25000;
    else:
        return 1.03 * fack(year - 1) + 900;
print(fack(1));
print(fack(2));
print(fack(3));
print();

#8.13
def sgd(m, n):
    if (m == n):
        return m;
    elif (m > n):
        return sgd(m - n, n);
    else:
        return sgd(m, n -m);
print(sgd(12, 16));
print(sgd(16, 12));
print();

