import sqlite3
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    status: str


@dataclass
class Reader:
    id: int
    name: str
    age: int


class Library:
    def __init__(self, db_name="library.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        create table if not exists books (
            id integer primary key autoincrement,
            title text,
            author text,
            year integer,
            status text check(status in ('available','borrowed')) default 'available'
        )
        """)

        self.cursor.execute("""
        create table if not exists readers (
            id integer primary key autoincrement,
            name text,
            age integer
        )
        """)

        self.cursor.execute("""
        create table if not exists borrowed_books (
            reader_id integer,
            book_id integer,
            borrow_date text,
            foreign key(reader_id) references readers(id),
            foreign key(book_id) references books(id)
        )
        """)

        self.conn.commit()

    def add_book(self, title, author, year):
        self.cursor.execute(
            "insert into books (title, author, year, status) values (?, ?, ?, 'available')",
            (title, author, year)
        )
        self.conn.commit()
        print("книга добавлена")

    def add_reader(self, name, age):
        self.cursor.execute(
            "insert into readers (name, age) values (?, ?)",
            (name, age)
        )
        self.conn.commit()
        print("читатель добавлен")

    def borrow_book(self, reader_id, book_id):
        self.cursor.execute(
            "select status from books where id = ?",
            (book_id,)
        )
        book = self.cursor.fetchone()

        if book and book[0] == "available":
            self.cursor.execute(
                "update books set status = 'borrowed' where id = ?",
                (book_id,)
            )

            self.cursor.execute(
                "insert into borrowed_books (reader_id, book_id, borrow_date) values (?, ?, ?)",
                (reader_id, book_id, datetime.now().strftime("%Y-%m-%d"))
            )

            self.conn.commit()
            print("книга выдана")
        else:
            print("книга недоступна")

    def return_book(self, book_id):
        self.cursor.execute(
            "update books set status = 'available' where id = ?",
            (book_id,)
        )

        self.cursor.execute(
            "delete from borrowed_books where book_id = ?",
            (book_id,)
        )

        self.conn.commit()
        print("книга возвращена")

    def search_books(self, keyword):
        self.cursor.execute(
            "select * from books where title like ? or author like ?",
            (f"%{keyword}%", f"%{keyword}%")
        )
        results = self.cursor.fetchall()

        for row in results:
            print(row)

    def get_borrowed_books(self):
        self.cursor.execute("""
        select readers.name, books.title, borrowed_books.borrow_date
        from borrowed_books
        join readers on borrowed_books.reader_id = readers.id
        join books on borrowed_books.book_id = books.id
        """)
        results = self.cursor.fetchall()

        for row in results:
            print(row)

    def get_statistics(self):
        self.cursor.execute(
            "select count(*) from books where status = 'available'"
        )
        available = self.cursor.fetchone()[0]

        self.cursor.execute(
            "select count(*) from books where status = 'borrowed'"
        )
        borrowed = self.cursor.fetchone()[0]

        print(f"доступно книг: {available}")
        print(f"выдано книг: {borrowed}")

    def close(self):
        self.conn.close()



if __name__ == "__main__":
    library = Library()
    library.add_book("1984", "George Orwell", 1949)
    library.add_book("The Hobbit", "J.R.R. Tolkien", 1937)

    library.add_reader("Alice", 25)
    library.add_reader("Bob", 30)

    library.borrow_book(1, 1)

    library.get_borrowed_books()

    library.search_books("1984")

    library.get_statistics()

    library.return_book(1)

    library.get_statistics()

    library.close()