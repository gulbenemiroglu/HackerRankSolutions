n = int(input().strip())
if n>=1 and n<=100:
    if n%2!=0:
        print("Weird")
    else :
        if n>=2 and n<=5:
            print("Not weird")
        elif  n>=6 and n<=20:
            print("Weird")
        else:
            print("Not weird")
else: 
    print("it is not a valid")
    
    





















