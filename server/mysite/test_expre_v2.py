from expressionotron.common_tools import tuple_from_raw_str
import expressionotron.v002.expr_builder


def test_shufflers_coverage():
    shufflers = expressionotron.v002.expr_builder.shufflers
    for shuffler in shufflers:
        shuffler_sorted = sorted(shuffler)
        # Pour faire foirer le test, décommenter la ligne ci-dessous
        # if shuffler == shufflers[-1]: shuffler_sorted[15] = 17
        assert shuffler_sorted == list(range(len(shuffler)))


def test_seed_size():
   seed_size = expressionotron.v002.expr_builder.seed_max
   assert seed_size == 151 * 141 * 173 * 158 * 150
   assert seed_size == 87295229100


def test_lengths_coherency():
    # On prend pas les RAW_STRING_ADJ_PREFIXES, c'est normal.
    # On s'en sert pas directement pour déterminer la quantité de hasard dispo.
    from expressionotron.v002.dataphrase import (
        RAW_STRING_VERBS, RAW_STRING_SUBJECTS,
        RAW_STRING_ADJECTIVES, RAW_STRING_WHATEVERS, RAW_STRING_INTERJECTIONS,
    )
    data_lengths = expressionotron.v002.expr_builder.data_lengths

    # Pour faire foirer le test, décommenter la ligne ci-dessous
    # RAW_STRING_ADJECTIVES += "\nhahahaha"
    raw_strings = (
        RAW_STRING_VERBS, RAW_STRING_SUBJECTS,
        RAW_STRING_ADJECTIVES, RAW_STRING_WHATEVERS, RAW_STRING_INTERJECTIONS,
    )
    expr_pieces_no_prefix = [
        tuple_from_raw_str(raw_string)
        for raw_string in raw_strings
    ]
    expr_piece_lengths = tuple(
        ( len(expr_piece) for expr_piece in expr_pieces_no_prefix )
    )
    assert data_lengths == expr_piece_lengths

    shufflers = expressionotron.v002.expr_builder.shufflers
    shuffler_lengths = tuple(
        ( len(shuffler) for shuffler in shufflers )
    )
    assert data_lengths == shuffler_lengths


