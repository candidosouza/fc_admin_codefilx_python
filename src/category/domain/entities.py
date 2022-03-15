
class Category:

    __slots__ = ['__name']

    def __init__(self, name) -> None:
        self.__name = name

    def __str__(self) -> str:
        return f'Category {self.__name}'
 