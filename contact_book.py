#print("How many numbers you want to store")
names = []
phone_numbers = []
i=1

def contact_store():
    k=1
    while(k):
        name = input("Name: ")
        phone_number = input("Phone Number: ") 
        names.append(name)
        phone_numbers.append(phone_number)
        print("want to continue enter 1 else 0")
        k=int(input())
        i=k

def contact_search():
 search_term = input("\nEnter search term: ")
 if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]
    print("Name: {}, Phone Number: {}".format(search_term, phone_number))

 else:
    print("Name Not Found")

def book_display():
    print("\t\tBook Details")
    for j in range(i):
     print("{}\t\t\t{}".format(names[j], phone_numbers[j]))

contact_store()

print("want to search enter y")
inp=input()
if(inp=='y'):
    contact_search()

print("want to dispaly book enter y")
inc=input()
if(inc=='y'):
    book_display()

