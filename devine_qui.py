from random import shuffle

from personnages import CARACTERISTIQUES
import random


def types_caracteristiques_ordre_aleatoire():
    """
    Donne les types de caractéristiques dans un ordre aléatoire.

    Indices:
    - Vous pouvez obtenir le dictionnaire de caractéristiques en important CARACTERISTIQUES
        du module personnages.
    - Vous pouvez obtenir la liste des clés d'un dictionnaire avec list(dictionnaire.keys())
    - Utilisez la fonction shuffle importée pour mélanger l'ordre de la liste (Attention:
        shuffle ne retourne rien, mais modifie directement la liste en argument)

    Returns:
        list: La liste des types de caractéristiques
    """
    print(CARACTERISTIQUES.keys())
    print(list(CARACTERISTIQUES.keys()))
    random.shuffle(CARACTERISTIQUES.keys())
    print(CARACTERISTIQUES.keys())
    return list



def valeurs_ordre_aleatoire(type_caracteristique):
    """
    Donne les valeurs de caractéristiques dans un ordre aléatoire,
    pour un type de caractéristique donné.

    Attention!! Si vous utilisez shuffle directement sur la liste de valeurs,
    celles-ci sera modifiée pour la suite du programme (il ne faut pas).
    Faites-en d'abord une copie avec liste.copy()

    Args:
        type_caracteristique (string): Le type de caractéristique

    Returns:
        list: La liste des valeurs possibles pour ce type de caractéristique
    """
    # VOTRE CODE ICI
    CARACT3 = list.copy(CARACTERISTIQUES[type_caracteristique])
    random.shuffle(CARACT3[type_caracteristique])
    return list


def possede(donnees_personnage, type_caracteristique, valeur_caracteristique):
    """
    Indique si la valeur de caractéristique fait partie des données du personnage.

    Attention! Si le type de caractéristique est accessoires ou pilosite, il faut vérifier
    que la valeur cherchée EST DANS les données du personnage pour ce type, tandis que
    si le type est autre chose, il faut vérifier que la valeur cherchée EST la donnée du personnage
    pour ce type.

    Args:
        donnees_personnage (dict): Les données (sous forme type:valeur) pour un personnage
        type_caracteristique: Le type de caractéristique analysé
        valeur_caracteristique: La valeur de la caractéristique recherchée

    Returns:
        bool: True si le personnage possède la caractéristique, False sinon.
    """
    if list(donnees_personnage[type_caracteristique]) == [
        valeur_caracteristique] and type_caracteristique != "accesoires" or "pilosite":
        return True
    elif [valeur_caracteristique] in list(
            donnees_personnage[type_caracteristique]) and type_caracteristique != "accesoires" or "pilosite":
        return True
    else:
        return False


def score_dichotomie(personnages_restants, type_caracteristique, valeur_caracteristique):
    """
    Retourne un score en fonction du nombre de personnages restants ayant ou n'ayant pas la
    caractéristique en paramètres. Ce score est élevé pour les caractéristiques divisant les personnages
    en deux parties le plus égales possibles, et est faible pour les caractéristiques divisant les
    personnages en parties inégales.

    Le score est calculé selon la formule suivante:
    nombre de personnages total - maximum(nombre de personnages ayant la caractéristique,
                                          nombre de personnages n'ayant pas la caractéristique)

    Exemple:
    En début de partie, il y 5 femmes sur 24 personnages. Le score de la caractéristique ayant le type genre
    et la valeur femme est donc 24 - maximum(5, 19), c'est-à-dire 5.
    En revanche, ce score peut changer en cours de partie. Par exemple supposons qu'il ne reste que
    les personnages ayant des chapeaux. Il y a alors 2 femmes sur 5 personnages. Le score
    de la caractéristique femme est donc 5 - maximum(2, 3), donc 2. Le score de la caractéristique
    lunettes serait quant à lui 5 - maximum(1, 4), c'est-à-dire 1. Cela indique que, parmi les personnages
    ayant des chapeaux, la caractéristique femme divise mieux l'ensemble que la caractéristique lunettes.

    Note: cette fonction devrait appeler la fonction possede.

    Args:
        personnages_restants (dict): L'ensemble des personnages n'ayant pas été éliminés encore.
        type_caracteristique (string): Le type de la caractéristique dont on veut connaître le score
        valeur_caracteristique (string): La valeur de la caractéristique dont on veut connaître le score

    Returns:
        int: Le score
    """
    list_personnages_restants = list(personnages_restants)
    nombre_de_personnages_total = len(list_personnages_restants)
    i = 0
    while i != nombre_de_personnages_total:
        if possede(list_personnages_restants[i], type_caracteristique, valeur_caracteristique):
            personnages_ayant_la_caractéristique = 0
            personnages_ayant_la_caractéristique += 1
        i += 1
    score = nombre_de_personnages_total - maximum(personnages_ayant_la_caractéristique,
                                                  (nombre_de_personnages_total - personnages_ayant_la_caractéristique))
    return score


