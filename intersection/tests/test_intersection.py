"""Test suite to ensure that each function words correctly."""

from intersection import __version__

from intersection import main


def test_version():
    """Confirm that the version of the program is correct."""
    assert __version__ == "0.1.0"


def test_generate_random_container_list():
    """Ensure that generation of random container is correct size."""
    random_container = main.generate_random_container(10, 100, False)
    assert len(random_container) == 10


def test_intersection_list_single_double():
    """Ensure that intersection works for both of the list algorithms."""
    first_list = [1, 2, 3, 4, 5]
    second_list = [4, 5, 6, 7, 8]
    intersection_single = main.compute_intersection_list_single(first_list, second_list)
    assert len(intersection_single) == 2
