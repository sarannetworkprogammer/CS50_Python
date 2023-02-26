"""
doc string format to analyze generate pages convert to pdf or

type hints
what it returns
take input
can we define multiple init methods great question
strong suggestion use mypy tool to detect errors



"""


def meow(n: int) -> str:

    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows , one per line
    :returntype : str
    """

    return ("meow\n" * n)


number: int = int(input("Number: "))

meows: str = meow(number)

print(meows, end="")