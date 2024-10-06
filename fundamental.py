
import re
import math

def add_numbers(num1, num2):
    sum = num1 + num2
    return sum

print(add_numbers(5,7))

def is_even(num):
    if(num % 2)==0:
        return True
    else:
        return False

print(is_even(11)) 

def reverse_string(text):
    reverse = text[::-1]
    return reverse

print(reverse_string("annah wanjiru"))

def count_vowels(text):
    vowels = r'[aeiouAEIOU]'
    count = len(re.findall(vowels, text))
    return count

print(count_vowels("Annah"))

def calculate_factorial(num):
    return math.factorial(num)

print(calculate_factorial(23))


def  apply_decorator(func):
    def wrapper():
        func()
        print("Original function")
    return wrapper

def decorator_func():
    print("Decorator Applied")

decorator_func = apply_decorator(decorator_func)
decorator_func()    

tuples_list = [("Benard Mutemi", 35), ("Annah Wanjiru", 31), ("Dibarl Muuo", 7), ("Megah Mutanu", 4)]

def sort_by_age(tuple_age):
    return tuple_age[1]

tuples_list.sort(key = sort_by_age)
print(tuples_list)

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict

merged = merge_dicts(dict1, dict2)
print("Merged List", merged)


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Information: {self.year} {self.make} {self.model}")

# Example usage
my_car = Car("VW", "Golf", 2015)
my_car.display_info()

