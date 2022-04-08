class MyError(Exception):
    pass
class AgeError(MyError):
    pass

while True:
    try:
        x = int(input('Enter number '))
        y = 10/x
        if x < 18:
            raise AgeError('Invalid number')
    except ValueError:
        print('Not a valid number. Try again...')
    except ZeroDivisionError:
        print('Zero is not allowed. Try again...')
    except AgeError:
         print('Not a valid age. Try again...')
    else:
        print('OK')
        break
   # finally:
     #   print('Done')
print(x)
# print(10/0)
