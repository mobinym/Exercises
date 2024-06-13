shoppingList1 = ["Milk","Cheese","Butter","Tomato","Banana","Apple"] 
shoppingList2 = ["Orange","Cheese","Kiwi","Tomato","Banana","Butter"] 


def check(item1,item2):
    if item1==item2:
        return item1
    
maplist1=list(map(check,shoppingList1,shoppingList2))
list2=[i for i in maplist1 if i!=None]
print(list2)