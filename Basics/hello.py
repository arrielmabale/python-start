
myName = 'Arriel'
myAge = 40
youngerBrotherAge = 20
youngerBrotherName = 'Boy'


print('Hello, World!')
print('What is your name?')

myInputName = str(input())

if myInputName!='' :
    print('Nice to meet you ' + myInputName)
else:
    print('You seem to be quiet, I am ' + myName)

print('The lenght of yout name is : ')
print(len(myInputName))
print('What is your age?')

myInputAge =  input()
try:
    myInputAge = int(myInputAge)
except ValueError:
    myInputAge = 0

print(type(myInputAge))

if type(myInputAge) !=  int :
    myInputAge =0
    

if myInputAge > 0 :
    print('Your age is ' + str(myInputAge))
    if myInputAge == youngerBrotherAge:
        print('Your the same age as my ' + youngerBrotherName + '!')
    elif myInputAge > youngerBrotherAge: 
        print('You are older than ' + youngerBrotherName)
    else :
        print('you are younger than ' + youngerBrotherName)
else: 
    print('Wow your immortal, my age is ' + str(myAge))

exit()