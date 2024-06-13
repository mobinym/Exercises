import re
try:
    with open('practice1/information.txt' , 'r') as file1:
        read = file1.read()

        
        res = re.findall(r'Name:(\w.*).+Family:(\w.*).+Mobile:(0912\d*),.+Code:(\d{10}),.+(Tehran).+\s',read)

        with open('practice1/F3.csv','w') as f1:
            f1.write('Name,Family,Mobile,Postal_Code,City\n')
            for item in res:
                f1.write(f"{item[0]},{item[1]},{item[2]},{item[3]},{item[4]}\n")
        
except Exception as error:
    print('\033[31m'+str(error)+'\033[0m')

else:
    print('\033[32m'+'Done F3.csv Created ... '+'\033[0m')