class BookCatalog:
    def __init__(self, books: dict):
        self._books_catalog = self.__init_books_graph(books)
        self._authors = {}
        self._books = self.__all_book_names(books)
        self._gener = {}

    def __all_authors(self, books: dict) -> set:
        return set(books.keys())

    def __all_book_names(self, books: dict) -> set:
        books_names = set()
        for authors in books:
            books_names |= set(books[authors].keys())
        return books_names

    def __init_books_graph(self, inp_books) -> dict:

        output_graph = {}

        for author in inp_books.keys():

            output_graph[author] = set()

            for book in set(inp_books[author].keys()):

                output_graph[book] = set()
                output_graph[book].add(author)

                output_graph[author].add(book)

                for gener in inp_books[author][book]:

                    output_graph[book].add(gener)

                    if gener not in output_graph:
                        output_graph[gener] = set()

                    output_graph[gener].add(author)
                    output_graph[gener].add(book)

        return output_graph

    def all_catalog(self):
        return self._books_catalog

    def remove_book_from_catalog(self, book_name_for_remove: str) -> None:

        if book_name_for_remove in self._books_catalog:
            self.__remove_book(book_name_for_remove)

    def __remove_book(self, book_name_for_remove: str) -> None:

        for edges in self._books_catalog[book_name_for_remove]:
            self._books_catalog[edges].remove(book_name_for_remove)

        del self._books_catalog[book_name_for_remove]


books_for_catalog = {"author1": {"book1": ["g1", "g2"], "book2": ["g3", "g1"]}, "author2": {"book3": ["g1", "g2"]}}

cc = BookCatalog(books_for_catalog)
print(cc.all_catalog())
