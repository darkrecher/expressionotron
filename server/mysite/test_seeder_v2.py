import itertools
import functools
import operator

import expressionotron.v002.seeder
data_indexes_from_seed = expressionotron.v002.seeder.data_indexes_from_seed


def test_seeder_doctest():
    import doctest
    (failure_count, test_count) = doctest.testmod(expressionotron.v002.seeder)
    assert failure_count == 0


def test_coverage_nominal():
    """ Test de couverture sur plage restreinte. """
    data_index_lengths = (2, 4, 5)
    total_length = 2*4*5
    data_indexes_to_cover = list(itertools.product(
        range(2), range(4), range(5)))

    # Pour faire foirer le test :
    # data_indexes_to_cover[10] = (1, 2, 3)
    data_indexes_obtained = [
        data_indexes_from_seed(data_index_lengths, seed)
        for seed in range(total_length) ]

    assert data_indexes_obtained[0] == (0, 0, 0)
    data_indexes_obtained.sort()
    assert data_indexes_obtained == data_indexes_to_cover


def test_coverage_big():
    """ Test de couverture plus générique, sur une plage plus grande. """
    data_index_lengths = (1, 5, 20, 40, 45)
    total_length = functools.reduce(operator.mul, data_index_lengths)
    data_indexes_lists = [
        range(data_index_length)
        for data_index_length in data_index_lengths ]
    data_indexes_to_cover = list(itertools.product(*data_indexes_lists))

    # Pour faire foirer le test :
    # data_indexes_to_cover[total_length//2] = (1, 2, 3, 4, 5)
    data_indexes_obtained = [
        data_indexes_from_seed(data_index_lengths, seed)
        for seed in range(total_length) ]

    assert data_indexes_obtained[0] == (0, 0, 0, 0, 0)
    data_indexes_obtained.sort()
    assert data_indexes_obtained == data_indexes_to_cover


def test_coverage_shuffle():
    """ Test de couverture sur plage raisonnable, avec des shufflers. """
    data_index_lengths = (10, 12, 14)
    shufflers = (
        (0, 4, 9, 3, 8, 1, 5, 7, 6, 2),
        (9, 5, 3, 1, 7, 4, 0, 10, 6, 8, 11, 2),
        (9, 11, 0, 7, 10, 5, 12, 4, 13, 2, 1, 3, 8, 6),
    )
    total_length = functools.reduce(operator.mul, data_index_lengths)
    data_indexes_lists = [
        range(data_index_length)
        for data_index_length in data_index_lengths ]
    data_indexes_to_cover = list(itertools.product(*data_indexes_lists))

    # Pour faire foirer le test :
    # data_indexes_to_cover[10] = (1, 2, 3)
    data_indexes_obtained = [
        data_indexes_from_seed(data_index_lengths, seed, shufflers)
        for seed in range(total_length) ]

    # Les shuflers ont méga-mélangés les index,
    # le premier n'est plus celui avec les 0.
    assert data_indexes_obtained[0] != (0, 0, 0)
    data_indexes_obtained.sort()
    assert data_indexes_obtained == data_indexes_to_cover


def test_coverage_random():
    """ Test de couverture random, avec shuffle random aussi. """
    import random
    nb_data_index = random.randrange(5) + 2
    data_index_lengths = []
    current_lengths = 1
    for i in range(nb_data_index):
        current_lengths += random.randrange(4)
        data_index_lengths.append(current_lengths)
    print('data_index_lengths :', data_index_lengths)

    # Renvoyer une liste mélangée : http://stackoverflow.com/a/12978830
    shufflers = [
        random.sample(range(data_index_length), data_index_length)
        for data_index_length in data_index_lengths ]
    print('shufflers :', shufflers)

    total_length = functools.reduce(operator.mul, data_index_lengths)
    data_indexes_lists = [
        range(data_index_length)
        for data_index_length in data_index_lengths ]
    data_indexes_to_cover = list(itertools.product(*data_indexes_lists))

    data_indexes_obtained = [
        data_indexes_from_seed(data_index_lengths, seed, shufflers)
        for seed in range(total_length) ]

    data_indexes_obtained.sort()
    assert data_indexes_obtained == data_indexes_to_cover


def test_no_proximity():
    """
    Test de non-proximité des seeds, sur une grande plage, sans shuffle.
    """
    data_index_lengths = (5, 20, 40, 45)
    # Pour faire foirer le test :
    # (la non-proximité ne marche pas bien si la plage est petite)
    # data_index_lengths = (4, 6, 7)

    total_length = functools.reduce(operator.mul, data_index_lengths)

    previous_data_indexes = data_indexes_from_seed(data_index_lengths, 0)
    for seed in range(1, total_length):
        current_data_indexes = data_indexes_from_seed(data_index_lengths, seed)
        differences = [
            (prev, cur)
            for (prev, cur)
            in zip(previous_data_indexes, current_data_indexes)
            if prev != cur ]
        assert len(differences) == len(data_index_lengths)
        previous_data_indexes = current_data_indexes



