"""Perform primality testing with an exhaustive and efficient approaches."""

from pyinstrument import Profiler  # type: ignore

from typing import Any
from typing import Iterable
from typing import List
from typing import Tuple
from typing import Union

from enum import Enum

import random

import typer

from rich.console import Console

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a Profiler object to support timing program code segments
profiler = Profiler()


class IntersectionApproach(str, Enum):
    """Define the name for the approach for performing intersection of structured types."""

    list = "list"
    tuple = "tuple"
    set = "set"


def human_readable_boolean(answer: bool) -> str:
    """Produce a human-readable Yes or No for a boolean value of True or False."""
    # the provided answer is True
    if answer:
        return "Yes"
    # the provided answer is False
    return "No"


def pretty_print_list(values: Iterable[int]) -> str:
    """Pretty print a list without brackets and adding commas."""
    # create and return a version of the list without brackets
    # and with commas in between all of the values
    return ", ".join(map(str, values))


def generate_random_list(size: int, make_tuple: bool = False) -> Union[List[int], Tuple[int, ...]]:
    """Generate a random list defined by the size."""
    random_list = [random.randrange(1, 25, 1) for _ in range(size)]
    if make_tuple:
        return tuple(random_list)
    return random_list


def compute_intersection_list(input_one: List[Any], input_two: List[Any]) -> List[Any]:
    """Compute the intersection of two provided lists."""
    result = []
    for x in input_one:
        for y in input_two:
            if x == y:
                result.append(y)
    return result


def compute_intersection_tuple(input_one: Tuple[Any, ...], input_two: Tuple[Any, ...]) -> Tuple[Any, ...]:
    """Compute the intersection of two provided tuples."""
    result = ()
    for element in input_one:
        if element in input_two:
            result += (element,)
    return result


@cli.command()
def intersection(
    number: int = typer.Option(5),
    profile: bool = typer.Option(False),
    display: bool = typer.Option(False),
    approach: IntersectionApproach = IntersectionApproach.tuple,
) -> None:
    """Compute the intersection of data containers."""
    # create a console for rich text output
    console = Console()
    # create the starting data containers with no contents
    input_one = None
    input_two = None
    # create a starting output variable for the intersection computation
    intersection_output = None
    # use the intersection algorithm that works on an input list
    if approach.value == IntersectionApproach.list:
        # generate the two lists of random values
        input_one = generate_random_list(number)
        input_two = generate_random_list(number)
        # perform profiling on the execution of the intersection algorithm
        if profile:
            profiler.start()
            intersection_output = compute_intersection_list(list(input_one), list(input_two))
            profiler.stop()
        # do not perform profiling on the intersection algorithm
        else:
            intersection_output = compute_intersection_list(list(input_one), list(input_two))
    # display the input sets and the result of running the computation
    if display:
        console.print(":sparkles: Here are the details about the intersection computation!")
        console.print()
        console.print(f"Performed intersection with the first data container: {input_one}")
        console.print(f"Performed intersection with the second data container: {input_two}")
        console.print(f"Computed the intersection as the data container: {intersection_output}")
    # display the results of the profiling if that option was requested
    if profile:
        console.print()
        console.print(
            f":microscope: Here's profiling data from computing an intersection with random data containers of size {number}!"
        )
        profiler.print()
