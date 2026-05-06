numbers = [1, 2, 3, 4, 5, 6]
even = filter(lambda x : x % 2 == 0, numbers)
double = map(lambda x : x * 2, even)
print(list(double))    
