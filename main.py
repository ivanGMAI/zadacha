import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, constr, EmailStr, ConfigDict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
books = [
    {
        'title': 'na zap bes peremen',
        'data': 1925,
        'pocht': 'hohol@mail.ru',
        'id': 1
    },
    {
        'title': 'titan',
        'data': 1912,
        'pocht': 'sos@mail.ru',
        'id': 2
    }
]


@app.get('/books', tags=['BOOM'], summary='NABLEVAL')
def read():
    return books


@app.get('/books/{book_id}', tags=['BOOM'], summary='NA')
def get_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=404, detail='idi gulai')


class Newbook(BaseModel):
    title: constr(max_length=50)
    data: int = Field(ge=1700, le=2024)
    pocht: EmailStr
    model_config = ConfigDict(extra="forbid")


@app.post('/books/pop', tags=['ADD'], summary='PRESS')
def create_book(new_book: Newbook):
    if any(book['title'] == new_book.title for book in books):
        raise HTTPException(status_code=404, detail='уже есть')
    new_id = len(books) + 1
    books.append({
        'title': new_book.title,
        'data': new_book.data,
        'pocht': new_book.pocht,
        'id': new_id
    })
    return {'ok': True}

@app.delete('/books/{book_id}', tags=['DELETE'], summary='Удалить книгу')
def delete_book(book_id: int):
    global books
    initial_length = len(books)
    books = [book for book in books if book['id'] != book_id]
    if len(books) == initial_length:
        raise HTTPException(status_code=404, detail='Книга не найдена')
    return {'ok': True}


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
