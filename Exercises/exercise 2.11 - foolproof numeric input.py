import logging

logging.basicConfig(filename = None,   # 'example.log',
                    format = '%(levelname)s %(asctime)s %(message)s',
                    level = logging.WARNING)

class OutOfBoundsException(Exception):
    pass
    
    
def foolproof_input(prompt, lower, upper):

    while True:
        try:
            response = input(prompt)
            number = int(response)

            if lower <= number <= upper:
                return number
            else:
                raise OutOfBoundsException(f'{number} is not between {lower} and {upper}.')

        except ValueError:
            logging.info(f'"{response}" is not a number.')

        except OutOfBoundsException as ex:
            logging.info(ex)

        except KeyboardInterrupt:
            print('\nOK. Stoping now.')
            break
        


# ----------------------------------------------------------------

if __name__ == '__main__':

    number = foolproof_input('Give me a number between 1 and 10: ', 1, 10)

    if number is not None:
        print('The number you entered (%d) is OK' % number)
