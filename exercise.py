# hg ot jes


# name=["narath","phearak","nisai"]
# condition=True
# while condition:
#     listname=str(input())
#     for n in range(len(name)):
#         if listname==name[n]:
#             print("finished!")
#             condition=False



# asdfghj
# dic={ 
#   1:"seavy",
#   2:23,
#   3:"PNC",
#   4:True
# }
# array=dic.values()
# print(array)
# for item in array:
#   print(item)
# diccopy=dic.copy()
# diccopy[5]="a"
# print(diccopy)
# a=dic.get(3)
# print(a)
# studentsDictionary = eval(input())
# newStudentsNumber= int(input())
# newStudentsClass = input()
# studentsDiccopy=studentsDictionary.copy()
# condition=True
# for item in studentsDictionary:
#   if condition:
#     if newStudentsClass!=item:   
#       studentsDiccopy[str(newStudentsClass)]=newStudentsNumber
#     else:
#       studentsDiccopy[newStudentsClass]=studentsDiccopy[newStudentsClass]+newStudentsNumber
#       condition=False
# for item in studentsDiccopy:
#     print("Class",item,"has",studentsDiccopy[item],"students")



# studentsDictionary1 = {"2021A": 20, "2021B": 30, "2021C": 15,"2021D":23}
# studentsDictionary2 = {"2021A": 20, "2021B": 30, "2021C": 15}
# studentsDiccopy=studentsDictionary1.copy()
# for item in studentsDictionary1:
#   # if  studentsDictionary1[item]==studentsDictionary2[item]:
#   #   studentsDiccopy[item]=studentsDiccopy[item]+studentsDictionary2[item]
#   if studentsDictionary1[item]!=studentsDictionary2[item]:
#     studentsDiccopy[studentsDictionary1.keys()]=str(studentsDictionary1.values())
# print(studentsDiccopy)


#studentsDic1 = {"2021A": 20, "2021B": 30, "2021C": 15}
# studentsDic2 = {"2021A": 20, "2021B": 30, "2021C": 15, "2021D": 34}
# studentresult={}
# for key in studentsDic1:
#   for key in studentsDic2:
#     if studentsDic1[key] == studentsDic2[key]:
#        studentresult=studentsDic1[key]+studentsDic2[key]
#     elif studentsDic1[key] not in studentsDic2[key]:
#       studentsresult=studentsDic1[key]
#     elif studentsDic2[key] not in studentsDic1[key]:
#       studentsresult=studentsDic2[key]
# print(studentresult)
# *
# studentsDictionary = {"2021A": 20, "2021B": 30, "2021C": 15}
# newStudentsNumber= 21
# newStudentsClass = "2021A"
# # for key in studentsDictionary:
# #   if newStudentsClass in key:
# #     studentsDictionary[key]+=newStudentsNumber
# #   else:
# #     studentsDictionary=newStudentsClass[newStudentsNumber]
# print(studentsDictionary[str(newStudentsClass)]=newStudentsNumber)
# for y in range(5):
#   for x in range(5):
#     print(0,end=" ",)
#   print()


#-------week1-------#


# monday
# ex1

# word=str(input())
# word=word.upper()
# counta=0
# for n in range(len(word)):
#   if word[n]=="A":
#     counta+=1
#   else:
#     counta+=0
# print("The number of A is :",counta)

# ex2:

# word=str(input())
# word=word.upper()
# counta=0
# for n in range(len(word)):
#   if word[n]=="A":
#     counta+=1
#   else:
#     counta+=0
# if counta>0:
#   print("GOOD")
# else:
#   print("BAD")


# tuesday
# ex1
# word=str(input())
# word=word.upper()
# counta=0
# countb=0
# for n in range(len(word)):
#   if word[n]=="A":
#     counta+=1
#   if word[n]=="B":
#     countb+=1
# if counta==2 and countb==2:
#   print("WELL DONE")
# else:
#   print("LOST")


# ex2:
# word=str(input())
# word=word.upper()
# countnota=0
# for n in range(len(word)):
#   if word[n]!="A":
#     countnota+=1
# if countnota>0:
#   print("LOST")
# else:
#   print("WELL DONE")


