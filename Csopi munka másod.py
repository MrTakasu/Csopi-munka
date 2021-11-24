if valasztas=masodik
    import math
    a=float(input("Írd be az a-t"))
    b=float(input("Írd be az b-t"))
    c=float(input("Írd be az c-t"))
    # Első
    első=-b
    második=b**2
    harmadik=4*a*b
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
        print("Az x1",round(x1))
        print("Az x2",round(x2))
