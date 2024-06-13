from abc import ABC,abstractmethod

class Participants(ABC):
    def __init__(self,name,family,National_Code,Field_Study,address):
        self.__name = name
        self.__family = family
        self._National_Code = National_Code
        self.__Field_Study = Field_Study
        self.__address = address

    def getname(self):
        return f'{self.__name} {self.__family}' 
    
    def setname(self,newname):
        self.__name=newname
        
    @abstractmethod
    def Calculate_the_final_score(self):
        pass

#____________________________________________________________________________________________
class FreeParticipant(Participants):
    def __init__(self,name,family,National_Code,Field_Study,address,Interview_score,Written_test_score):
        super().__init__(name,family,National_Code,Field_Study,address)
        self.__Interview_score = Interview_score
        self.__Written_test_score = Written_test_score

    def Calculate_the_final_score(self):
        if self.__Interview_score > 100 or self.__Written_test_score > 100:
            return 'invalid score ... '
        else:
            return (self.__Interview_score + self.__Written_test_score) / 2

    
#____________________________________________________________________________________________
class eliteLearned(Participants):
    def __init__(self,name,family,National_Code,Field_Study,address,UniversityRank,averageGrade):
        super().__init__(name,family,National_Code,Field_Study,address)
        self.__UniversityRank= UniversityRank
        self.__Averagegrade = averageGrade

    def Calculate_the_final_score(self):
        score_university = 0
        if self.__UniversityRank == 1:
            score_university=100
        elif self.__UniversityRank == 2:
            score_university=80
        elif self.__UniversityRank == 3:
            score_university=60
       
        average = 0

        if 16<= self.__Averagegrade<=17.5:
            average = 60 

        elif 17.5<self.__Averagegrade<=18.5:
            average = 80

        elif 18.5<self.__Averagegrade<=20:
            average = 100

        else:
            return 'average not valid...'
            
        

        return(average + score_university)/2
  
#____________________________________________________________________________________________


class organizationEmployee(Participants):
    def __init__(self,name,family,National_Code,Field_Study,address,work_experience,Performance_rating_list):
        super().__init__(name,family,National_Code,Field_Study,address)
        self.__work_experience = work_experience
        self.__Performance_rating_list = Performance_rating_list

    def Calculate_the_final_score(self):
        
        average_Performance_List = sum(self.__Performance_rating_list)/len(self.__Performance_rating_list)
        
        
        work_Experience=0
        
        if 1<=self.__work_experience<=5:
            workExperience=0.1
            
        elif self.__work_experience>5:
            workExperience= 0.2
        else:
            return 'Work experience should be more than one year...'

        return average_Performance_List +(workExperience*average_Performance_List )

 
#_____________________________________main program _______________________________________________________

t1 = FreeParticipant('Ali','Rezaii',1230456,'Computer','Tehran',50,100)
print(f't1 Final Score is : {t1.getname()} {t1.Calculate_the_final_score()}')

t2 = eliteLearned('Hossein','Ramezani',12546566,'Zist','Arak',2,19)
print(f't2 Final Score is : {t2.getname()} {t2.Calculate_the_final_score()}')

t3 = organizationEmployee('Reza','Akbari',45135565,'Memari','Tehran',10,[10,20,12,16,20])
print(f't3 Final Score is : {t3.getname()} {t3.Calculate_the_final_score()}')

t4 = organizationEmployee('negin','monaii',545451316,'Farsi','Tehran',5,[50,90,100,80,100])
print(f't4 Final Score is : {t4.getname()} {t4.Calculate_the_final_score()}')


participants = [t1, t2, t3,t4]
high_scores = []

for participant in participants:
    if participant.Calculate_the_final_score() >= 90:
        high_scores.append(participant)

high_scorers_names = []
for scorer in high_scores:
    high_scorers_names.append(scorer.getname())

print(f'The List of People Who Got a Passing Grade: {high_scorers_names}')

