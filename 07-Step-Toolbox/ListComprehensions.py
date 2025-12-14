
#* con for

nums  = [12,8,21,3,16]
new_nums = []
for num in nums:
    new_nums.append(num + 1)
# print(new_nums)

#! With list comprehension

# [[expresión de salida] for *variable de iterador* in *iterable*]
new_nums = [num + 1 for num in nums]
# print(new_nums)

#? Ejemplo
pairs_1= [(num1,num2) for num1 in range(2) for num2 in range(6,8)]

# print(pairs_1)

#? Ejemplo 2

matrix = [[col for col in range(5)] for row in range(5)]
# print(matrix)

# ! Advanced comprehension
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
#* Conditionals in comprehensions
new_nums = [num**2 for num in range(10) if num % 2 == 0] 
new_nums = [num**2 if num % 2 == 0 else 0 for num in range(10)]

new_fellowship = [member for member in fellowship if len(member)>= 7]
new_fellowship = [member if len(member)>= 7  else '' for member in fellowship]

#* dict comprehensions
new_dict = {num: -num for num in range(10) }
new_fellowship = {member: len(member) for member in fellowship}


#! Generator expressions

result = (num for num in range(10))
#* no almacena los datos en memoria entonces necesitamos iterar sobre ellos 
for num in result:
    print(num) 
    
even_nums = (num for num in range(10) if num % 2 == 0)
print(list(even_nums))

#! Generators functions
def num_sequence(n):
    i = 0
    while i < n:
        yield i
        i += 1 
        
        
#! Ejercicio Tweets
import os 
import pandas as pd 
df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)),'src', 'tweets.csv'))

tweet_time = df['created_at']

tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']