# ex3:
# word=str(input())
# word=word.upper()
# counta=0
# countb=0
# for n in range(len(word)):
#   if word[n]=="A":
#     counta+=1
#   if word[n]=="B":
#     countb+=1
# if counta > countb:
#   print("WELL DONE")
# else:
#   print("LOST")


# wednesday

# ex1:
# word1=str(input())
# word2=str(input())
# word3=str(input())
# if len(word1)>len(word2) and len(word1)>len(word3):
#   print("The greatet word is:",word1)
# if len(word2)>len(word3) and len(word2)>len(word1):
#   print("The greatet word is:",word2)
# if len(word3)>len(word2) and len(word3)>len(word1):
#   print("The greatet word is:",word3)


# ex2:
# word=str(input())
# lenword=len(word)
# space=0
# for n in range(lenword):
#   if word[n]==" ":
#     space+=1
# print("The number of letters is:",lenword-space)


# tuesday
# ex1
# number=int(input())
# if number%2==0:
#   print("This number is even")
# else:
#   print("This number is odd")

# ex2
# number=int(input())
# positivenumber=0
# for n in range(number):
#   if n%2==0:
#     positivenumber+=n
# print(positivenumber)

# # friday
# number=int(input("numberofvalues:"))
# odd=0
# for n in range(number):
#   numberofvalues=int(input(">"))
#   if numberofvalues%2!=0:
#     odd+=1
# print(odd)

#-------week2-------#
# # monday
# # ex1
# # ចាប់យកតែindex​ ដំបូងបើវាមានលេង 7 ពីរ
# number=int(input(">Number of values:"))
# fount7=""
# condition=True
# for n in range(number):
#   numberofvalues=int(input(">"))
#   if condition:
#     if numberofvalues==7:
#       fount7=n
#       condition=False
# if fount7:
#   print("7 index is:",fount7)
# else:
#   print("No 7 intered")

# tuesday

# number=int(input(">number of values:"))
# n1=''
# n2=''
# countgreater=0
# for n in range(number):
#   numberofvalues=int(input(">"))
#   n1=numberofvalues
#   if n>=1 and  n1>n2:
#     countgreater+=1
#   if n>=0:
#     n2=n1
# print(">result is :",countgreater)


# wednesday
# n1=int(input())
# n2=int(input())
# n3=int(input())
# if n1+1==n2 and n2+1== n3: 
#   print("SEQUENCE")
# else:
#   print("NOT SEQUENCE")
# not yet complete
# number=int(input(">number of values:"))
# n1=""
# n2=""
# n3=""
# countofsequence=0
# for n in range(number):
#   nofva=int(input(">"))
#   if n>1:
#     n1=n2
#   if n>0:
#     n2=n3
#   n3=nofva
#   if n >=2 and  n1 + 1==n2 and n2 + 1 ==n3:
#     countofsequence=+1
# print(countofsequence)



# # practice:::**********#

# #array
# students=[
#     ["ronan","ogor"],
#     ["mengheang","pho"],
#     ["sreyaem","hourn"]
# ]
# firstname=input()
# isfound=False
# result=""
# #   firstway
# for item in students:
#   if not isfound and  item[0]==firstname:
#     result=item[1]
#     isfound=True
# if isfound:
#   print(result)
# else:
#   print("not found!")

# #  second way
# for item in students:
#   if not isfound:
#     if item[0]==firstname:
#       result=item[1]
#       isfound=True  
#     else:
#       result="not found!"
# print(result)

# #  third way
# result="not found!"
# for item in students:
#   if not isfound:
#     if item[0]==firstname:
#       result=item[1]
#       isfound=True  
# print(result)


# #dict

# fruits = {
#     "mango" : ["yellow", 3000],
#     "banana" : ["yellow", 500],
#     "apple" : ["green", 1000],
# }
# fruitName = input("enter fruitname: ")
# fruit=fruits[fruitName]
# color =fruit [0]
# price= fruit[1]
# print(color)
# print(price)
  # ** prepare final **
# # 1
# # replace array
# array2D=eval(input())
# for item in array2D:
#   for n in range(len(item)):
#     if item[n]==7:
#       item.remove(item[n])
#       item.insert(n,8)
# print(array2D)
# second way
# array2D=eval(input())
# for n in range(len(array2D)):
#   for i in range(len(array2D[n])):
#     if array2D[n][i]==7:
#       array2D[n][i]=8
# print(array2D)
# 2
# compare2 array
# def isEqual(array1, array2):
#     #write your code here
#     if len(array1)!=len(array2):
#         return False
#     else:
#         lenarray=0
#         for n in range(len(array1)):
#             if array1[n]==array2[n]:
#                 lenarray+=1
#         if len(array1) == lenarray:
#             return True
#         else:
#             return False
    
