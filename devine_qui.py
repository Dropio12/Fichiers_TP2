from personnages import CARACTERISTIQUES
from random import shuffle


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
    liste_type_caracteristique = list(CARACTERISTIQUES.keys())  # liste des types de caractéristiques #
    shuffle(liste_type_caracteristique)  # mélange la liste
    return liste_type_caracteristique  # retourne la liste


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
    liste_caracteristique = list.copy(CARACTERISTIQUES[type_caracteristique])  # liste des valeurs de caractéristiques
    shuffle(liste_caracteristique)  # mélange la liste
    return liste_caracteristique  # retourne la liste des caractéristiques mélangés


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

    if type_caracteristique == "accessoires" or type_caracteristique == "pilosite":  # si le type est accessoires ou
        # pilosite
        if donnees_personnage[type_caracteristique] == [valeur_caracteristique]:  # si la valeur est dans les données
            # du personnage, retourne True
            return True
        else:  # si la valeur n'est pas dans les données du personnage, , on retourne False
            return False
    else:  # si le type n'est pas accessoires ou pilosite et que la valeur est dans les données du personnage,
        # retourne True. Sinon, retourne False.
        if donnees_personnage[type_caracteristique] == valeur_caracteristique:
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
    liste_personnages_restants = list(personnages_restants.keys())  # liste des personnages restants
    liste_caracteristique_personnages_restants = list(personnages_restants.values())  # liste des caractéristiques des
    # personnages restants
    nombre_de_personnages_total = len(liste_personnages_restants)  # nombre de personnages total
    personnages_ayant_la_caracteristique = 0  # nombre de personnages ayant la caractéristique
    i = 0  # compteur 1
    while i != nombre_de_personnages_total:  # tant que le compteur 1 n'est pas égal au nombre de personnages total
        k = 0  # compteur 2
        while k != len(liste_caracteristique_personnages_restants[i].keys()):  # tant que le compteur 2 n'est pas
            # égal au nombre de caractéristiques des personnages restants
            if list(liste_caracteristique_personnages_restants[i].keys())[k] == type_caracteristique and (
                    type_caracteristique == "accessoires" or type_caracteristique == "pilosite"):  # si le type est
                # accessoires ou pilosite
                t = 0  # compteur 3
                while t != len(liste_caracteristique_personnages_restants[i].values()):
                    if valeur_caracteristique == list(liste_caracteristique_personnages_restants[i].values())[t]:  #
                        # si la valeur est dans les données du personnage, on ajoute 1 au nombre de personnages ayant
                        # la caractéristique
                        personnages_ayant_la_caracteristique += 1
                    t += 1
            elif list(liste_caracteristique_personnages_restants[i].keys())[k] == type_caracteristique:  # si le type
                # n'est pas accessoires ou pilosite
                if valeur_caracteristique in list(liste_caracteristique_personnages_restants[i].values())[k]:
                    personnages_ayant_la_caracteristique += 1  # si la valeur est dans les données du personnage,
                    # on ajoute 1 au nombre de personnages ayant la caractéristique
            k += 1  # on incrémente le compteur 2
        i += 1  # on incrémente le compteur 1
    # on sépare ceux qui ont de la pilosité et des accessoires des autres, car ils sont dans des listes
    score = nombre_de_personnages_total - max(personnages_ayant_la_caracteristique,
                                              (nombre_de_personnages_total - personnages_ayant_la_caracteristique))
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
    liste_type_caracteristiques = [types_caracteristiques_ordre_aleatoire()]  # liste des types de caractéristiques
    liste_type_caracteristiques = list(liste_type_caracteristiques)[0]  # on transforme la liste en liste de liste
    # pour enlever les []
    a = 0  # compteur 1
    score_avant = 0  # le score final va être stocké dans cette variable
    type_caract = ""  # type de caractéristique
    valeur = ""  # valeur de la caractéristique
    while len(liste_type_caracteristiques) != a:
        liste_caracteristiques = [valeurs_ordre_aleatoire(liste_type_caracteristiques[a])]  # liste des caractéristiques
        liste_caracteristiques = list(liste_caracteristiques)[
            0]  # on transforme la liste en liste de liste pour enlever
        # les []
        c = 0  # compteur 2
        while len(liste_caracteristiques) != c:  # tant que le compteur 2 n'est pas égal au nombre de caractéristiques,
            # on passe toute les caractéristiques du type donné plus haut et on trouve le meilleur score, on le stocke
            # dans score_avant et on stocke le type et la valeur dans type_caract et valeur
            score_actuel = [
                score_dichotomie(personnages_restants, liste_type_caracteristiques[a], liste_caracteristiques[c])]
            if score_actuel[0] >= score_avant:
                score_avant += score_actuel[0]
                type_caract = liste_type_caracteristiques[a]
                valeur = liste_caracteristiques[c]
            c += 1
        a += 1
    return type_caract, valeur


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
    liste_cara_personnages_restants = list(personnages_restants.values())  # liste des caractéristiques des personnages
    liste_personnages_restants = list(personnages_restants.keys())  # liste des personnages restants
    nombre_de_personnages_total = len(liste_personnages_restants)  # nombre de personnages restants
    personnages_restants_a_jour = {}  # dictionnaire des personnages restants à jour
    k = 0
    i = 0
    while k != len(personnages_restants):  # passe à travers tous les personnages restants et crée une copie du
        # dictionnaire personnages_restants
        personnages_restants_a_jour[list(personnages_restants.keys())[k]] = list(personnages_restants.values())[k]
        k += 1
    while i != nombre_de_personnages_total:  # passe à travers tous les personnages restants
        if reponse:  # si la réponse est oui, on enlève les personnages qui possèdent la caractéristique
            if not possede(liste_cara_personnages_restants[i], type_caracteristique, valeur_caracteristique):
                del personnages_restants_a_jour[liste_personnages_restants[i]]
        if not reponse:  # si la réponse est non, on enlève les personnages qui ne possèdent pas la caractéristique
            if possede(liste_cara_personnages_restants[i], type_caracteristique, valeur_caracteristique):
                del personnages_restants_a_jour[liste_personnages_restants[i]]
        i += 1
    return personnages_restants_a_jour


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
    score_dichotomie(personnages, 'genre', 'homme')

    # Aucun test n'est fourni pour selectionner_caracteristiques
    assert selectionner_caracteristique(personnages) == ('genre', 'homme') or ('genre', 'femme')
    assert selectionner_caracteristique(personnages) != ('accessoires', 'chapeau')
    # Tests de la fonction mettre_a_jour_hypotheses
    assert len(mettre_a_jour_hypotheses(personnages, 'genre', 'homme', True)) == 3
    assert len(mettre_a_jour_hypotheses(personnages, 'genre', 'homme', False)) == 2

    print("Tests réussis!")
