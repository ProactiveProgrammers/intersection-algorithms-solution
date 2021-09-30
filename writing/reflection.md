# Intersection Algorithms

## Gregory M. Kapfhammer

## Program Output

### Use eight fenced code blocks to provide output from eight different runs of `intersection` with different inputs

Note: Summary of the runs for the List-based algorithms:

Note: Summary of the runs for the ListSingle algorithm:
Run 1: ListSingle with a small input
Run 2: ListSingle with a large input

Note: Summary of the runs for the ListDouble algorithm:
Run 1: ListDouble with a small input
Run 2: ListDouble with a large input

Note: Summary of the runs for the Tuple-based algorithms:

Note: Summary of the runs for the TupleSingle algorithm:
Run 1: TupleSingle with a small input
Run 2: TupleSingle with a large input

Note: Summary of the runs for the ListDouble algorithm:
Run 1: ListDouble with a small input
Run 2: ListDouble with a large input

Note: Whenever possible, please use the same "small" and "large" inputs for both
the List-based and Tuple-based algorithms.

Note: Do not run the program with the `--display` option when conducting
experiments!

#### Two outputs from running the `ListSingle` algorithm with different inputs

```
output
```

```
output
```

#### Two outputs from running the `ListDouble` algorithm with different inputs

```
output
```

```
output
```

#### Two outputs from running the `TupleSingle` algorithm with different inputs

```
output
```

```
output
```

#### Two outputs from running the `TupleDouble` algorithm with different inputs

```
output
```

```
output
```

## Performance Analysis

Note: Provide three paragraphs that explain which algorithm is fastest, by how
much it is faster, and how you knew that the it was faster, referencing the data
in the aforementioned command outputs to support your response. You should make
sure that you answer the following research questions:

- RQ: Is intersection faster with a list or a tuple?
- RQ: Is intersection faster with a double-for-loop or a single-for-loop?
- RQ: Overall, what is the fastest approach for computing the intersection?

Note: Make sure that your responses explain WHY certain algorithms are faster!

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
no sea takimata sanctus est Lorem ipsum dolor sit amet.

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
no sea takimata sanctus est Lorem ipsum dolor sit amet.

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
no sea takimata sanctus est Lorem ipsum dolor sit amet.

## Source Code

### Describe in detail how the completed source code works

#### A class that defines the four algorithmic options for running the experiment

Note: Use a fenced code block to provide the requested source code
Note: Write at least one paragraph to explain the request source code

```
class IntersectionApproach(str, Enum):
    """Define the name for the approach for performing intersection of structured types."""

    list_single = "ListSingle"
    tuple_single = "TupleSingle"
    list_double = "ListDouble"
    tuple_double = "TupleDouble"
```

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

#### A function signature that defines the command-line interface for `intersection`

Note: Use a fenced code block to provide the requested source code
Note: Write at least one paragraph to explain the request source code
Note: Explain each of the command-line arguments for this program

```
def intersection(
    number: int = typer.Option(5),
    maximum: int = typer.Option(25),
    profile: bool = typer.Option(False),
    display: bool = typer.Option(False),
    approach: IntersectionApproach = IntersectionApproach.tuple_single,
) -> None:
```

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
no sea takimata sanctus est Lorem ipsum dolor sit amet.

#### A function that can generate a data container with random values in it

Note: Use a fenced code block to provide the requested source code
Note: Write at least one paragraph to explain the request source code
Note: Explain each line of source code in this function

```
def generate_random_container(
    size: int, maximum: int, make_tuple: bool = False
) -> Union[List[int], Tuple[int, ...]]:
    """Generate a random list defined by the size."""
    random_list = [random.randrange(1, maximum, 1) for _ in range(size)]
    if make_tuple:
        return tuple(random_list)
    return random_list
```

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

### What was the greatest challenge that you faced when completing this assignment?

Note: Provide a one-paragraph response that answers this question in your own words.

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

### Leveraging your response to the previous question, how did you overcome the challenge?

Note: Provide a one-paragraph response that answers this question in your own words.

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
