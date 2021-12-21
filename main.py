from itertools import combinations

"""
GLOBAL CONST
"""
LISTE_INITIAL = [67, 104, 38, 124, 113, 114, 132, 101, 116, 59, 101, 115, 152, 32, 151, 105, 110, 148, 98, 108, 101, 54,
                 97, 74, 85, 250, 141, 198, 244, 211, 18, 113, 172, 236, 191, 138, 68, 79, 198, 132, 167, 17, 86]
NB_PREMIER = 257
NB_POINTS_JUSTE = -19
NB_POINTS_CONTENANT_ERREURS = 24


def euclide_etendu(a, b):
    """
    Fonction d'euclide étendu qui retourne le pgcd, le v et le u de 2 nombre
    :param a: premier nombre afin de trouver le pgcd
    :param b: deuxième nombre afin de trouver le pgcd
    :return: le pgcd, le v de a et le u de b
    """
    if (b == 0):
        return a, 1, 0
    else:
        (pgcd, u, v) = euclide_etendu(b, a % b)
        return (pgcd, v, u - (a // b) * v)


def voirDiff(polynome1, polynome2):
    """
    Fonction qui regarde la différence de taille d'un polynome et qui complète par des 0 afin que les 2 polynomes soient de même taille
    :param polynome1: un polynome
    :param polynome2: un polynome
    """
    if len(polynome1) - len(polynome2) < 0:
        diff = len(polynome2) - len(polynome1)
        ajouterManquant(polynome1, diff)
    else:
        diff = len(polynome1) - len(polynome2)
        ajouterManquant(polynome2, diff)


def ajouterManquant(poly, diff):
    """
    Ajoute un 0 à un polynome
    :param poly: un polynome
    :param diff: le nombre de 0 à ajouter
    """
    for i in range(diff):
        poly.append(0)


def additionPolynome(polynome1, polynome2):
    """
    Fonction d'addition de polynome
    :param polynome1: un polynome
    :param polynome2: un polynome
    :return: l'addition des 2 polynomes en paramètre
    """
    newPoly = []
    voirDiff(polynome1, polynome2)
    for x in range(len(polynome1)):
        newPoly.append((polynome1[x] + polynome2[x]) % NB_PREMIER)
    return newPoly


def modinv(a, m):
    """
        Fonction d'inverse modulaire
        :param polynome1: un nombre
        :param polynome2: un nombre
        :return: l'inverse modulaire de p suite à l'euclide étendue par m
        """
    g, x, y = euclide_etendu(a, m)
    if g != 1:
        raise Exception('L\'inverse modulaire n\'existe pas')
    else:
        return x % m


def multiplierPolynome(polynome1, polynome2):
    """
    Fonction de multiplication de polynome
    :param polynome1: un polynome
    :param polynome2: un polynome
    :return: la multiplication des 2 polynomes en paramètre
    """
    newPoly = []
    for i in range((len(polynome1) + len(polynome2) - 1)):
        newPoly.append(0)
    for x in range(len(polynome1)):
        for y in range(len(polynome2)):
            newPoly[x + y] += (polynome1[x] * polynome2[y]) % NB_PREMIER
    return newPoly


def lagrange(points):
    """
    Fonction qui calcule la grande pour une liste de points
    :param points: la liste de points à calculer
    :return: la liste de points en paramètre après été calculer par la grange
    """
    L = [0]
    for i in points:
        l_j = [1]
        for j in points:
            if j != i:
                reste = (i[0] - j[0])
                polyDivision = [(-1) * j[0] * modinv(reste, NB_PREMIER), 1 * modinv(reste, NB_PREMIER)]
                l_j = multiplierPolynome(l_j, polyDivision)
        l_j = multiplierPolynome(l_j, [i[1]])
        L = additionPolynome(l_j, L)
    return L


def convert(lst):
    """
    Converti une liste en plusieurs listes de points
    :param lst: une liste
    :return: un dictionnaire de liste avec des indices
    """
    dictionnary = []
    for i, j in enumerate(lst):
        dictionnary += [[i, j]]
    return dictionnary


def returnBonneListe(list):
    """
    Retourne la bonne liste de points passant par les 32 points afin de pouvoir décoder le message
    :param list: la liste initiale
    :return: la liste de points correcte
    """
    listeJuste = convert(list)[24:]
    randomList = combinations(list[:NB_POINTS_CONTENANT_ERREURS], 2)
    grange_list = lagrange(convert(list))
    for rand in randomList:
        new_list = convert(rand) + listeJuste
        L = lagrange(new_list)
        cpt = 0
        for i in range(len(grange_list)):
            if (evalPoly(L, i) == list[i]):
                cpt += 1
        if (cpt >= 32):
            return new_list



def evalPoly(pol, x):
    """
    Fonction d'évaluation de polynome
    :param pol: liste à évaluer
    :param x: chiffre pour le calcul de l'évaluation
    :return: le chiffre de cette évaluation
    """
    somme = 0
    for degre, coef in enumerate(pol[::-1]):
        if degre == 0:
            somme += coef
        else:
            somme = (somme * x + coef) % NB_PREMIER
    return somme


def toPhrase(List):
    """
    Converti une liste de points en caractère
    :param List: une liste de points
    """
    msg = ""
    for i in range(21):
        ch = round(evalPoly(List, i) % NB_PREMIER)
        msg += chr(ch)
    print(msg)

if __name__ == '__main__':
    print("Valeur de base : " + str(LISTE_INITIAL))
    print("Nombre premier : "+ str(NB_PREMIER))
    print("Bon polynome : "+ str(returnBonneListe(LISTE_INITIAL)))
    print(" ")
    print("Réponse : ")
    toPhrase(lagrange(returnBonneListe(LISTE_INITIAL)))
