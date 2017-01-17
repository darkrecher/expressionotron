# python -m py.test


from expressionotron.v002.dataphrase import (
    RAW_STRING_VERBS,
    RAW_STRING_SUBJECTS,
    RAW_STRING_ADJ_PREFIXES,
    RAW_STRING_ADJECTIVES,
    RAW_STRING_WHATEVERS,
    RAW_STRING_INTERJECTIONS)


def test_no_strange_char_in_raw_strings():

    total_string = "\n".join((
        RAW_STRING_VERBS,
        RAW_STRING_SUBJECTS,
        RAW_STRING_ADJ_PREFIXES,
        RAW_STRING_ADJECTIVES,
        RAW_STRING_WHATEVERS,
        RAW_STRING_INTERJECTIONS))

    # Les caractères ASCII mais pas tous.
    AUTHORIZED_CHARS = "".join((
        " !\"#$%&'()*+,-./0123456789:;=?",
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "[]_`",
        "abcdefghijklmnopqrstuvwxyz",
        "{|}~"))

    all_ok = True
    for line in total_string.split("\n"):
        for char in line:
            if char not in AUTHORIZED_CHARS:
                print(line)
                all_ok = False

    assert all_ok







