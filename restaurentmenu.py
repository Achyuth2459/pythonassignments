class Food(object):
    def __init__(self,name,price):
        self.name = name
        self.price=price
        
    
    def getprice(self):
        return self.price
    
    def __str__(self):
        return self.name + ' : ' + self.getprice()
  
# Defining a function for building a Menu 
# which generates list of Food    
def menu_display(names,costs):
    menu=[]
    for i in names:
        lst=[]
        for j,k in zip(names[i],costs[i]):
            lst.append(Food(j,k))
        menu.append(lst)
    k=1
    for i in menu:
        n = 1

        if(k==1):
            print("starters")
        elif(k==2):
            print("side dishes")
        elif(k==3):
            print("Main dishes")
        else:
            print("deserts")
        for el in i:
            print(n,'. ', el)
            n = n + 1
        k=k+1

def add_menu(names,costs):
    print("enter item type")
    item_type=input()
    print("enter item price")
    price=input()
    print("enter item to be added")
    item_add=input()
    names[item_type].append(item_add)
    costs[item_type].append(price)

def menuitem_delete(names,costs):
    print("enter item type")
    item_type=input()
    print("enter item to be del")
    item_del=input()
    names[item_type].remove(item_del)
    costs[item_type].remove(item_del)

def update_menu(names,costs):
    print("enter item type")
    item_type=input()
    print("enter item for its price updated")
    item_p=input()
    print("enter price to be updated")
    new_p=input()
    ind=names[item_type].index(item_p)
    costs[item_type][ind]=new_p

def search_menu(names,costs):
    i

# items
names = {"starters":["springrolls","french onion soup","salads","tomato soup"],"side dishes":["mixed green salad"
,           "garden vegetable","french fries","garlic bread"],"main dishes":["chicken birayani","mutton biryani","fish fry",
            "mushrooom"],"deserts":["venilla ice cream","fruit salad","chocolate cake","cool drinks"] }
# prices
costs = {"starters":["Rs100","Rs150","Rs200","Rs120"],"side dishes":["Rs140","Rs130","Rs130","Rs150"],
         "main dishes":["Rs300","Rs450","Rs200","Rs220"],"deserts":["Rs140","Rs130","Rs130","Rs150"]}

flag='0'
while(flag):
    print("enter 1 for display\nenter 2 for add\nenter 3 for delete\nenter 4 for update")
    num=input()
    if(num=='1' or num =='2' or num =='3' or num =='4'):
     pass
    else:
     print("enter proper digit")
    num=input()
    if(num=='1'):
     menu_display(names,costs)
    elif(num=='2'):
     add_menu(names,costs)
    elif(num=='3'):
     menuitem_delete(names,costs) 
    else:
        update_menu(names,costs)
    print("want to continue enter 0 ")
    flag=input()
    


