class MyError(Exception):
    pass


class NumError(MyError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
while True:
    try:
        x=float(input("Celsius(minimum is 273.15)="))
        if x<-273.15:
            raise NumError("Invalid number")
    except ValueError:
        print("Not a number")
    except TypeError:
        print("Not a number")
    except NumError:
        print("The number is out of range")
    else:
        break
y=x*1.8+32
print("Fahrenheit= ",y)
    
        
