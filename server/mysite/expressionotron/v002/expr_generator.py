"""
Module permettant de générer une expression top délire à partir d'une seed.

Toutes les modules de générateur d'expression doivent obligatoirement
comporter les éléments suivants :

version : chaîne de caractère. Indique la version du module.

generate_expression : fonction nécessitant un paramètre 'seed'
(valeur numérique) et renvoyant une chaîne de caractère (l'expression).
La même seed doit toujours renvoyer la même expression.

seed_max : valeur numérique. Elle renseigne sur la quantité d'expression qui
peuvent être générées. Idéalement, si on fait varier le paramètre 'seed'
de 0 à seed_max, on devrait couvrir toutes les expressions possibles, sans
qu'il y ait de doublons.
Pour cette version '002', cette consigne est bien respectée. De plus, les
expressions restent dans le même ordre. C'est à dire que
generate_expression(n) == generate_expression(seed_max + n)
"""

import random
import functools
import operator

from expressionotron.common_tools import tuple_from_raw_str
from . import dataphrase
from .seeder import data_indexes_from_seed


version = '002'

raw_strings = (
    dataphrase.RAW_STRING_VERBS,
    dataphrase.RAW_STRING_SUBJECTS,
    dataphrase.RAW_STRING_ADJ_PREFIXES,
    dataphrase.RAW_STRING_ADJECTIVES,
    dataphrase.RAW_STRING_WHATEVERS,
    dataphrase.RAW_STRING_INTERJECTIONS,
)

(verbs, subjects, adj_prefixes, adjectives, whatevers, interjections) = [
   tuple_from_raw_str(raw_string)
   for raw_string in raw_strings
]

# On crée une seed fixe, pour générer toujours les mêmes shufflers.
# Comme ça une, seed d'expression générera toujours la même expression.
SEED_SHUFFLERS = (''
    'El haya gamila fi \'aineek, ana bahlam beek.'
    'Dayman dayman ahwak wo dayman ahwak.'
    'Inta \'aref leeh.')
random.seed(SEED_SHUFFLERS)
data_lengths = []
shufflers = []
# Il n'y a pas les adj_prefixes dans le tuple sur lequel on boucle,
# c'est normal. On ne les choisit pas vraiment aléatoirement. Enfin si,
# mais pas directement aléatoirement.
for expr_list in (verbs, subjects, adjectives, whatevers, interjections):
    len_expr_list = len(expr_list)
    data_lengths.append(len_expr_list)
    shuffler = list(range(len_expr_list))
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
    if ' ' in adjective:
        return None

    return adj_prefixes[index_interjection]


def generate_expression(seed_expr):
    data_indexes = data_indexes_from_seed(data_lengths, seed_expr, shufflers)
    # On ne teste pas le nombre d'index renvoyés, ni s'ils sont bien inférieurs
    # à la taille des différents tuples de bouts de phrases.
    # Tout cela est censé avoir été fait lors de l'exécution des tests.
    verb = verbs[data_indexes[0]]
    subject = subjects[data_indexes[1]]
    adjective = adjectives[data_indexes[2]]
    whatever = whatevers[data_indexes[3]]
    interjection = interjections[data_indexes[4]]

    index_interjection = data_indexes[4]
    adj_prefix = _get_adjective_prefix(adjective, index_interjection)

    if adj_prefix is None:
        # TODO : mettre des format()
        expr_pieces = (
            verb, subject, adjective, whatever, interjection)
        return '%s %s %s %s !! %s !!1!' % expr_pieces
    else:
        expr_pieces = (
            verb, subject, adj_prefix, adjective, whatever, interjection)
        return '%s %s %s-%s %s !! %s !!1!' % expr_pieces

