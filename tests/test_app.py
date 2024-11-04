from http import HTTPStatus


def test_read_root(client):
    """Teste para a rota raiz."""
    response = client.get('/')  # Act (Ação)

    assert response.status_code == HTTPStatus.OK  # Assert (Verificação)
    assert response.json() == {'message': 'Hello World'}


def test_create_user(client):
    """Teste para a rota de criação de usuário."""
    response = client.post(
        '/users/',
        json={
            'username': 'F1234567',
            'password': '12345678',
            'email': 'user@test.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED  # Assert (Verificação)
    assert response.json() == {
        'id': 0,
        'username': 'F1234567',
        'email': 'user@test.com',
    }


def test_read_users(client):
    """Teste para a rota de leitura de usuários."""
    response = client.get('/users/')  # Act (Ação)

    assert response.status_code == HTTPStatus.OK  # Assert (Verificação)
    assert response.json() == {
        'users': [
            {
                'id': 0,
                'username': 'F1234567',
                'email': 'user@test.com',
            }
        ]
    }


def test_update_user(client):
    """Teste para a rota de atualização de usuário."""
    response = client.put(
        '/users/0',
        json={
            'password': '12345678',
            'username': 'T7654321',
            'email': 'user@test.com',
        },
    )

    assert response.json() == {
        'username': 'T7654321',
        'email': 'user@test.com',
        'id': 0,
    }

    response = client.put(
        '/users/1',
        json={
            'password': '12345678',
            'username': 'T7654321',
            'email': 'user@test.com',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND  # Assert (Verificação)
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    """Teste para a rota de deleção de usuário."""
    response = client.delete('/users/0')  # Act (Ação)

    assert response.status_code == HTTPStatus.OK  # Assert (Verificação)
    assert response.json() == {'message': 'User deleted'}

    response = client.delete('/users/1')  # Act (Ação)

    assert response.status_code == HTTPStatus.NOT_FOUND  # Assert (Verificação)
    assert response.json() == {'detail': 'User not found'}
