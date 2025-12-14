
#! Global vs local scope

def func1():

    num = 3

    print(num)

num = 10
def func2():

    global num

    double_num = num * 2

    num = 6

    print(double_num)

# func1()
# func2()
# print(num)

#! Functions nested
#* SIN
def mod2plus5 (x1,x2,x3):
    new_x1 =  x1 % 2 + 5
    new_x2 =  x2 % 2 + 5
    new_x3 =  x3 % 2 + 5

    return new_x1,new_x2,new_x3

# print(mod2plus5(1,2,3))

#* CON
def mod2plus5V2 (x1,x2,x3):
    def inner(x):
        return x % 2 + 5
    return inner(x1),inner(x2),inner(x3)

# print(mod2plus5V2(1,2,3))

#! Returning functions

def raise_val(n):
    def inner(x):
        return x ** n
    return inner

square = raise_val(2)
cube = raise_val(3)

# print(square(2))
# print(cube(4))


def outer():
    n = 1
    def inner():
        nonlocal n
        n = 2
        print(n)
    inner()
    print(n)

# outer()

#! Default arguments

def power(number, pow=1):
    return number ** pow

# print(power(2))
# print(power(2,3))


#! Flex arguments
def add_all(*args):
    sum_all = 0
    for num in args :
        sum_all += num
    return sum_all
#Podes llamarlo con cualquier cantidad de argumentos
# print(add_all(1,2,3,4,5))


def print_all(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# print_all(name="Ciro", age=30, city="Buenos Aires")

#! Ejercicio
import os
import pandas as pd

df = pd.read_csv(os.path.join(os.path.dirname(__file__), "src",'tweets.csv'))


def count_entries(df, *args):
    cols_count= {}
    
    for col_name in args:
        col = df[col_name]
        for entry in col:
            if entry in cols_count.keys():
                cols_count[entry] += 1
            else:
                cols_count[entry] = 1
    return cols_count


result1 = count_entries(df,'lang')
result2 = count_entries(df, 'lang', 'source')

print(result1)
print(result2)