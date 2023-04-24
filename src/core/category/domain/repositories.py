from abc import ABC
from core.__seedwork.domain.repositories import RepositoryInterface
from core.category.domain.entities import Category

class CategoryRepository(RepositoryInterface[Category], ABC):
    pass