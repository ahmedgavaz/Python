class MyError(Exception):
    pass


class AgeError(MyError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


# while True:
#     print('Hello')
while True:
    try:
        x = int(input('Enter number '))
        y = 10/x
        if x < 18:
            raise AgeError('Invalid number')
        # print(z)
        # break
    # except (ValueError, ZeroDivisionError):
    except ValueError as e:
        print('Not a valid number. Try again...')
        # print(e)
        # print(e.args)
        # raise ZeroDivisionError
    except ZeroDivisionError:
        print('Zero is not allowed. Try again...')
    except AgeError:
         print('Not a valid age. Try again...')
    # except:
    #     print('Generic error')
    else:
        print('OK')
        break
    finally:
        print('Done')
print(x)
# print(10/0)
