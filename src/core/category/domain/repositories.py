from abc import ABC
from core.__seedwork.domain.repositories import (
    SearchParams as DesfaultSearchParams,
    SearchResult as DefaultSearchResult,
    SearchableRepositoryInterface
)
from core.category.domain.entities import Category


class _SearchParams(DesfaultSearchParams):
    pass


class _SearchResult(DefaultSearchResult):
    pass


class CategoryRepository(SearchableRepositoryInterface[Category, _SearchParams, _SearchResult], ABC):
    SearchParams = _SearchParams
    SearchResult = _SearchResult
