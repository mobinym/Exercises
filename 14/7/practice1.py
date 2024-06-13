
def Check_Birth_Date(name,family,birthday):
    split=birthday.split('/')
    years = int(split[0])
    months = int(split[1])
    days = int(split[2])
    
    if years<=1340:
        print(f'Dear {name.capitalize()} {family.capitalize()} You are now eligible to get a COVID-19 vaccination')
    else:
        print(f'Dear {name.capitalize()} {family.capitalize()} You are not eligible to get a COVID-19 vaccination now')
    

name = input('Enter name:')
family = input('Enter Family:')
birthday = input('Enter birthday(ex: 1382/2/5):')
person = (name,family,birthday)
Check_Birth_Date(*person)