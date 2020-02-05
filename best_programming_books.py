from pathlib import Path
from urllib.request import urlretrieve

from bs4 import BeautifulSoup

url = ("https://bites-data.s3.us-east-2.amazonaws.com/"
       "best-programming-books.html")
tmp = Path("/tmp")
html_file = tmp / "books.html"

if not html_file.exists():
    urlretrieve(url, html_file)


class Book:
    """Book class should instatiate the following variables:

    title - as it appears on the page
    author - should be entered as lastname, firstname
    year - four digit integer year that the book was published
    rank - integer rank to be updated once the books have been sorted
    rating - float as indicated on the page
    """
    def __init__(self, title, author, year, rank, rating):
        self.title = title
        self.author = author
        self.year = year
        self.rank = int(rank)
        self.rating = float(rating)
        
    def __repr__(self):
        return (f'[{self.rank:03}] {self.title} ({self.year})\n'
                f'      {self.author} {self.rating}')
    pass


def _get_soup(file):
    return BeautifulSoup(file.read_text(), "html.parser")


def display_books(books, limit=10, year=None):
    """Prints the specified books to the console

    :param books: list of all the books
    :param limit: integer that indicates how many books to return
    :param year: integer indicating the oldest year to include
    :return: None
    """
    if limit >= len(books):
        limit = len(books)
    
    if year == None:
        print(books[:limit])
    else:
        books = filter(lambda x: int(x.year) >= year, books)
        for _ in range(limit):
            print(next(books))
    
    return None
    pass


def load_data():
    """Loads the data from the html file

    Creates the soup object and processes it to extract the information
    required to create the Book class objects and returns a sorted list
    of Book objects.

    Books should be sorted by rating, year, title, and then by author's
    last name. After the books have been sorted, the rank of each book
    should be updated to indicate this new sorting order.The Book object
    with the highest rating should be first and go down from there.
    """
    soup = _get_soup(html_file)
    
    book_blocks = soup.find_all('div', class_='book accepted normal')
    
    book_list = []
    rank_setting = 1
    for book in book_blocks:
        if 'python' not in book.find('h2', class_='main').text.lower():
            continue
        
        try:
            title = book.find('h2', class_='main').text
            author_name = book.find('h3', class_='authors').find('a').text.split()
            first_name, last_name = " ".join(author_name[:-1]), author_name[-1]
            author = last_name + ", " + first_name
            year = book.find('span', class_='date').text[3:]
            rank = rank_setting
            rank_setting += 1
            rating = float(book.find('span', class_='rating').text)
            book_list.append(Book(title, author, year, rank, rating))
        except:
            continue
    
    sort_spec = ((lambda x: x.rating, True), (lambda x: x.year, False), (lambda x:x.title.lower(), False), (lambda x: x.author, False))
    
    for sort_func, reverse_value in sort_spec[::-1]:
        book_list.sort(key = sort_func, reverse=reverse_value)

    updated_rank = 1
    for book in book_list:
        book.rank = updated_rank
        updated_rank += 1
    
    return book_list
    pass


def main():
    books = load_data()
    display_books(books, limit=5, year=2017)
    """If done correctly, the previous function call should display the
    output below.
    """


if __name__ == "__main__":
    main()

"""
[001] Python Tricks (2017)
      Bader, Dan 4.74
[002] Mastering Deep Learning Fundamentals with Python (2019)
      Wilson, Richard 4.7
[006] Python Programming (2019)
      Fedden, Antony Mc 4.68
[007] Python Programming (2019)
      Mining, Joseph 4.68
[009] A Smarter Way to Learn Python (2017)
      Myers, Mark 4.66
"""