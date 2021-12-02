def euclide_etendue(a, b):
    if a==0:
        return b,0,1
    else:
        gcd,x,y=euclide_etendue(b % a, a)
        return gcd, y-(b//a)*x,x

def euclide_etend_Kex(a,b):
    if (b==0):
        return a,1,0
    else:
        (pgcd,u,v)= euclide_etend_Kex(b, a%b)
        return (pgcd,v,u-(a/b)*v)

# fonction euclide-étendu(a, b)
#     si b = 0 alors
#           retourner (a, 1, 0)
#     sinon
#           (d', u', v') := euclide-étendu(b, a mod b)
#           retourner (d', v', u' - (a÷b)v')