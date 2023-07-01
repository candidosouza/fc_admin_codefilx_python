from dependency_injector import containers, providers

from core.category.infra.in_memory.repositories import CategoryInMemoryRepository
from core.category.infra.django_app.repositories import CategoryDjangoRepository
from core.category.application.use_cases import (
    CreateCategoryUseCase,
    GetCategoryUseCase,
    ListCategoriesUseCase,
    UpdateCategoryUseCase,
    DeleteCategoryUseCase,
)


class Container(containers.DeclarativeContainer):  # pylint: disable=too-few-public-methods, c-extension-no-member
    repository_category_in_memory = providers.Singleton(  # pylint: disable=c-extension-no-member
        CategoryInMemoryRepository
    )

    repository_category_django_orm = providers.Singleton(  # pylint: disable=c-extension-no-member
        CategoryDjangoRepository
    )

    use_case_category_create_category = providers.Singleton(  # pylint: disable=c-extension-no-member
        CreateCategoryUseCase,
        category_repository=repository_category_django_orm
    )

    use_case_category_list_categories = providers.Singleton(  # pylint: disable=c-extension-no-member
        ListCategoriesUseCase,
        category_repository=repository_category_django_orm
    )

    use_case_category_get_category = providers.Singleton(  # pylint: disable=c-extension-no-member
        GetCategoryUseCase,
        category_repository=repository_category_django_orm
    )

    use_case_category_update_category = providers.Singleton(  # pylint: disable=c-extension-no-member
        UpdateCategoryUseCase,
        category_repository=repository_category_django_orm
    )

    use_case_category_delete_category = providers.Singleton(  # pylint: disable=c-extension-no-member
        DeleteCategoryUseCase,
        category_repository=repository_category_django_orm
    )