def selectionner_caracteristique(personnages_restants):
    """
    Parmi tous les couples type/valeur de caractéristiques, retourne
    celui qui présente le meilleur score de dichotomie. Les types et valeurs doivent être
    itérées en ordre aléatoire (utilisez les fonctions à cet effet déclarées précédemment)

    Note: cette fonction devrait appeler les fonctions
        types_caracteristiques_ordre_aleatoire, valeurs_ordre_aleatoire et score_dichotomie.

    Args:
        personnages_restants (dict): Les personnages à considérer pour les scores.

    Returns:
        (string, string): Le type et la valeur ayant le meilleur score dichotomique
    """
    i = 0
    List_type_caract_alea = types_caracteristiques_ordre_aleatoire()
    while i != len(List_type_caract_alea):
        m = 0
        List_caract_alea = valeurs_ordre_aleatoire(List_type_caract_alea[i])
        while m != len(valeurs_ordre_aleatoire(List_type_caract_alea[i])):
            scoreactuel = score_dichotomie(List_type_caract_alea[i],
                                           List_caract_alea[m])
            scoreavant = 0
            if scoreavant <= scoreactuel:
                caract_optim = List_caract_alea[m]
                type_caract_optim = List_type_caract_alea[i]
            m += 1
        i += 1
    return (type_caract_optim, caract_optim)


def mettre_a_jour_hypotheses(personnages_restants, type_caracteristique, valeur_caracteristique, reponse):
    """
    Retourne un dictionnaire basé sur le dictionnaire de personnages restants en paramètre, dans
    lequel on enlève les personnages qui possèdent ou ne possèdent pas la caractéristique en paramètres.

    Args:
        personnages_restants (dict): Les personnages préalablement restants
        type_caracteristique (string): Le type de la caractéristique dont on
                                       veut conserver/enlever ceux qui l'ont
        valeur_caracteristique (string): La valeur de la caractéristique dont
                                   on veut conserver/enlever ceux qui l'ont
        reponse (bool): True si on doit conserver les personnages qui possèdent la caractéristique,
                        False si on doit conserver ceux qui ne la possèdent pas.

    Note: cette fonction devrait appeler la fonction possede.

    Returns:
        dict: Le dictionnaire de personnages restants mis à jour.
    """
    list_personnages_restants = list(personnages_restants)
    nombre_de_personnages_total = len(list_personnages_restants)
    i = 0
    while i != nombre_de_personnages_total:
        if reponse:
            if not possede(list_personnages_restants[i], type_caracteristique, valeur_caracteristique):
                list_personnages_restants.remove(i)
        if not reponse:
            if possede(list_personnages_restants[i], type_caracteristique, valeur_caracteristique):
                list_personnages_restants.remove(i)
        i += 1


if __name__ == '__main__':
    print("Tests unitaires...")

    # Test de la fonction types_caracteristiques_ordre_aleatoire
    assert len(types_caracteristiques_ordre_aleatoire()) == len(CARACTERISTIQUES)

    # Test de la fonction valeurs_ordre_aleatoire
    assert len(valeurs_ordre_aleatoire("cheveux")) == len(CARACTERISTIQUES["cheveux"])

    # Tests de la fonction possede
    donnees = {"cheveux": "bruns", "accessoires": ["chapeau"]}
    assert possede(donnees, "cheveux", "bruns")
    assert not possede(donnees, "accessoires", "bijoux")

    # Tests de la fonction score_dichotomie
    personnages = {'Bernard': {'genre': 'homme', 'accessoires': ['chapeau']},
                   'Claire': {'genre': 'femme', 'accessoires': ['chapeau']},
                   'Eric': {'genre': 'homme', 'accessoires': ['chapeau']},
                   'George': {'genre': 'homme', 'accessoires': ['chapeau']},
                   'Maria': {'genre': 'femme', 'accessoires': ['chapeau']}}
    assert score_dichotomie(personnages, 'genre', 'homme') == 2  # = 5 - max(3, 2)
    assert score_dichotomie(personnages, 'accessoires', 'chapeau') == 0  # = 5 - max(5, 0)

    # Aucun test n'est fourni pour selectionner_caracteristiques

    # Tests de la fonction mettre_a_jour_hypotheses
    assert len(mettre_a_jour_hypotheses(personnages, 'genre', 'homme', True)) == 3
    assert len(mettre_a_jour_hypotheses(personnages, 'genre', 'homme', False)) == 2

    print("Tests réussis!")
