from core.__seedwork.domain.repositories import InMemoryRepository
from core.category.domain.repositories import CategoryRepository


class CategoryInMemoryRepository(CategoryRepository, InMemoryRepository):
    pass
