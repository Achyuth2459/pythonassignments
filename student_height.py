class Student(object):
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def getheight(self):
        return self.height
    
    def __str__(self):
        return self.name.center(10) + ' : ' + str(self.getheight())

st_height={}

def add_student(st_height):
    print("enter name of student")
    na_me=input()
    print("enter height of student")
    he_ght=int(input())
    st_height[na_me]=he_ght    

def display_student(st_height):
    dis=[]
    for i in st_height:
        dis.append(Student(i,st_height[i]))
    print(" Name\t\theight")
    n=1
    for j in dis:
        print(n,j)

def del_student(st_height):
    print("Enter name of student")
    nam=input()
    st_height.pop(nam)

def upd_height(st_height):
    print("Enter name of student")
    nam=input()
    print("enter value to be updated")
    up_h=int(input)
    st_height[nam]=up_h

def ser_student_ht(st_height):
    print("Enter name of student")
    nam=input()
    print(st_height[nam])

flag='0'
while(flag=='0'):
    print("enter 1 for add\nenter 2 for display\nenter 3 for update\nenter 4 for search\nenter 5 for delete")
    while(True):
      num=input()
      if(num=='1'):
       add_student(st_height)
       break
      elif(num=='2'):
       display_student(st_height)
       break
      elif(num=='3'):
       upd_height(st_height)
       break
      elif(num=='4'):
       ser_student_ht(st_height) 
       break
      elif(num=='5'):
       del_student(st_height)
       break
      else:
       print("enter proper digit")
    print("want to continue enter 0 ")
    flag=input()
    