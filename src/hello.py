from pydantic import BaseModel

def greet(name: str) -> str:
    """
    Generate a friendly greeting message.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A formatted greeting message including the provided name.
    """
    return f"Hello, {name}!"


class Korte(BaseModel):
    """
    Example data model representing a simple entity.

    Attributes:
        bbb (str): A string field with a default value of "aaaaaaaa".
    """
    bbb: str = "aaaaaaaa"

    def alma(a: str) -> None:
        """
        Print the provided string argument.

        Args:
            a (str): The string to be printed.
        """
        print(a)


def alma() -> None:
    """
    Print a fixed message.

    This function demonstrates a simple print statement
    with a hardcoded string.

    Returns:
        None
    """
    print("korte")


class Animal(BaseModel):
    """
    Base class representing a generic animal.

    Attributes:
        name (str): The name of the animal.
    """

class Dog(Animal):
    """
    A subclass of `Animal` representing a dog.

    Inherits:
        - `name` from Animal

    Attributes:
        breed (str): The breed of the dog.
    """

class Cat(Animal):
    """
    A subclass of `Animal` representing a cat.

    Inherits:
        - `name` from Animal

    Attributes:
        color (str): The color of the cat.
    """
