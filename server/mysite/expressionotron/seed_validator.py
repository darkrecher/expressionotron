import random
import expressionotron.v001.exprBuilder
b_v1 = expressionotron.v001.exprBuilder
import expressionotron.v002.expr_builder
b_v2 = expressionotron.v002.expr_builder


VALID_VERSION_NUMBERS = (b_v1.version, b_v2.version)
CURRENT_EXPR_VERSION = b_v2.version
SEPARATOR_SEED = "_"


def makeValidSeed(strSeed):
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
    return (strVersion, digest, strSeed)


