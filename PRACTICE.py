# typecasting and identyfying type

'''a=int(input("hii:"))
b=float(a)
print(type(b))'''



# using comaprison operator identity which number is greater
'''a=10
b=20
print(a>b)'''
# find avr of 2 number
'''a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
avg=(a+b)/2
print(avg)'''


# a=int(input("enter the number"))
# print(a*a)
'''s="hello world"
index=s.find("world")
print(index) '''
'''a=input("enter the name:")
print("good afternoon",a)'''


from calendar import c


a="hello i am prasad  achari"
b=a.replace("  "," ")
print(b)


# TUPLE AND LIST
'''fruits=[]
a=input("enter the fruit1: ")
fruits.append(a)
b=input("enter the fruit2: ")
fruits.append(b)
c=input("enter the fruit3: ")
fruits.append(c)
d=input("enter the fruit4: ")
fruits.append(d)
e=input("enter the fruit5: ")
fruits.append(e)
f=input("enter the fruit6: ")
fruits.append(f)
g=input("enter the fruit7: ")
fruits.append(g)
print(fruits)'''


# 2problem


'''marks=[]
a=int(input("enter the marks: "))
marks.append(a)
b=int(input("enter the marks: "))
marks.append(b)
c=int(input("enter the marks: "))
marks.append(c)
d=int(input("enter the marks: "))
marks.append(d)
e=int(input("enter the marks: "))
marks.append(e)
m=int(input("enter the marks: "))
marks.append(m)
print(marks)
marks.sort()
print(marks)'''


# # probl 4

# tuple=(1,2,3,4,0,0,0,0,0,9)
# print(tuple.count(0))

# a=[]
# b=int(input())
# a.append(b)
# c=int(input())
# a.append(c)
# d=int(input())
# a.append(d)
# print(a)
# print({a})


# greatest of 4
'''a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
d=int(input("enter the number"))
if a>b and a>c:
    print("a is greter")
elif b>c and b>d:
    print("b is gret")
elif c>b and c>d:
    print("c is gret")
else:
    print("d is gret")'''



"""marks1=int(input("enter the marks1: "))
marks2=int(input("enter the marks2: "))
marks3=int(input("enter the marks3: "))
total_percentage=((marks1+marks2+marks3)/300*100)
print(total_percentage)
if marks1>=33 and  marks2>=33 and marks3>=33 and total_percentage>=40:
    print("passed")
else:
    print("failed")"""


# finding spams
'''a1="click this"
a2="buy this"
a3="make more money"
a4="subscribe this"
message=input("enter the message: ")
if (a1 in message or a2 in message or a3 in message or a4 in message):
    print("message is spams")
else:
    print("its not a spam")'''

# username contains less then 10 char or not"
'''username=input("enter the username")
if (len(username)<=10):
    print("valid")
else:
    print("invalid") '''

# marks scheme
'''marks=int(input("enter the marks: "))
if (marks>90):
    print("ex")
elif(marks>=80 and marks<=90):
    print("A")
elif(marks>=70 and marks<80):
    print("B")
elif(marks>=60 and marks<70):
    print("C")
elif(marks>=50 and marks<60):
    print("D")
else:
    print("fail")'''

# CONTINUE
'''or i in range(4):
    print("printing")
    if i==2:
        continue
    print(i)'''

    # table for given number
'''i=1
n=int(input("enter the multiplication number:"))
while i<=10:
    print(n,"x", i ,"=",n*i)
    i+=1'''

# another method 
# n=int(input("enter the number: "))
# for i in range(1,11):
#     print(f"{n}X{i}={n*i}")




# greet NameError

'''l=["prasad",'sujan' ,"pallavi","snehal"]
for i in l:
    if i.startswith("s"):
        # print("hello",i)
        print(f"hello {i}")'''

# prime or not
'''n=int(input("entr the number"))
for i in range(2,n):
    if (n%i)==0:
        print("its not a prime")
        break
else:
    print("prime")'''

# first n naturalnnumber
# n=int(input("enter the number"))
# i=1
# sum=0
# while i<=n:
 
#     sum=sum+i
#     i=i+1
# print(sum)



# factorial
'''m=int(input("enter the number"))
fact=1
for i in range(1,m+1):
    fact=fact*i
print(fact)'''

# patterns
'''a=int(input("enter the number"))
for i in range(1,a+1):
    print(" "*(a-i),end="")
    print("*"*(2*i-1),end="")
    print(" ")'''

# 2problem
'''a=4
for i in range(1,a+1):
    print("*"*i)'''
# a//3rd

# n=3
# for i in range(1,n+1):
#     print("*"*i)
#     print()

# rverse multiplication
 
'''n=int(input("ebter the numver"))
for i in range(1,11):
    print(f"{n}X{11-i}={n*(11-i)}")
# '''


# functions
'''def day():
    print("good day")


day()
day()
day()
'''
# \/function with arguments

''''def gooday(name,end):
    print("hello dear" + name)
    print(end)
gooday(" Prasad", " thank you")'''


# problem1
'''def greatest(a=10,b=20,c=7):
    if a>b and a>c:
        print( " a is greater")
    elif b>a and b>c:
        print("b is greater")
    else:
        print("c is greater")
        # a=int(input("enter the number one: "))
        # b=int(input("enter the number two:"))
        # c=int(input("enter the number three: "))
greatest(a=17,b=39,c=88)'''
# or

'''def greatest(a,b,c):
    if (a>b) and (a>c):
        return a
    elif (b>a) and (b>c):
        return b
    else:
        return c
a=1
b=2
c=3
print(greatest(a,b,c))'''

# celsius convert
# def celsius(F):
#     return C = 5*(F-32)/9
#     F=int(input("enter the farennt: "))
# print(celsius(C))
        
'''def f_to_c(f):

    return 5*(f-32)/9
f=int(input("enter the tenp in farenyt: "))
print(f_to_c(f))'''

# sum of n naturalnumber with recursive function
'''
def sum(n):
    if (n==1):
        return 1
    return sum(n-1)+n
print(sum(3))
    '''

# inchtocm
# n=int(input("enter inch"))
# print(n*2.54)

'''def inch_cm(inch):
    return inch*2.54
n=int(input("enter the number in inch: "))
print(f"the num is cms is :{inch_cm(n)}")'''

# file
# st="hii m prasad"
# f=open("file.txt","w")
# f.write(st)
# f.close()


'''f=open("file.txt")
lines=f.readlines()
print(lines,type(lines))
f.close()'''
# readlines list everythingin list and readline displays one sentence and type will b string
'''f=open("file.txt")
line1=f.readline()
print(line1,type(line1))
f.close()'''



# practice set 
f=open("poem.txt","r")
data=f.read()
data.find("twinkle")
if "twinkle" in data:
    print("yes")
else:
    print("no")
f.close()