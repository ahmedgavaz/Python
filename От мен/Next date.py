class MyError(Exception):
    pass

class Err(MyError):
    def __init__(self,message):
        self.message=message
    def __str__(self):
        return self.message
while True:
    try:
        year=int(input("Input year:"))
        month=int(input("Input month:"))
        day=int(input("Input day:"))
        if (month>12) or ((month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) and (day>31)) or ((month==4 or month==6 or month==9 or month==11) and (day>30)) or ((year % 4==0) and (month==2) and (day>29)) or ((year % 4>0) and (month==2) and (day>29)):
            raise Err("Not a Valid date. Try again...")
    except ValueError:
        print("Date must be inputed with numbers")
    except Err:
        print("Not a Valid date. Try again...")
    else:
        break
if ((month==1 or month==3 or month==5 or month==7 or month==8 or month==10) and (day==31)) or ((month==4 or month==6 or month==9 or month==11) and (day==30)) or ((year % 4==0) and (month==2) and (day==29)) or ((year % 4>0) and (month==2) and (day==29)):
        month=month+1
        day=1
elif (month==12 and day==31):
    year= year+1
    month=1
    day=1
else:
    day=day+1
print("The next date is [yyyy-mm-dd]",year,"-",month,"-",day)    
    
    


