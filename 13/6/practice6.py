import collections
mobile = collections.namedtuple('mobile','brand model price color')
mobile1=mobile('Samsung','2018',5000000,['black','blue','red'])
mobile2=mobile('Apple','2020',20000000,['white','black','blue','red'])
mobile3=mobile('Apple','2021',40000000,['blue','red'])
mobile4=mobile('Shiami','2022',5000000,['blue','red','pink'])
mobile5 = mobile('nokia', '3310', 1000000, ['grey', 'blue'])
mobile6 = mobile('sony', 'xperia', 15000000, ['black', 'white'])
mobile7 = mobile('lg', 'g6', 12000000, ['black', 'silver'])
mobile8 = mobile('htc', 'u11', 13000000, ['blue', 'red'])
mobile9 = mobile('motorola', 'moto g', 8000000, ['black', 'white'])
mobile10 = mobile('huawei', 'p30', 18000000, ['black', 'blue'])


mobilelist=[mobile1,mobile2,mobile3,mobile4,mobile5,mobile6,mobile7,mobile8,mobile9,mobile10]
for i in mobilelist:
    i._asdict()
    print(i)

