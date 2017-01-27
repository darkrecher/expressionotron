# Ce fichier de code ne sert plus à grand chose.
# Il m'a juste permis de lister les morceaux de phrases dans le bon ordre,
# pour détecter les doublons.


from expressionotron.v002.dataphrase import (
    RAW_STRING_VERBS,
    RAW_STRING_SUBJECTS,
    RAW_STRING_ADJ_PREFIXES,
    RAW_STRING_ADJECTIVES,
    RAW_STRING_WHATEVERS,
    RAW_STRING_INTERJECTIONS)


def list_from_raw_string(raw_string):
    elems_stripped = (
        elem.strip()
        for elem in raw_string.split("\n") )
    elems_stripped_filtered = (
        elem
        for elem in elems_stripped
        if elem != "" )
    return list(elems_stripped_filtered)


def print_sorted_elems(raw_string):
    elems = list_from_raw_string(raw_string)
    elems.sort()
    print("    " + "\n    ".join(elems))


print('RAW_STRING_VERBS = """')
print_sorted_elems(RAW_STRING_VERBS)
print('"""')
print("")

print('RAW_STRING_SUBJECTS = """')
print_sorted_elems(RAW_STRING_SUBJECTS)
print('"""')
print("")

print('RAW_STRING_ADJ_PREFIXES = """')
print_sorted_elems(RAW_STRING_ADJ_PREFIXES)
print('"""')
print("")

print('RAW_STRING_ADJECTIVES = """')
print_sorted_elems(RAW_STRING_ADJECTIVES)
print('"""')
print("")

print('RAW_STRING_WHATEVERS = """')
print_sorted_elems(RAW_STRING_WHATEVERS)
print('"""')
print("")

print('RAW_STRING_INTERJECTIONS = """')
print_sorted_elems(RAW_STRING_INTERJECTIONS)
print('"""')
print("")


