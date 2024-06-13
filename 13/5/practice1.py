class My_Exception_Handeling(Exception):
    def __init__(self,message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"Error: {self.message}..."
#--------------------------------------------------------------
class Player_selection:
    def __init__(self,code,age,height,weight):
        self.code=code
        self.age=age
        self.height=height
        self.weight=weight

    def age_validation(self):      
        if not 15<=self.age<=35:
            raise My_Exception_Handeling('Age out of range This person is not allowed to register')

    def weight_validation(self):
        if 15<=self.age<=25:
            if not 60<=self.weight<=80:
                raise My_Exception_Handeling("weight out of range This person is not allowed to register")
        elif 25<self.age<=35:
            if not 50<=self.weight<=75:
                raise My_Exception_Handeling('Weight out of range This person is not allowed to register')
        
    def height_validation(self):
        if not 170<=self.height<=190 or self.height=='':
            raise My_Exception_Handeling('height out of range This person is not allowed to register')


    def regiter_player(self):
        try:
            self.code = int(self.code)
        except:
            raise My_Exception_Handeling('Code should be an integer value ')
        try:
            self.age = int(self.age)
        except:
            raise My_Exception_Handeling('Age is not valid')
        try:
            self.weight = float(self.weight)
        except:
            raise My_Exception_Handeling('Weight is not valid')
        try:
            self.height = int(self.height)
        except:
            raise My_Exception_Handeling('Height is not valid')
        self.age_validation()
        self.height_validation()
        self.weight_validation()
        return f'Code is: {self.code}, Age is: {self.age} , Height is: {self.height}, Weight is: {self.weight}'

#-----------------main program------------------------------------------------------
accept_players=[]
while True:
    code =input('Enter Code(Enter 0 to Exit and print list):')
    if code == '0':
        break
    age=input('Enter Age:')
    height=input('Enter Height in cm:')
    weight=input('Enter Weight in kg:')
    

    
    player = Player_selection(code,age,height,weight)
    try:
        accept_players.append(player.regiter_player())
    except My_Exception_Handeling as Error:
        print(Error)

for person in accept_players:
    print(person)