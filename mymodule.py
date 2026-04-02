#Difference between MOdule/library/package

'''def greetings(name):
    print("welcome",name)'''

'''a=3
b=8
print("the sum is",a+b)'''


'''Details={"idnos":[10,20,30],
         "names":["harika","taruni","simhadri"],
         "cities":["vja","hyd","vzg"]}'''

'''if __name__=="__main__":
    a=[10,20,30,40,50]
    #a.append("code")
    a.extend("code")
    print(a)'''

'''def dummy():
    if __name__=="__main__":
        print("This program is run as script")
    else:
        print("This program is run as module")
dummy()'''

#random module

'''import random
a=random.sample(range(10,30),5)
print(a)'''

#randint()
'''import random
a=random.randint(40,60)
print(a)'''


#choice()
'''import random
b=[10,20,30,40,50,60]
a=random.choice(b)
print(b)'''


#task Dice code
'''while True:
    import random
    a=int(input("enter the roll of Dice"))
    b=random.randint(1,6)
    print(b)
    options=input("Roll again? (y/n)")
                  
    if options=="y":
        continue
    elif options=="n":
        break
    else:
        print("Invalid option")'''

#calendar
'''import calendar
year=2026
month=4
print(calendar.month(year,month))'''


'''import calendar
year=2027
print(calendar.calendar(year))'''


'''import calendar
year=int(input("Enter the year"))
month=int(input("enter the month"))
print(calendar.month(year,month))'''


#Date&time

'''from datetime import date
a=date.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()
print(a)'''

'''import time
a=time.time()
print(a) #epoch time

b=time.localtime(a)
print(b)'''

'''import time
a=time.time()
b=time.localtime(a)
print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")'''


'''import time
a=time.time()
b=time.localtime(a)
print(f"Now time is {b.tm_hour}:{b.tm_min}:{b.tm_sec}")'''

'''import time
a=time.time()
b=time.localtime(a)
print(f"day is {b.tm_wday}-{b.tm_yday}-{b.tm_isdst}")'''






        




