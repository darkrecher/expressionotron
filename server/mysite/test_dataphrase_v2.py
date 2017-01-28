import expressionotron.v002.dataphrase
v2phrase = expressionotron.v002.dataphrase

def test_no_strange_char_in_raw_strings():

    total_string = '\n'.join((
        v2phrase.RAW_STRING_VERBS,
        v2phrase.RAW_STRING_SUBJECTS,
        v2phrase.RAW_STRING_ADJ_PREFIXES,
        v2phrase.RAW_STRING_ADJECTIVES,
        v2phrase.RAW_STRING_WHATEVERS,
        v2phrase.RAW_STRING_INTERJECTIONS))

    # Les caractères ASCII mais pas tous.
    AUTHORIZED_CHARS = (''
        ' !"#$%&\'()*+,-./0123456789:;=?'
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        '[]_`'
        'abcdefghijklmnopqrstuvwxyz'
        '{|}~')

    all_ok = True
    for line in total_string.split('\n'):
        for char in line:
            if char not in AUTHORIZED_CHARS:
                print(line)
                all_ok = False

    assert all_ok







