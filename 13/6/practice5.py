import itertools
import operator 

# Math = M, Computer = C, Industrial Engineering = IE, Electrical Engineering = EE """
expert_List1 = [("Ali","Ahmadi","M",35), ("Sima","Sadri","C",39), 
("Ahmad","Moradi","M",30), ("Ftemeh","Majd","C",29), ("Sara","Biglar","IE",27), 
("Reza","Rahnama","EE",45)] 

expert_List2 = [("Mina","Gohari","EE",40), ("Iman","Shams","M",26), 
("Farzad","Yeganeh","M",41), ("Ali","Imani","C",33), ("Aref","Alameh","M",32), 
("Narges","Sohrabi","C",35)] 


Totallist = [expert_List1,expert_List2]

chain = list(itertools.chain.from_iterable(Totallist))
SortChainList=sorted(chain,key=operator.itemgetter(2))

print(30*'-'+'SortChainList'+30*'-'+'\n')

print(SortChainList)

print(30*'-'+'Math_selected'+30*'-'+'\n')

Math_selected=[select for select in chain if select[2]=='M']
print(Math_selected)

print(30*'-'+'Combinations'+30*'-'+'\n')

combinations=list(itertools.combinations(Math_selected,3))
for i in combinations:
    print(i)

