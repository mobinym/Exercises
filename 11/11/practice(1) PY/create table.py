from mysql.connector import connect,Error

try:
    with connect(host ='****',user ="****",password ="****",database="****") as db:
        mycurser = db.cursor()
        TABLE='''
        create TABLE T_BOOK(
            BookId int PRIMARY KEY AUTO_INCREMENT,
            Title VARCHAR(200),
            Author VARCHAR(200),
            Publisher VARCHAR(200)
        )
        '''
        mycurser.execute(TABLE)
        db.commit()
        
except Error as error:
    print(error)