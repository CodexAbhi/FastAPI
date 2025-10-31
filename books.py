from fastapi import Body, FastAPI

app=FastAPI()

Books=[{"title":"Book 1", "author": "Author 1", "category": "science"},
       {"title":"Book 2", "author": "Author 2", "category": "science"},
       {"title":"Book 3", "author": "Author 3", "category": "history"},
       {"title":"Book 4", "author": "Author 4", "category": "maths"},
       {"title":"Book 5", "author": "Author 5", "category": "maths"}]

@app.get("/books")
async def read_all_books():
    return Books

@app.get("/books/{book_title}")
async def get_book(book_title: str):
    for book in Books:
        if(book.get('title').casefold()==book_title.casefold()):
            return book
        
@app.get("/books/{author}/")
async def get_book_by_author(author: str, category: str):
    books_to_return=[]
    for book in Books:
        if book.get('author').casefold()==author.casefold() and book.get('category').casefold()==category.casefold():
            books_to_return.append(book)

    return books_to_return

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    Books.append(new_book)

@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(Books)):
        if Books[i].get('title').casefold()==updated_book.get('title').casefold():
            Books[i]=updated_book

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(Books)):
        if Books[i].get('title').casefold()==book_title.casefold():
            Books.pop(i)
            break

@app.get("/books/byauthor/{author}")
async def read_books_by_author_path(author:str):
    books_to_return=[]
    for book in Books:
        if book.get('author').casefold()==author.casefold():
            books_to_return.append(book)