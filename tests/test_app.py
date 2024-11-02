from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root():
    """Teste para a rota raiz."""
    client = TestClient(app)  # Arrange (Preparação)

    response = client.get('/')  # Act (Ação)

    assert response.status_code == HTTPStatus.OK  # Assert (Verificação)
    assert response.json() == {'message': 'Hello World'}
