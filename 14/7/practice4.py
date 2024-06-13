customer_List = [
    "Sara Ahmadi",
    "Ali Rezaee",
    "Bahar Sadr",
    "Ahmad Majedpoor",
    "Iman Mohammadi",
    "Mina Bavandpoor",
    "Mohammad Alimoradi",
    "Majid Rafiee",
    "Sima Sefidiyan"] 

customer_Special = [
    "Vahid Abdoli",
    "Ali Rezaee",
    "Bahar Sadr",
    "Sima Sefidiyan"] 

def check(customer):
    return customer in customer_List
    
print(list(filter(check,customer_Special)))