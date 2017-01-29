"""
Module permettant de générer une expression top délire à partir d'une seed.

Toutes les modules de générateur d'expression doivent obligatoirement
comporter les éléments suivants :

version : chaîne de caractère. Indique la version du module.

build_expression : fonction nécessitant un paramètre 'seed' (valeur numérique)
et renvoyant une chaîne de caractère (l'expression). La même seed doit
toujours renvoyer la même expression.

seed_max : valeur numérique. Elle renseigne sur la quantité d'expression qui
peuvent être générées. Idéalement, si on fait varier le paramètre 'seed'
de 0 à seed_max, on devrait couvrir toutes les expressions possibles, sans
qu'il y ait de doublons.
Pour cette version '001', cette consigne n'est pas respectée, la valeur de
seed_max est fortement arbitraire. Mais le module fonctionne quand même.
"""

# Ce fichier de code ne respecte pas le PEP8, et il est plutôt mal codé.
# Mais je le laisse comme ça car c'est la version précédente et ce n'est pas
# grave si elle n'évolue plus. C'est du "code legacy", on va dire.

import functools

from expressionotron.common_tools import tuple_from_raw_str
from .dataphrase import (
    RAW_STRING_VERB, RAW_STRING_COMPLEMENT, RAW_STRING_PREFIX_ADJ,
    RAW_STRING_ADJ, RAW_STRING_WHATEVER)


version = '001'

TUPLE_VERB = tuple_from_raw_str(RAW_STRING_VERB)
TUPLE_COMPLEMENT = tuple_from_raw_str(RAW_STRING_COMPLEMENT)
TUPLE_PREFIX_ADJ = tuple_from_raw_str(RAW_STRING_PREFIX_ADJ)
TUPLE_ADJ = tuple_from_raw_str(RAW_STRING_ADJ)
TUPLE_WHATEVER = tuple_from_raw_str(RAW_STRING_WHATEVER)

# 1 chance sur 3 de rajouter un prefixe a l'adjectif.
# Mais on refiltrera encore une fois, en decidant de pas mettre le prefixe
# si l'adjectif est compose de plusieurs mots
TUPLE_ENABLE_PREFIX = ("y", "n", "n")

TUPLE_NB_POSSIBILITIES = (
    len(TUPLE_VERB),
    len(TUPLE_COMPLEMENT),
    len(TUPLE_ENABLE_PREFIX),
    len(TUPLE_PREFIX_ADJ),
    len(TUPLE_ADJ),
    len(TUPLE_WHATEVER))

# Example : La taille des listes est (100, 100, 3, 54, 120)
# Alors, MULTIPLICATOR vaudra 99 * 99 * 2 * 53 * 119 - 1
# (Pas sur du tout que ce soit une bonne methode, mais j'emmerde les maths.)
MULTIPLICATOR = functools.reduce(lambda x, y: x*(y-1), TUPLE_NB_POSSIBILITIES, 1) - 1

# Valeur totalement arbitraire. Mais c'est celle que j'utilisais dans cette
# 1ère version, je la garde ici pour info et pour l'homogénéité.
# (Mais en vrai, on ne s'en sert plus)
seed_max = 300000000


def _extractChoices(seedDigest):
    liChoices = []
    for nbPossibility in TUPLE_NB_POSSIBILITIES:
        choice = seedDigest % nbPossibility
        seedDigest = seedDigest // nbPossibility
        liChoices.append(choice)
    return liChoices

def _applyChoices(liChoices):
    verb = TUPLE_VERB[liChoices[0]]
    complement = TUPLE_COMPLEMENT[liChoices[1]]
    enablePrefix = TUPLE_ENABLE_PREFIX[liChoices[2]] == "y"
    # On prend pas tout de suite le prefixe d'adjectif, parce qu'il ne sera peut-etre pas necessaire.
    adj = TUPLE_ADJ[liChoices[4]]
    whatever = TUPLE_WHATEVER[liChoices[5]]
    if " " not in adj and enablePrefix:
        prefixAdj = TUPLE_PREFIX_ADJ[liChoices[3]]
        tupleElements = (verb, complement, prefixAdj, adj, whatever)
        formatExpression = "%s %s %s-%s %s !! 11! !!1"
    else:
        tupleElements = (verb, complement, adj, whatever)
        formatExpression = "%s %s %s %s !! 11! !!1"
    return formatExpression % tupleElements


def build_expression(seedDigest):
    liChoices = _extractChoices(seedDigest*MULTIPLICATOR)
    return _applyChoices(liChoices)

