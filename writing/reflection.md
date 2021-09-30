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

#### Two outputs from running the `ListSingle` algorithm with different inputs

#### Two outputs from running the `ListDouble` algorithm with different inputs

#### Two outputs from running the `TupleSingle` algorithm with different inputs

#### Two outputs from running the `TupleDouble` algorithm with different inputs

## Performance Analysis

Note: Provide one paragraph that states which algorithm is fastest, by how much
it is faster, and how you knew that the it was faster, referencing the data in
the aforementioned command outputs to support your response.

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

#### A function that converts a `bool` into a human readable `str` value

Note: Use a fenced code block to provide the requested source code
Note: Write at least one paragraph to explain the request source code

```
def human_readable_boolean(answer: bool) -> str:
    """Produce a human-readable Yes or No for a boolean value of True or False."""
    # the provided answer is True
    if answer:
        return "Yes"
    # the provided answer is False
    return "No"
```

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

#### A function signature that defines the command-line interface for `intersection`

Note: Use a fenced code block to provide the requested source code
Note: Write at least one paragraph to explain the request source code

```
@cli.command()
def intersection(
    number: int = typer.Option(5),
    profile: bool = typer.Option(False),
    approach: intersectionTestingApproach = intersectionTestingApproach.efficient,
) -> None:
```

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
no sea takimata sanctus est Lorem ipsum dolor sit amet.

### What was the greatest challenge that you faced when completing this assignment?

Note: Provide a one-paragraph response that answers this question in your own words.

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

### Based on your experiences with this project, what is one way in which you want to improve?

Note: Provide a one-paragraph response that answers this question in your own words.

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
