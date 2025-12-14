
#! Funciones lambda

raise_to_power = lambda x, y: x ** y

# print(raise_to_power(2, 3))

#? Ejemplo
nums = [48,6,9,21,1]

square_all = list(map(lambda num: num ** 2, nums))  # map(func,seq)

print(square_all)

#! Filter

fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

result = filter (lambda member: len(member) > 6, fellowship)
print(list(result))


#? Ejemplo 2

from functools import reduce

#* antes
# def gibberish(*args):

#     """Concatenate strings in *args together."""

#     hodgepodge = ''

#     for word in args:

#         hodgepodge += word

#     return hodgepodge

#* Con lambda y reduce
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

result = reduce ( lambda item1, item2: item1 + item2, stark)
print(result)

#! Try Catch

def sqrt(x):
    try:
        return x ** 0.5
    except Exception as e:
        print("X must be an int or float")

print(sqrt(4))
print(sqrt('hola'))


#! Raise

def shout_echo(word1, echo=1):
    if echo < 0:
        raise ValueError('echo must be greater than or equal to 0')
    echo_word = word1 * echo
    shout_word = echo_word + '!!!'
    return shout_word


shout_echo("particle", echo=5)

shout_echo("particle", echo=-5)
