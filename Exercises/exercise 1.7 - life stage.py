# Exercise 5.6 from Crash Course for Python

age = int(input('What age? : '))

if 0 <= age < 2:
    print('A baby')

elif 2 <= age < 4:
    print('A toddler')

elif age >= 4 and age < 13:
    print('A kid')

elif 13 <= age < 20:
    print('A teenager')

elif age in range(20, 65):
    print('An adult')

elif 65 <= age < 120:
    print('An elder')

else:
    print('Invalid age')
    assert False







# match age:
#     case age if age < 2:
#         print('A baby')
#
#     case age if age < 4:
#         print('A toddler')
#
#     case age if age >= 4 and age < 13:
#         print('A kid')
#
#     case age if 13 <= age < 20:
#         print('A teenager')
#
#     case age if age in range(20, 65):
#         print('An adult')
#
#     case _:
#         print('An elder')




# lijst = [{'bounds': [0, 2], 'stage': 'A baby'},
#          {'bounds': [2, 4], 'stage': 'A toddler'},
#          {'bounds': [4, 12], 'stage': 'A kid'},
#          {'bounds': [13, 20], 'stage': 'A teenager'},
#          {'bounds': [21, 65], 'stage': 'An adult'},
#          {'bounds': [65, 110], 'stage': 'An elder'}]
#
# for d in lijst:
#     lower, upper = d['bounds']
#     if lower <= age < upper:
#         print(d['stage'])
#         break







# lifestages = {'A baby': [0, 2],
#      'A toddler': [2, 4],
#      'A kid': [4, 12],
#      'A teenager': [13, 20],
#      'An adult': [21, 65],
#      'An elder': [65, 110]}
#
# for lifestage, (lower, upper) in lifestages.items():
#     if lower <= age < upper:
#         print(lifestage)
#         break
