from dependency_injector import containers, providers

from core.category.infra.in_memory.repositories import CategoryInMemoryRepository
from core.category.application.use_cases import (
    CreateCategoryUseCase,
    ListCategoriesUseCase
)


class Container(containers.DeclarativeContainer):  # pylint: disable=too-few-public-methods, c-extension-no-member
    repository_category_in_memory = providers.Singleton(  # pylint: disable=c-extension-no-member
        CategoryInMemoryRepository
    )

    use_case_category_create_category = providers.Singleton(  # pylint: disable=c-extension-no-member
        CreateCategoryUseCase,
        category_repository=repository_category_in_memory
    )

    use_case_category_list_categories = providers.Singleton(  # pylint: disable=c-extension-no-member
        ListCategoriesUseCase,
        category_repository=repository_category_in_memory
    )
