add = lambda a,b: a+b
sub = lambda a,b: a-b
print("Addition:",add(5,6))
print("Substract:", sub(6,4))
List = [1,2,4,8,5,6]
even_numbers = list(filter(lambda x: x % 2 == 0, List))

print(even_numbers)