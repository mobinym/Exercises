from mysql.connector import connect,Error
                
def Record():
    try:
        #The fields must be completed
        with connect(host ='****',user ="****",password ="****",database="****") as db:
            mycurser = db.cursor()
            Title = input('Enter Title : ')
            Author = input('Enter Author : ')
            Publisher = input('Enter Publisher : ')
            mycurser.execute(f"INSERT INTO T_BOOK(Title,Author,Publisher) VALUES('{Title}','{Author}','{Publisher}') ")
            print('Book Successfully Insert...')
            db.commit()
            
    except Error as error:
        print(error)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# The fields must be completed
db = connect(host ='******',user ="****",password ="****",database="****") 
mycurser = db.cursor()
#for delete item in database
def Delete():
    try:
        bookid = int(input("Enter BookId to Delete book : "))
        mycurser.execute(f'DELETE FROM T_BOOK WHERE BOOKID = {bookid}')
        print("Delete Successfully...")
        db.commit()
    except Error as error:
        print(error)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#for search item in database by id
def Search_by_id():
    try:
        bookid = int(input('Enter Book ID for Search : '))
        mycurser.execute(f"SELECT * FROM T_BOOK WHERE BOOKID = {bookid}")
        res = mycurser.fetchall()
        if res == []:
            print('not found')
        else:
            print(res)
    except Error as error:
        print(error)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#show all item in database
def Search_All():
    try:
        mycurser.execute(f"SELECT * FROM T_BOOK")
        res = mycurser.fetchall()
        if res == []:
            print('Nothing...')
        else:
            for i in res:
                print(i)
    except Error as error:
        print(error)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
NUMBER = int(input("Enter num(1-4) '1.insert , 2.Delete , 3.search with id , 4.show all' : "))

if NUMBER == 1 :
    Record()
if NUMBER == 2 :
    Delete()
if NUMBER == 3:
    Search_by_id()
if NUMBER == 4:
    Search_All()
#-----------------------------------------------------------------------------------------------------------------------------------------------------