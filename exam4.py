# part1 thank u for ur charity
# p1
# numbers = [10, 20, 30]
# for i in range(len(numbers)):
#     print(i)  #pishem esli xotim chtobi pokazival index
#     print(numbers[i]) #esli nuzhno chtobi pokazal znachenie index-ov vnutri lista


# p2
# x = int(input('raqami mexostagiyatonro vorid kuned: '))


# try:
#     print(100 / x)
# except:
#     if x==0:
#      print ('ba i raqam ne delim')
#     elif x=='abcdefghijklmonp': #i tak dalee
#        print('ish voobche raqam nestay ku')
#     elif x>100:
#        print('a baaachaaa')
# finally:
#     print('javob hami bday')



# p3
# name=input('kiyaaayy?: ')
# if name == "Admin":
#     print("Welcome")
# else:
#     print('ne qabulkaem')


# p4
# import random
# print(random.randint(100, 103)) #just oxir dobavit' kadem 


# p5
# file = open("data.txt", "a") #esli napisat w to to chto bilo udalit 
# file.write("Hello")
 



# part2
# p1 
# stroka=input('vvedite stroku:')
# cnt=0
# with open('file.txt', 'a') as file:
#     file.write(stroka)
#     str=stroka.join('')
#     print(f'количество символов: {len(str)}')



#     st=stroka.split(' ')
#     print(f'количество слов: {len(st)}')


#     cnt=0
#     for s in st: 
#         if s=='eyiuoa':
#             cnt+=1
#             print(cnt)
#     print(f'количество гласных букв: {cnt}')


# print(f'строкa в обратном порядке: {stroka[::-1]}')



# p2
# import random

# lst=[]
# x=random.randint(1,100)
# lst.append(x)
# mx=-9999
# mn=9999
# sum=0
# cnt=0
# for x in lst:
#     if mx<x:
#         mx=x
#         print(f'максимальное число: {mx}')
#     if mn>x:
#         mn=x
#         print(f'минимальное число: {mn}')

# for x in lst:
#     sum+=x
#     print(f'среднее значение: {sum}')

# for x in lst:
#     if x%2==0:
#         cnt+=1
#         print(f'количество чётных чисел: {cnt}')

# print(lst.sort())


    


# p3
# numbers=[]
# numbers=input('enter pack of numbers: ')
# sum=0
# mx=-999
# mn=999
# def analyze(numbers):

#  for n in numbers:
#         sum+=int(n)

# for n in numbers:
#          if mx<int(n):
#            mx=n
#            print(f'максимальный элемент: {mx}')
#          if mn>int(n):
#            mn=n
#            print(f'минимальный элемент: {mn}')


# print(f'суммa элементов: {sum}')
# print(f'среднее значение: {sum/len(numbers)}')




# p4
# name=input('enter student name: ')
# with open('student.txt', 'a') as file:
#     file.write(name)
#     if name=='stop':
#         break

#     file.readlines()
# print(file.readlines())


# p5
# class Student:
#     def __init__(self,name,age,score):
#         self.name=name
#         self.age=age
#         self.score=score

#     def create(self):
#         student = []
#         student.append(st)



#     def show_info(self):
#         return f'''
# name = {self.name}
# age = {self.age}
# score = {self.score}'''
    

#     def increase_score(self,points):
#         self.points=points
#         if self.score<100:
#             self.score+=self.points

#     def is_excellent(self):
#         if self.score<90:
#             return True
#         else:
#             return False

# st=Student()
# n=input('enter info: ')


# while True:
#     if n==1:
#         st.create()
#         name = input('enter name: ')
#         age = int(input('enter age: '))
#         score = int(input('enter score: '))

#     if n==2:
#          st.show_info()

#     if n==3:
#         mx=-999
#         for s in score:
#             if mx<s:
#              print(f'student {name} has highest score')

#     if n==4:
#         sum=0
#         for s in score:
#             sum+=s
#         print(f'средний балл всей группы: {sum/5}')

#     if n==5:
#         break




# p6
# import random,datetime

# x=random.random()
# start=datetime.time() 

# c1=0
# c2=0
# n=int(input('enter ur number: '))
# if n>x:
#     print('Больше')
#     c1+=1
# elif n<x:
#     print('Меньше')
#     c2+=1
# else:
#     finish=datetime.time()
#     print(f'bale, количество попыток: {c1+c2}, время, затраченное на игру: {finish-start}')