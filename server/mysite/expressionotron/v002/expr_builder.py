"""
TODO : expliquer qu'il faut version, seed_max et build_expression
"""

import random
import functools
import operator

from .dataphrase import (
    RAW_STRING_VERBS, RAW_STRING_SUBJECTS, RAW_STRING_ADJ_PREFIXES,
    RAW_STRING_ADJECTIVES, RAW_STRING_WHATEVERS, RAW_STRING_INTERJECTIONS,
)
from .seeder import data_indexes_from_seed

version = '002'


def tupleFromRawString(rawString):
    liElemStripped = [ elem.strip() for elem in rawString.split("\n") ]
    liElemStrippedFiltered = [ elem for elem in liElemStripped if elem != "" ]
    return tuple(liElemStrippedFiltered)

raw_strings = (
    RAW_STRING_VERBS, RAW_STRING_SUBJECTS, RAW_STRING_ADJ_PREFIXES,
    RAW_STRING_ADJECTIVES, RAW_STRING_WHATEVERS, RAW_STRING_INTERJECTIONS,
)

(verbs, subjects, adj_prefixes, adjectives, whatevers, interjections) = [
   tupleFromRawString(raw_string)
   for raw_string in raw_strings
]

# Une seed fixe, pour générer toujours les mêmes shufflers. Comme ça une
# seed d'expression générera toujours la même expression.
SEED = "".join((
    "El haya gamila fi 'aineek, ana bahlam beek.",
    "Dayman dayman ahwak wo dayman ahwak.",
    "Inta 'aref leeh."))
random.seed(SEED)
data_lengths = []
shufflers = []
# Il n'y a pas les adj_prefixes dans le tuple sur lequel on boucle,
# c'est normal. On ne les choisit pas vraiment aléatoirement. Enfin si,
# mais pas directement aléatoirement. Bon bref voilà quoi.
for expr_piece in (verbs, subjects, adjectives, whatevers, interjections):
    len_expr_piece = len(expr_piece)
    data_lengths.append(len_expr_piece)
    shuffler = list(range(len_expr_piece))
    random.shuffle(shuffler)
    shufflers.append(tuple(shuffler))
shufflers = tuple(shufflers)
data_lengths = tuple(data_lengths)

# On reprend une seed totalement random, afin de générer des expressions
# totalement aléatoires.
random.seed()

seed_max = functools.reduce(operator.mul, data_lengths)


def _get_adjective_prefix(adjective, index_interjection):
    """
    Renvoie None (pas de préfixe d'adjectif) ou le préfixe choisi.

    Tous les adjectifs n'acceptent pas d'avoir un préfixe. Si ils sont
    constitués de plusieurs mots, ça ferait vraiment bizarre.

    De plus, le préfixe n'est pas choisi complètement au hasard comme les
    autres morceaux de phrases. On le prend à partir du choix de
    l'interjection (qui lui est complètement random). Il y a environ 3 fois
    plus d'interjections que de préfixes. C'est fait exprès. Ça donne environ
    une chance sur 3 d'avoir un préfixe si l'adjectif en accepte. Et j'ai
    estimé que c'était plutôt correcte comme dosage.

    La façon dont c'est déterminé fait qu'on ne peut pas avoir toutes les
    combinaisons possibles de couples (interjections, préfixes). On s'en fout.
    Les interjections ont justement été ajoutées pour absorber la probabilité
    de 1 sur 3 tout en permettant de générer une phrase différente pour chaque
    seed.
    """
    if index_interjection >= len(adj_prefixes):
        return None
    # REC TODO : faudrait être un peu plus intelligent que ça, parce que
    # certains adjectifs tordus, comme "+5" sont sans espaces, mais ont
    # l'air bizarre lorsqu'on leur met un préfixe. Ce sera pour la prochaine
    # version (si y'en a une un jour)
    if " " in adjective:
        return None

    return adj_prefixes[index_interjection]


# REC TODO : seed_digest ça veut rien dire. De plus, il y a plein de seeds
# différentes, utilisés pour différentes raisons, et il faudrait les nommer
# correctement. Mais pas là parce que j'ai autre chose à faire.
def buildExpression(seed_digest):
    data_indexes = data_indexes_from_seed(data_lengths, seed_digest, shufflers)
    # On teste pas le nombre d'index renvoyés, ni si ils sont bien inférieurs
    # à la taille des différents tuples de bouts de phrases.
    # Tout cela est censé avoir été fait lors de l'exécution des tests.
    verb = verbs[data_indexes[0]]
    subject = subjects[data_indexes[1]]
    adjective = adjectives[data_indexes[2]]
    whatever = whatevers[data_indexes[3]]
    interjection = interjections[data_indexes[4]]

    index_interjection = data_indexes[4]
    adjective_prefix = _get_adjective_prefix(adjective, index_interjection)

    if adjective_prefix is None:
        # TODO : mettre des format()
        tupleElements = (
            verb, subject, adjective, whatever, interjection)
        return "%s %s %s %s !! %s !!1!" % tupleElements
    else:
        tupleElements = (
            verb, subject, adjective_prefix, adjective, whatever, interjection)
        return "%s %s %s-%s %s !! %s !!1!" % tupleElements

