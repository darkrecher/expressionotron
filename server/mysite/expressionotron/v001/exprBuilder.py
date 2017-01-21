from .dataphrase import (
    RAW_STRING_VERB, RAW_STRING_COMPLEMENT, RAW_STRING_PREFIX_ADJ,
    RAW_STRING_ADJ, RAW_STRING_WHATEVER)

version = '001'


def tupleFromRawString(rawString):
    liElemStripped = [ elem.strip() for elem in rawString.split("\n") ]
    liElemStrippedFiltered = [ elem for elem in liElemStripped if elem != "" ]
    return tuple(liElemStrippedFiltered)

TUPLE_VERB = tupleFromRawString(RAW_STRING_VERB)
TUPLE_COMPLEMENT = tupleFromRawString(RAW_STRING_COMPLEMENT)
TUPLE_PREFIX_ADJ = tupleFromRawString(RAW_STRING_PREFIX_ADJ)
TUPLE_ADJ = tupleFromRawString(RAW_STRING_ADJ)
TUPLE_WHATEVER = tupleFromRawString(RAW_STRING_WHATEVER)

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
import functools
MULTIPLICATOR = functools.reduce(lambda x, y: x*(y-1), TUPLE_NB_POSSIBILITIES, 1) - 1

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


def buildExpression(seedDigest):
    liChoices = _extractChoices(seedDigest*MULTIPLICATOR)
    return _applyChoices(liChoices)

