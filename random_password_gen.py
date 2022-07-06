import random
import string

def get_random_password(num):
    random_source = string.ascii_letters + string.digits + string.punctuation
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
    if(num>4):
     for i in range(num-4):
        password += random.choice(random_source)
    password_list = list(password)
    # shuffle all characters
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password

print("Enter the length of the password needed")
num=int(input())
if(num<=0):
  print("please enter a positive number")
  num=int(input())
if(num>0):
 res=get_random_password(num)
 for i in range(num):
    print(res[i],end='')
 print("\n")

