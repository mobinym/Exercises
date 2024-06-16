def main():
    x=input('What time is it? ')
    x=convert(x)
    if 7<=x<=8:
        print('breakfast time')
    elif 12<=x<=13:
        print('lunch time')
    elif 18<=x<=19:
        print('dinner time')

def convert(time):
    h,m=time.split(':')
    time=float(h)+(float(m)/60)
    return(time)
if __name__ == "__main__":
    main()