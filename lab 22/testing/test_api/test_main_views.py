from starlette.testclient import TestClient
from fastapi import status
import pytest

from main import app

client = TestClient(app=app)

def test_root_view():
    response = client.get('/')
    response_data = response.json()
    expected_message = 'Hello, World!'

    assert response.status_code == status.HTTP_200_OK
    assert response_data['docs'] == '/docs'
    assert response_data['message'] == expected_message

@pytest.mark.parametrize(
        'name',
        [
            'BGPU',
            'Bob',
            '',
            '!@@####$$$',
        ]
)
def test_root_view_custom_name(name: str):
    query = {'name': name}
    response = client.get('/', params=query)
    response_data = response.json()
    expected_message = f'Hello, {name}!'

    assert response.status_code == status.HTTP_200_OK
    assert response_data['docs'] == '/docs'
    assert response_data['message'] == expected_message