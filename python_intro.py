# if 3 > 2:
#     print('It works!')
# if 5 > 2:
#     print('5 is indeed greater than 2')
# else:
#     print('5 is not greater than 2')
# name = input('Jak se jmenujes? ')

def hi(name):
    print('Hi' + name + '!')

    if name == 'Ola':
        print('Hey Ola!')
    elif name == 'Sonja':
        print('Hey Sonja!')
    else:
        print('Hey anonymous!')
hi('Rachel')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']

for name in girls:

    hi(name)
    print('Next girl')

    for i in range(1, 6):
        print(i)

# volume = 10
#
# if volume < 20:
#     print('Je to dost potichu.')
# elif 20 <= volume < 40:
#     print('Jako hudba v pozadi dobre.')
# elif 40 <= volume < 60:
#     print('Skvele, pocujem vsetko paraaadne :)')
# elif 60 <= volume < 80:
#     print('Dobre na party')
# elif 80 <= volume < 100:
#     print('Trochu moc nahlas, nemyslis ;)')
# else:
    # print('Krvacaju mi usi :p')

# def hi ():
#     print('Hi there!')
#     print('How are you?')
# hi()
