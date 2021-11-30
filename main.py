def euclide_etendue(a, b):
    if a==0:
        return b,0,1
    else:
        gcd,x,y=euclide_etendue(b % a, a)
        return gcd, y-(b//a)*x,x
