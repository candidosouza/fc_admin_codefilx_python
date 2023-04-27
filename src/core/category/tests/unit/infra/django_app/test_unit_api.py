import unittest
from datetime import datetime
from unittest import mock

from core.category.application.use_cases import (
    CreateCategoryUseCase
)
from core.category.infra.django.api import CategoryResource

from rest_framework.request import Request
from rest_framework.test import APIRequestFactory


class TestCategoryResourceUnit(unittest.TestCase):

    def test_post_method(self):
        send_data = {
            'name': 'Movie',
        }
        mock_create_use_case = mock.Mock(CreateCategoryUseCase)
        mock_create_use_case.execute.return_value = CreateCategoryUseCase.Output(
            id='a849156c-fbc3-4dc0-a479-8179c6db099b',
            name='Movie',
            description=None,
            is_active=True,
            created_at=datetime.now(),
        )
        resource = CategoryResource(
            create_use_case=lambda: mock_create_use_case,
            list_use_case=None
        )
        _request = APIRequestFactory().post('/categories/', send_data)
        request = Request(_request)
        request._full_data = send_data  # pylint: disable=protected-access
        response = resource.post(request)
        mock_create_use_case.execute.assert_called_with(
            CreateCategoryUseCase.Input(
                name='Movie',
            ))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, {
            'id': 'a849156c-fbc3-4dc0-a479-8179c6db099b',
            'name': 'Movie',
            'description': None,
            'is_active': True,
            # 'created_at': mock.ANY,
            # 'created_at': created_at,
            'created_at': mock_create_use_case.execute.return_value.created_at,
        })
