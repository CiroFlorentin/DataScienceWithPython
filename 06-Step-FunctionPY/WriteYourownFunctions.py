
#! Function with single return and params
def square(x):
    return x ** 2
print(square(2))

#! Function with multiple returns and params
def power(x,y):
    value1 = x ** y
    value2 = y ** x
    return value1, value2

print(power(2,3))


#! unpacking
nums=  (3,4,6)

a, b, c = nums

even_nums = (2, b , c)
print(even_nums)


#? Other Example of unpacking
def shout_all(word1 ,word2):
    shout1 = word1 + '!!!'
    shout2 = word2 + '!!!'
    shout_words =(shout1 , shout2)
    return shout_words

yell1 , yell2 = shout_all('congratulations','you')

print(yell1)
print(yell2)

#! Uniting everything

import pandas as pd
import os
df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'src', 'tweets.csv'))

def count_entries(df, col_name):
    langs_count = {}
    for entry in df[col_name]:
        if entry in langs_count:
            langs_count[entry] += 1
        else:
            langs_count[entry] = 1
    return langs_count

result = count_entries(df, 'lang')
print(result)