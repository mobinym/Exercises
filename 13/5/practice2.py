city_List = ["city1","city2","city3","city4","city5","city6"] 
population_List = [300000, 1000000, 3800000, 500000, 1900000, 100000] 
area_List_squarekilometer = [100, 200, 500, 150, 300, 100] 

def convert_area():
    hektar_area_list=[]
    for i in area_List_squarekilometer:
        i*=100
        hektar_area_list.append(i)        
    return hektar_area_list


def population_density():
    density_list=[]
    for i in range(len(city_List)):
        density = population_List[i] // hektar_area_list[i]
        density_list.append(density)
    return density_list

def high_Density():
    city_area_dict = {}
    for i in range(len(city_List)):
        if density_list[i] >= 50:
            city_area_dict[city_List[i]] = density_list[i]
    return city_area_dict

#------------------------------------------------------------------

hektar_area_list=convert_area()
density_list=population_density()
city_area_dict =high_Density()



zip1 = zip(city_List,density_list)


dict1=[f'{key} {value}'for key,value in zip1]
print(f'List of cities by population density \n ---------------')

for i in dict1:
    print(i)

print(f'******************\nList of high-Density cities\n --------------- ')

for key,value in city_area_dict.items():
    print(f'{key} {value}')





