
import re

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