from dataclasses import asdict

from sqlalchemy import select

from fast_zero.models import User

test_number = '12345678'


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(username='alice', password=test_number,
                        email='teste@test')
        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == 'alice'))

    assert asdict(user) == {
        'id': 1,
        'username': 'alice',
        'password': test_number,
        'email': 'teste@test',
        'created_at': time,
        'updated_at': time,
    }