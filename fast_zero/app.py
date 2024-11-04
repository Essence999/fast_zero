from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from fast_zero.schemas import Message, User, UserInDB, UserList, UserPublic

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    """Return a simple message."""
    return {'message': 'Hello World'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: User):
    """Create a user."""
    user_with_id = UserInDB(id=len(database), **user.model_dump())

    database.append(user_with_id)

    return user_with_id


@app.get('/users/', response_model=UserList)
def read_users():
    """Return all users."""
    return {'users': database}


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: User):
    """Update a user."""
    if user_id < 0 or user_id > len(database) - 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='User not found')

    user_with_id = UserInDB(id=user_id, **user.model_dump())
    database[user_id] = user_with_id

    return user_with_id


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    """Delete a user."""
    if user_id < 0 or user_id > len(database) - 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='User not found')

    del database[user_id]

    return {'message': 'User deleted'}
