import math
print("a*x+b=0 egyenletet oldok meg!")
a=float(input("Kérem az 'a' értékét!"))
b=float(input("Kérem a 'b' értékét!"))
if a==0:
    if b==0:
        print("Az összes x megoldás!")
    else:
        print("Nem megoldható!")
else:
    eredmeny=-b/a
    print(eredmeny)
    
