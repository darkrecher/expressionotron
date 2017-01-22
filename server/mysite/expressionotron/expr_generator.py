"""
TODO : docstring expliquant le vocabulaire des noms de variable relative à la seed.
unsafe_expr_gen_key
expr_gen_key
version
seed
seed_str
"""

import random
# Renommer tout ça en "expr_generator". "Builder", ça fait bizarre.
import expressionotron.v001.exprBuilder
b_v1 = expressionotron.v001.exprBuilder
import expressionotron.v002.expr_builder
b_v2 = expressionotron.v002.expr_builder

# Renommer ce nom à la con de dictionnaire.
FUNC_BUILDER_FROM_VERSION = {
    b_v1.version: b_v1.buildExpression,
    b_v2.version: b_v2.buildExpression,
}

VALID_VERSION_NUMBERS = (b_v1.version, b_v2.version)
CURRENT_EXPR_VERSION = b_v2.version
SEPARATOR_SEED = "_"


def makeValidSeed(strSeed):
    """
    TODO : docstring expliquant les différents formats possibles de strSeed
    on peut pas demander du random sur une version précédente de l'expressionotron.
    C'est bien dommage mais c'est comme ça. Et de toutes façon on n'en a pas besoin.
    """
    rebuildSeed = False
    strVersion = CURRENT_EXPR_VERSION
    digest = 0

    if strSeed.isdigit():
        # On a uniquement le digest, sans la version. C'est pas grave.
        # On prend ce digest, et on utilisera la version courante
        digest =  int(strSeed)

    else:
        # On verifie que la seed respecte le format 000...000_<num_version>
        # Si ce n'est pas le cas, on prendra un digest au hasard, et la version courante.
        strDigest, sep, strVersion = strSeed.partition(SEPARATOR_SEED)
        if sep != SEPARATOR_SEED:
            rebuildSeed = True
        elif strVersion not in VALID_VERSION_NUMBERS:
            rebuildSeed = True
        elif not strDigest.isdigit():
            rebuildSeed = True

        if rebuildSeed:
            strVersion = CURRENT_EXPR_VERSION
            # REC TODO : v001 = 300000000 (un peu arbitraire). v002 = 87295229100.
            # faudrait juste que ce soit pas en dur. Vilain.
            digest = random.randrange(87295229100)
        else:
            digest = int(strDigest)

    strSeed = SEPARATOR_SEED.join( (str(digest), strVersion) )
    # TODO : faut inverser les params : digest, version, str.
    return (strVersion, digest, strSeed)


def generate_expression(seed, version):
    """
    Les paramètres seed et version sont supposés safe.
    Si ça ne l'est pas, ça fera des exceptions diverses.
    """
    function_expr_generator = FUNC_BUILDER_FROM_VERSION[version]
    return function_expr_generator(seed)


# TODO : fonction recréant une expr_gen_key à partir de seed/seed_str et de gen_version.