# #input:
# array1 = eval(input())
# array2 = eval(input())

# #call your function here
# if isEqual(array1, array2)==True:
#     print("EQUAL")
# else:
#     print("NOT EQUAL")

# 3
# + taem 1 1
# originalArray=eval(input())
# newArray=[]
# for item in originalArray:
#   newArray.append(item+1)
# print(newArray)

# 4
# found8
# def numberOfEight(array):
#     # Enter your code here:
#     found8=0
#     for n in range(len(array)):
#         if array[n]==8:
#             found8+=1
#     if found8>0:
#         return found8
#     else:
#         return "NOT FOUND"
    
    
# #Enter your code here:
# array=eval(input())
# print(numberOfEight(array))


# 5
# ??????
# studentsDictionary = eval(input())
# newStudentsNumber= int(input())
# newStudentsClass = input()
# # Enter your code here. Read input from STDIN. Print output to STDOUT
# if  newStudentsClass in studentsDictionary:
#   studentsDictionary[newStudentsClass]+=newStudentsNumber
# else:
#   studentsDictionary[newStudentsClass]=newStudentsNumber
# for key in studentsDictionary:
#   print("Class "+str(key)+" has "+str(studentsDictionary[key])+ " students")



# #add star
# R0w=int(input("Row:"))
# COl=int(input("Col:"))
# array=[]
# for row in range(R0w):
#   array.append([])
#   for col in range(COl):
#     array[row].append("*")
# # print star
# count=0
# while count<4:
#   count+=1
#   x=int(input("X:"))
#   y=int(input("Y:"))
#   symbol=str(input("symbol:"))
#   array[x][y]=symbol
#   result=""
#   for item in array:
#     for n in item:
#       result+=n+" "
#     result+="\n"
#   print(result)

# students = [
#     ["Bunthoeun", 98],
#     ["Sophea", 95],
#     ["Dyna", 25],
#     ["Chanthy", 60],
# ]
# bestStudents=[]
# goodStudents=[]
# for n in range(len(students)):
#   if students[n][1]>75:
#     bestStudents.append(students[n][0])
#     bestStudents.append(students[n][1])
#   else:
#     goodStudents.append(students[n][0])
#     goodStudents.append(students[n][1])

# print("Best students : ", bestStudents)
# print("Good students : ", goodStudents)



##### find odd and even in array
# array=eval(input())
# even=[]
# odd=[]
# for i in array:
#   if i%2==0:
#     even.append(i)
#   else:
#     odd.append(i)
# print("Even is ",even)
# print("Odd is ",odd)



# hospital:
# def getHospitalForNewPatient(maxBedsPerHospital, personnsPerHospital):
#     # Your function code here !
#     for index in maxBedsPerHospital:
#         if maxBedsPerHospital[index] != len(personnsPerHospital[index]):
#             return index
#     return None

# # MAIN
# persons = eval(input())
# maxBedsPerHospital = eval(input())
# personnsPerHospital = {}

# # Your main code here !
# for index in maxBedsPerHospital:
#     personnsPerHospital[index]=[]
# for person in persons:
#     personnsPerHospital[getHospitalForNewPatient(maxBedsPerHospital,personnsPerHospital)].append(person)

# print(personnsPerHospital)





studentsData = [{"name": "Bunthoeun", "score": 90}, {"name": "Kunthy", "score": 35}, {"name": "Sreymom", "score": 95}]
score=[]
name=[]
maxscore=""
beststu=""
score75up=0
if len(studentsData)==0:
  print("No result")
else:
  for dic in studentsData:
    for key in dic:
      if key =="name":
        name.append(dic[key])
      if key=="score":
        score.append(dic[key])
      if dic[key]>=75:
        score75up+=1
  result="All students have more than 75"
  maxscore=(max(score))
  for n in range(len(score)):
    if score[n]==maxscore:
      beststu=name[n]
  if  score75up==len(score):
    print("The best student is "+beststu+"\n"+result)
  else:
    print("The best student is "+beststu)