import unittest


class BookCatalog:
    def __init__(self):
        self.books = {"book1": ["author1", ["genre1_1", "genre1_2"]],
                      "book2": ["author2", ["genre2_1", "genre2_2"]], "book3": ["author1", "name1", None]}

        self.authors_in_storage = self.make_base("authors")
        self.genres_in_storage = self.make_base("genres")

    def make_base(self, key="authors/genres") -> set:
        output_set = set()
        match key:
            case "genres":
                for books_key in self.books:
                    if self.books[books_key][1] is not None:
                        for genres in self.books[books_key][1]:
                            output_set.add(genres)
            case "authors":
                for books_key in self.books:
                    output_set.add(self.books[books_key][0])
            case _:
                return set()
        return output_set

    def add_book(self, book_name: str, author_name: str = "No name", genres: list = None) -> None:
        if not (book_name in self.books):
            self.authors_in_storage.add(author_name)
            self.books[book_name] = [author_name, genres]
        else:
            print("Book in storage")

    def del_book(self, book_name: str) -> None:
        del self.books[book_name]

    def search_book(self, book_name: str = None, author_name: str = None, genres: list = None):
        if book_name is not None:
            if book_name in self.books:
                if self.books[book_name][1] is not None:
                    print(f"{book_name}, {self.books[book_name][0]}: {self.books[book_name][1]}")
                else:
                    print(f"{book_name}, {self.books[book_name][0]}: — ")
        elif author_name is not None:
            if author_name in self.authors_in_storage:
                output_book_list = [[] for books_key in self.books]
            else:
                print("No author name in storage")
        elif genres is not None:
            if genres in self.genres_in_storage:
                output_book_list = []
        else:
            ellipsis
