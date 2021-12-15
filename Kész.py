choice=int(input("Nyomja meg az 1-es gombot,ha az első fokú egyenletet szeretné kiválasztani, Nyomja meg a 2-es gombot, ha Másodfokú egyenletet szeretné választani!'))"))
if (choice==1):
    # Első
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
    # Második
elif (choice==2): 
        import math
        a=float(input("Írd be az a-t"))
        b=float(input("Írd be az b-t"))
        c=float(input("Írd be az c-t"))
        if a==0:
                if b==0:
                        if c==0:
                                print("Az összes x megoldás!")
                        else:
                                print("Nem megoldható!")
                else:
                        eredmeny=-c/b
                        print(eredmeny)
        else:
            # Első
            első=-b
            második=b**2
            harmadik=4*a*c
            negyedik=2*a
            # Második
            számítás1=második-harmadik
            if számítás1<0:
                print("Nincs megoldás")
            else:
                számítás2=math.sqrt(számítás1)
                # Harmadik
                x1=(első+számítás2)/negyedik
                x2=(első-számítás2)/negyedik
                # Negyedik
                print("Az x1:",round(x1))
                print("Az x2:",round(x2))
else:
    print('Érvényes számot írj!')

