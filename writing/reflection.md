# Intersection Algorithms

## Gregory M. Kapfhammer

## Program Output

### Use six fenced code blocks to provide output from six different runs of `primality` with different inputs

Note: Pick three different input values and run then each with
(a) the exhaustive algorithm
and
(b) the efficient algorithm

#### Three outputs from running the exhaustive algorithm

Note: Provide the specific command that you ran to produce this output
Note: Use a fenced code block to provide the output for this command.

- `poetry run primality --number 49979687 --approach efficient --profile`

```
😄 Attempting to determine if 49979687 is a prime number!

✨ What divisors were found? 1, 49979687
✨ Was this a prime number? Yes

🔬 Here's profile data from performing primality testing on {number}!

  _     ._   __/__   _ _  _  _ _/_   Recorded: 14:03:54  Samples:  1
 /_//_/// /_\ / //_// / //_'/ //     Duration: 0.895     CPU time: 0.895
/   _/                      v4.0.3

Program: primality --number 49979687 --approach efficient --profile

0.895 square  primality/main.py:93
└─ 0.895 primality_test_efficient  primality/main.py:77
```

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

#### A function signature that defines the command-line interface for `primality`

Note: Use a fenced code block to provide the requested source code
Note: Write at least one paragraph to explain the request source code

```
@cli.command()
def primality(
    number: int = typer.Option(5),
    profile: bool = typer.Option(False),
    approach: PrimalityTestingApproach = PrimalityTestingApproach.efficient,
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
