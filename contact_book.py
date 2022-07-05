print("Enter the details")
names = []
phone_numbers = []
def contact_store():
    k=1
    while(k):
        name = input("Name: ")
        phone_number = input("Phone Number: ") 
        names.append(name)
        phone_numbers.append(phone_number)
        print("want to continue enter 1 else 0")
        k=int(input())
        

def par_search_name():
    se_it=input("enter character")
    for na in names:
        in_x=names.index(na)
        if(na.__contains__(se_it)):
         print(na,phone_numbers[in_x])

def par_search_num():
    se_it=input("enter number")
    for nu in phone_numbers:
        in_x=names.index(nu)
        if(str(nu).__contains__(se_it)):
          print(nu,names[in_x])

def contact_search():
 search_term = input("\nEnter search term: ")
 if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]
    print("Name: {}, Phone Number: {}".format(search_term, phone_number))

 else:
    print("Name Not Found")

def book_display():
    print("\tBook Details")
    for j in range(len(names)):
     print("{}\t\t\t{}".format(names[j], phone_numbers[j]))

contact_store()

print("want to search enter y")
inp=input()
if(inp=='y'):
    contact_search()
# else:
#  print("thank you")

print("want to dispaly book enter y")
inc=input()
if(inc=='y'):
    book_display()
# else:
#     print("thank you")

print("want to  search name by entering the characters enter y")
in_s=input()
if(in_s=="y"):
  par_search_name()
else:
    print("thank you")

