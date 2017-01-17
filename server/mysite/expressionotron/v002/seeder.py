# coding: utf-8
import functools
import operator


def data_indexes_from_seed(data_index_lengths, seed, shufflers=None):
    """
    Génère une suite de data_index plus ou moins aléatoirement,
    à partir d'une seed.

    Tous les résultats possibles sont couverts, pour une seed
    variant de 0 à (data_index_lengths[0] * data_index_lengths[1] * ...) - 1.
    Deux seed proches renvoient des suites de data_index éloignées.
    Presque tous les data_indexes changent entre deux seed consécutives.
    Si les valeurs de data_index_lengths sont suffisamment grandes, il y a
    encore plus de chances que les data_indexes changent tous.

    :param data_index_lengths:
        taille du range de chaque data_index. [ d1, d2, ..., dN ]
    :param seed: seed de génération aléatoire.
    :param shufflers: mélangeurs additionnels des data_indexes (facultatif).
    :type data_index_lengths:
        itérable sur des entiers > 0. (longueur N).
        Attention, les entiers doivent être rangés dans l'ordre croissant.
        Cette contrainte n'est pas contrôlée par la fonction. Si elle n'est
        pas respectée, le comportement est indéterminé : Exceptions,
        renvoi de data_indexes ne couvrant pas toutes les valeurs possibles,
        même résultat pour deux seeds différentes, ...
    :type seed: int.
    :type shufflers:
        itérable de N éléments. Chaque élément est un sous-itérable
        de d1,d2,...dN sous-éléments.
        Chaque sous-itérable doit comporter des sous-éléments int, variant de
        0 à d1-1, 0 à d2-1, ... 0 à dN-1.
        La façon dont les sous-éléments sont ordonnés détermine le mélange
        des data_indexes.
        Attention : le contenu de shufflers n'est pas contrôlé. Si les
        contraintes ci-dessus ne sont pas respectées, le comportement de la
        fonction est indéterminé.

    :return:
        Les data_indexes choisis à partir de la seed. [ i1, i2, ..., iN].
        Avec : 0 <= i1 < d1.
               0 <= i2 < d2.
               etc.
    :rtype: liste d'entiers >= 0, de longueur N.

    :Example:

    >>> data_index_lengths = [3, 5, 5, 7]
    >>> data_indexes_from_seed(data_index_lengths, 0)
    (0, 0, 0, 0)
    >>> data_indexes_from_seed(data_index_lengths, 2)
    (2, 2, 2, 2)
    >>> data_indexes_from_seed(data_index_lengths, 3)
    (0, 1, 1, 1)
    >>> data_indexes_from_seed(data_index_lengths, 500)
    (2, 3, 1, 5)
    >>> shuf_1 = [0, 2, 1]
    >>> shuf_2 = [4, 2, 0, 1, 3]
    >>> shuf_3 = [3, 4, 1, 0, 2]
    >>> shuf_4 = [5, 3, 1, 6, 0, 2, 4]
    >>> shufflers = [ shuf_1, shuf_2, shuf_3, shuf_4 ]
    >>> data_indexes_from_seed(data_index_lengths, 0, shufflers)
    (0, 4, 2, 5)
    """

    # Détermination des "randomizer index". Il s'agit d'une liste qui compte
    # les data_index, en partant de celui le plus à gauche.
    # Exemple (avec 4 data_indexes) :
    # Premiers éléments de randomizer_indexes :
    #     [0, 0, 0, 0], [1, 0, 0, 0], [2, 0, 0, 0], ...
    # Quand le premier randomizer_index atteint le premier data_index_length,
    # on le remet à 0 et on augmente de 1 le data_index suivant.
    # Éléments suivants de randomizer_indexes :
    #     [len-1, 0, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0], [2, 1, 0, 0], ...
    # Quand le deuxième randomizer_index atteint le deuxième data_index_length,
    # on le remet à 0 et on augmente le troisième data_index.
    # Et ainsi de suite.
    total_length = functools.reduce(operator.mul, data_index_lengths)
    randomizer_indexes = []
    for data_index_length in data_index_lengths:
        total_length //= data_index_length
        randomizer_index_backward = seed % data_index_length
        seed //= data_index_length
        randomizer_indexes.append(randomizer_index_backward)

    # Redéfinit chaque randomizer index,
    # en les mélangeant à l'aide des shufflers
    if shufflers is not None:
        randomizer_indexes_shuffled = [
            shufflers[meta_index][randomizer_indexes[meta_index]]
            for meta_index
            in range(len(data_index_lengths))
        ]
        randomizer_indexes = randomizer_indexes_shuffled

    # À partir de randomizer_indexes = [ 1, 4, 2, 3 ],
    # génère data_indexes_distributed = [
    #     [ 1, 1, 1, 1, ],
    #     [ 0, 4, 4, 4, ],
    #     [ 0, 0, 2, 2, ],
    #     [ 0, 0, 0, 3, ],
    # ]
    data_indexes_distributed = []
    for (meta_index, randomizer_index) in enumerate(randomizer_indexes):
        zeros = [0, ] * (meta_index)
        numbers = [randomizer_index, ] * (len(data_index_lengths)-meta_index)
        data_index_distributed = zeros + numbers
        data_indexes_distributed.append(data_index_distributed)

    # Additionne chaque colonne de data_indexes_distributed et fait un modulo,
    # pour obtenir des data_indexes dans les bornes, et mélangés.
    data_indexes_zipped = zip(*data_indexes_distributed)
    data_indexes = [
        sum(randomizer_index_zipped)
        for randomizer_index_zipped
        in data_indexes_zipped ]
    randomizer_indexes_final = [
        randomizer_index % data_index_length
        for (randomizer_index, data_index_length)
        in zip(data_indexes, data_index_lengths) ]

    return tuple(randomizer_indexes_final)

