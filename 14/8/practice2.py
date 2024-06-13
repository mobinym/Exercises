import json

class Food_Menu:
    def __init__(self,foodCode,foodName,foodPrice):
        self.foodCode = foodCode
        self.foodName = foodName
        self.foodPrice = foodPrice
        self.content = []

    def __str__(self):
        return f'foodCode is:{self.foodCode}\t foodName is: {self.foodName}\t foodPrice is: {self.foodPrice}\t content is: {self.content}'

    def add(self,content):
        self.content.append(content)
#---------------------------main program----------------------------------------------
food_list = []
f1 = Food_Menu(1, 'Pizza', 180000)
f1.add('Pepperoni')
f1.add('Cheese')
f1.add('Tomato sauce')
food_list.append(f1.__dict__)

f2 = Food_Menu(2, 'Burger', 150000)
f2.add('Beef patty')
f2.add('Lettuce')
f2.add('Tomato')
f2.add('Cheese')
food_list.append(f2.__dict__)

f3 = Food_Menu(3, 'Pasta', 120000)
f3.add('Spaghetti')
f3.add('Tomato sauce')
f3.add('Meatballs')
food_list.append(f3.__dict__)

f4 = Food_Menu(4, 'Sushi', 200000)
f4.add('Rice')
f4.add('Salmon')
f4.add('Avocado')
food_list.append(f4.__dict__)

f5 = Food_Menu(5, 'Taco', 100000)
f5.add('Tortilla')
f5.add('Beef')
f5.add('Cheese')
f5.add('Salsa')
food_list.append(f5.__dict__)

f6 = Food_Menu(6, 'Salad', 90000)
f6.add('Lettuce')
f6.add('Tomato')
f6.add('Cucumber')
f6.add('Carrots')
food_list.append(f6.__dict__)

f7 = Food_Menu(7, 'Fried Rice', 80000)
f7.add('Rice')
f7.add('Egg')
f7.add('Peas')
f7.add('Carrots')
food_list.append(f7.__dict__)

f8 = Food_Menu(8, 'Sandwich', 70000)
f8.add('Bread')
f8.add('Ham')
f8.add('Cheese')
f8.add('Lettuce')
food_list.append(f8.__dict__)

f9 = Food_Menu(9, 'Stir Fry', 60000)
f9.add('Noodles')
f9.add('Chicken')
f9.add('Broccoli')     
f9.add('Carrots')
food_list.append(f9.__dict__)

f10 = Food_Menu(10, 'Soup', 50000)
f10.add('Chicken broth')
f10.add('Noodles')
f10.add('Carrots')
food_list.append(f10.__dict__)

for i in food_list:
    print(i)

with open('Homework 8/FoodMenu.json','w') as file1:
    json.dump(food_list,file1,indent=4)   

    