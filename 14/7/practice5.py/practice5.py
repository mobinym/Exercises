import os
try:
    with open('Homework 7/practice5.py/files_in_python.txt', 'r') as file1:
        content = file1.read()

    content = content.replace('inbuilt', 'built-in')


    with open('Homework 7/practice5.py/NewFolder/files_in_python_edit.txt', 'w') as file2:
        file2.write(content)

    with open('Homework 7/practice5.py/NewFolder/description.txt', 'w') as file3:
        Name = str(os.path.basename('Homework 7/practice5.py/NewFolder/files_in_python_edit.txt')+'\n')
        file3.write(f'FileName: {Name}')
        Size = str(os.path.getsize('Homework 7/practice5.py/NewFolder/files_in_python_edit.txt')//1024)
        file3.write(f'FileSize: {Size}KB')

except Exception as error:
    print('\033[31m'+str(error)+'\033[0m')

else:
    print('\033[32m'+'Done description.txt & files_in_python_edit_txt Created in NewFolder...'+'\033[0m')





























    # str1 = []
    
    # with readfile('Homework 7/practice6.py/files_in_python.txt','r') as file1:
    #     line = file1.readlines()
    #     for i in line:
    #         j=i.split()
    #         for n in j:
    #             if n == 'inbuilt':
    #                 n = 'built-in'
    #             str1.append(n)
                
    # 
    # editfile('files_in_python_edit.txt',str2)

    #     # while file1:
        #     line = file1.readline()
            
        #     if line == 'inbuilt':
        #         flag = True

        #     if line == ' ':
        #         break
            
        #     if flag == True:


