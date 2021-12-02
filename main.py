liste=[67, 104, 38, 124, 113, 114, 132, 101, 116, 59, 101, 115, 152, 32, 151, 105, 110, 148, 98, 108, 101, 54, 97, 74, 85, 250, 141, 198, 244, 211, 18, 113, 172, 236, 191, 138, 68, 79, 198, 132, 167, 17, 86]

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
        return (pgcd,v,u-(a//b)*v)

# fonction euclide-étendu(a, b)
#     si b = 0 alors
#           retourner (a, 1, 0)
#     sinon
#           (d', u', v') := euclide-étendu(b, a mod b)
#           retourner (d', v', u' - (a÷b)v')