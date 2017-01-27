def tuple_from_raw_str(raw_str):
    """
    Renvoie un tuple à partir d'une string multi-ligne, en éliminant les
    espaces avant et après chaque string, et en éliminant les lignes vides.

    :Example:

    >>> a = "  bonjour \\n  \\n\\nau revoir\\n"
    >>> tuple_from_raw_str(a)
    ('bonjour', 'au revoir')
    """
    elems_stripped = ( elem.strip() for elem in raw_str.split('\n') )
    elems_stripped_filtered = ( elem for elem in elems_stripped if elem )
    return tuple(elems_stripped_filtered)
