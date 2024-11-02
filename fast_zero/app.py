from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    """Root endpoint that returns a greeting message."""
    return {'message': 'Hello World'}


@app.get('/items/{item_id}')
def read_item(item_id: int, q: str | None = None):
    """Endpoint to read an item by its ID and an optional query parameter."""
    return {'item_id': item_id, 'q': q}
