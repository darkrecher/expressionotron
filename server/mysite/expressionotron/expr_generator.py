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

FUNCTION_GEN_FROM_VERSION = {
    b_v1.version: b_v1.buildExpression,
    b_v2.version: b_v2.buildExpression,
}

VALID_VERSION_NUMBERS = FUNCTION_GEN_FROM_VERSION.keys()
CURRENT_EXPR_VERSION = b_v2.version
SEPARATOR_SEED = "_"


def sanitize_key(unsafe_expr_gen_key):
    """
    TODO : docstring expliquant les différents formats possibles de unsafe_expr_gen_key
    on peut pas demander du random sur une version précédente de l'expressionotron.
    C'est bien dommage mais c'est comme ça. Et de toutes façon on n'en a pas besoin.
    """
    rebuildSeed = False
    version = CURRENT_EXPR_VERSION
    digest = 0

    if unsafe_expr_gen_key.isdigit():
        # On a uniquement le digest, sans la version. C'est pas grave.
        # On prend ce digest, et on utilisera la version courante
        digest =  int(unsafe_expr_gen_key)

    else:
        # On verifie que la seed respecte le format 000...000_<num_version>
        # Si ce n'est pas le cas, on prendra un digest au hasard, et la version courante.
        strDigest, sep, version = unsafe_expr_gen_key.partition(SEPARATOR_SEED)
        if sep != SEPARATOR_SEED:
            rebuildSeed = True
        elif version not in VALID_VERSION_NUMBERS:
            rebuildSeed = True
        elif not strDigest.isdigit():
            rebuildSeed = True

        if rebuildSeed:
            version = CURRENT_EXPR_VERSION
            # REC TODO : v001 = 300000000 (un peu arbitraire). v002 = 87295229100.
            # faudrait juste que ce soit pas en dur. Vilain. Faut importer le size qu'est dans le generator.
            digest = random.randrange(87295229100)
        else:
            digest = int(strDigest)

    return (digest, version)


def generate_expression(seed, version):
    """
    Les paramètres seed et version sont supposés safe.
    Si ça ne l'est pas, ça fera des exceptions diverses.
    """
    function_expr_generator = FUNCTION_GEN_FROM_VERSION[version]
    return function_expr_generator(seed)


def format_key(seed, version):
    """
    fonction recréant une expr_gen_key à partir de seed/seed_str et de gen_version.
    """
    return SEPARATOR_SEED.join((str(seed), version))
