from itertools import combinations

liste_initial=[67, 104, 38, 124, 113, 114, 132, 101, 116, 59, 101, 115, 152, 32, 151, 105, 110, 148, 98, 108, 101, 54, 97, 74, 85, 250, 141, 198, 244, 211, 18, 113, 172, 236, 191, 138, 68, 79, 198, 132, 167, 17, 86]

# GLOBAL CONST

NB_PREMIER = 257
NB_POINTS_JUSTE = -19
NB_POINTS_CONTENANT_ERREURS = 24


def euclide_etendu(a,b):
    if (b==0):
        return a,1,0
    else:
        (pgcd,u,v)= euclide_etendu(b, a%b)
        return (pgcd,v,u-(a//b)*v)

def voirDiff(polynome1, polynome2):
    if len(polynome1) - len(polynome2) < 0:
        diff = len(polynome2) - len(polynome1)
        ajouterManquant(polynome1, diff)
    else:
        diff = len(polynome1) - len(polynome2)
        ajouterManquant(polynome2, diff)

def ajouterManquant(poly,diff):
    for i in range(diff):
        poly.append(0)

def ajouterPolynome(polynome1, polynome2):
    newPoly=[]
    voirDiff(polynome1, polynome2)
    for x in range(len(polynome1)):
        newPoly.append((polynome1[x]+polynome2[x])%NB_PREMIER)
    return newPoly

def modinv(a, m):
    g, x, y = euclide_etendu(a, m)
    if g != 1:
        raise Exception('L\'inverse modulaire n\'existe pas')
    else:
        return x % m

def multiplierPolynome(polynome1, polynome2):
    newPoly=[]
    for i in range((len(polynome1)+len(polynome2)-1)):
        newPoly.append(0)
    for x in range(len(polynome1)):
        for y in range(len(polynome2)):
            newPoly[x+y]+=(polynome1[x]*polynome2[y])%NB_PREMIER
    return newPoly

def lagrange(points):
    L =[0]
    for i in points:
        l_j = [1]
        for j in points:
            if j!= i:
                reste = (i[0]-j[0])
                polyDivision = [(-1)*j[0]*modinv(reste, NB_PREMIER), 1*modinv(reste, NB_PREMIER)]
                l_j=multiplierPolynome(l_j, polyDivision)
        l_j =multiplierPolynome(l_j,[i[1]])
        L = ajouterPolynome(l_j,L)
    return L

def convert(lst):
    dictionnary = []
    for i,j in enumerate(lst[::-1]):
        dictionnary += [[i,j]]
    return dictionnary

def returnGrange(list):
    listeJuste = convert(list)[NB_POINTS_JUSTE:]
    randomList = combinations(list[:NB_POINTS_CONTENANT_ERREURS], 2)
    for i in randomList:
        # print(convert(i))
        new_list = listeJuste+convert(i)
        #print(lagrange(new_list))
        evalPoly(lagrange(new_list),10)

def evalPoly(pol,x):
    somme=0
    for degre, coef in enumerate(pol[::-1]):
        if degre==0:
            somme+=coef
        else:
            somme=(somme*x+coef)%NB_PREMIER
    return somme

valeur =[[0,1],[1,3],[2,7]]

if __name__ == '__main__':
    print(evalPolyDylan([2,3,1,6], 10))