def test_shufflers_reference():
    shufflers_reference = (
        (
            149, 36, 49, 41, 97, 4, 111, 83, 33, 46, 50, 58, 24, 8, 113, 130,
            31, 9, 112, 17, 109, 136, 15, 40, 131, 20, 35, 99, 27, 145, 63,
            116, 141, 84, 79, 28, 67, 71, 10, 5, 11, 93, 7, 45, 115, 121, 98,
            107, 101, 16, 117, 126, 127, 123, 138, 142, 85, 60, 92, 81, 21,
            44, 132, 51, 73, 64, 124, 139, 29, 140, 2, 96, 89, 57, 78, 43,
            110, 55, 144, 13, 87, 133, 75, 143, 137, 135, 48, 19, 95, 14, 106,
            52, 103, 69, 34, 56, 18, 147, 82, 146, 90, 22, 119, 105, 108, 6,
            128, 47, 59, 122, 104, 53, 150, 42, 25, 26, 1, 38, 68, 62, 125,
            134, 80, 61, 86, 30, 114, 0, 102, 70, 3, 91, 94, 148, 66, 129, 76,
            74, 100, 12, 32, 77, 88, 23, 39, 54, 120, 65, 118, 72, 37,
        ),
        (
            81, 140, 5, 0, 71, 128, 30, 8, 66, 14, 86, 115, 92, 24, 137, 76,
            131, 100, 37, 75, 32, 42, 58, 38, 11, 105, 136, 84, 85, 109, 68,
            106, 43, 48, 70, 110, 127, 10, 72, 20, 119, 89, 125, 7, 49, 9, 16,
            134, 27, 15, 12, 57, 91, 62, 90, 82, 31, 47, 93, 61, 44, 53, 13,
            69, 132, 139, 126, 98, 29, 123, 59, 17, 117, 78, 112, 120, 26, 55,
            138, 1, 39, 18, 19, 4, 83, 54, 56, 2, 135, 99, 129, 46, 107, 51,
            111, 67, 103, 33, 77, 102, 21, 113, 104, 28, 52, 22, 122, 23, 116,
            36, 97, 6, 96, 118, 50, 124, 87, 34, 101, 80, 65, 64, 130, 25, 79,
            88, 121, 108, 40, 60, 95, 45, 133, 74, 41, 94, 63, 73, 3, 114, 35,
        ),
        (
            147, 44, 60, 134, 49, 89, 29, 121, 59, 96, 69, 107, 128, 115, 7,
            153, 17, 112, 85, 87, 158, 92, 75, 156, 169, 137, 129, 25, 94, 144,
            3, 40, 113, 84, 152, 31, 101, 98, 63, 51, 157, 168, 14, 150, 15,
            81, 114, 142, 37, 5, 78, 170, 118, 18, 43, 64, 28, 130, 61, 65,
            135, 136, 33, 80, 166, 24, 154, 167, 127, 93, 50, 108, 124, 88, 36,
            119, 77, 139, 12, 38, 53, 97, 22, 125, 106, 79, 20, 131, 105, 171,
            138, 27, 172, 140, 72, 46, 67, 42, 30, 86, 155, 76, 23, 1, 83, 9,
            74, 161, 16, 132, 8, 145, 90, 102, 149, 66, 143, 109, 162, 45, 2,
            117, 160, 82, 100, 10, 104, 141, 6, 39, 41, 91, 62, 34, 56, 58, 4,
            126, 111, 163, 11, 70, 71, 21, 146, 151, 116, 35, 99, 48, 19, 55,
            164, 54, 110, 73, 120, 165, 159, 122, 133, 52, 68, 57, 148, 47, 32,
            13, 95, 0, 103, 26, 123,
        ),
        (
            17, 99, 6, 139, 109, 80, 23, 72, 84, 98, 40, 29, 120, 127, 13, 30,
            107, 61, 87, 51, 130, 103, 114, 67, 54, 63, 18, 36, 116, 10, 77,
            119, 144, 94, 48, 73, 121, 45, 79, 62, 138, 49, 124, 126, 14, 122,
            7, 92, 2, 157, 141, 147, 25, 125, 137, 152, 37, 146, 113, 132, 112,
            58, 76, 21, 50, 133, 90, 28, 33, 42, 83, 1, 115, 60, 106, 111, 4,
            136, 96, 154, 31, 27, 105, 123, 117, 102, 39, 153, 3, 118, 47, 101,
            131, 91, 52, 78, 151, 15, 93, 11, 143, 155, 110, 70, 35, 129, 145,
            104, 88, 66, 8, 56, 142, 86, 24, 19, 81, 16, 140, 43, 20, 59, 5,
            12, 69, 55, 128, 41, 38, 89, 97, 75, 134, 149, 57, 100, 135, 65,
            85, 44, 156, 82, 64, 68, 26, 9, 148, 95, 53, 22, 46, 108, 32, 0,
            74, 34, 150, 71,
        ),
        (
            20, 133, 28, 102, 80, 143, 85, 90, 24, 131, 34, 62, 63, 108, 106,
            116, 87, 67, 37, 84, 127, 18, 100, 70, 146, 107, 104, 21, 69, 36,
            72, 48, 81, 61, 19, 110, 74, 44, 9, 12, 49, 89, 126, 65, 32, 1, 46,
            132, 119, 29, 53, 79, 113, 103, 139, 56, 51, 59, 31, 115, 109, 134,
            114, 95, 60, 96, 94, 50, 71, 105, 33, 41, 47, 75, 148, 144, 23, 8,
            66, 93, 121, 15, 129, 124, 138, 27, 64, 101, 68, 26, 99, 0, 39, 98,
            122, 125, 77, 5, 86, 130, 30, 10, 40, 16, 83, 149, 76, 25, 42, 120,
            35, 136, 117, 111, 17, 137, 22, 57, 112, 52, 145, 4, 78, 43, 45, 7,
            123, 2, 55, 13, 147, 92, 73, 118, 88, 6, 38, 140, 141, 97, 128, 3,
            14, 142, 11, 91, 58, 54, 135, 82,
        )
    )
    assert expressionotron.v002.expr_builder.shufflers == shufflers_reference

