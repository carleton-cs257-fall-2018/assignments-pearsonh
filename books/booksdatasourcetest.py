'''
Paul Butterfield and Henry Pearson
09/20/18
Books2
'''

import unittest
import booksdatasource

class BooksDataSourceTest (unittest.TestCase):
    def setUp (self):
        self.books_data_source = booksdatasource.BooksDataSource("books.csv", 
            "authors.csv", "books_authors.csv")
    def tearDown(self):
        pass
        
    def test_book(self):
      self.assertEqual(self.books_data_source.book(13), 
         {'id': 13, 'title': 'Moby Dick', 'publication_year': 1851})
         
    def test_books_author_id(self):
        self.assertEqual(self.books_data_source.books(author_id=5),
            [{'id': 6, 'title': 'Good Omens', 'publication_year': 1990},
            {'id': 15, 'title': 'Neverwhere', 'publication_year': 1996}])
    
    def test_books_start_year(self):
        self.assertEqual(self.books_data_source.books(author_id=5, start_year=1996),
            [{'id': 15, 'title': 'Neverwhere', 'publication_year': 1996}])
            
    def test_books_search_text(self):
        self.assertEqual(self.books_data_source.books(search_text='Mirror'),
            [self.books_data_source.book(12)])
            
    def test_books_search_text_empty(self):
        self.assertEqual(self.books_data_source.books(search_text='Das Kapital'), [])
        
    def test_books_end_year(self):
        self.assertEqual(self.books_data_source.books(end_year=1815),
            [self.books_data_source.book(5), self.books_data_source.book(18),
            self.books_data_source.book(20)])
            
    def test_books_sort_by(self):
        self.assertEqual(self.books_data_source.books(end_year=1815, sort_by = 'year'),
            [self.books_data_source.book(18), self.books_data_source.book(20),
            self.books_data_source.book(5)])
            
    def test_books_allBooks(self):
        self.assertEqual(self.books_data_source.books(),
            [self.books_data_source.book(x) for x in range(48)])
            
            
            
    def test_author(self):
      self.assertEqual(self.books_data_source.author(10), 
         {'id': 10, 'last_name': 'Lewis', 'first_name': 'Sinclair',
         'birth_year': 1885, 'death_year': 1951})
         
    def test_authors_book_id(self):
        self.assertEqual(self.books_data_source.authors(book_id=5),
            [self.books_data_source.author(4)])
    
    def test_authors_start_year(self):
        self.assertEqual(self.books_data_source.authors(start_year=2014),
            [self.books_data_source.author(9), self.books_data_source.author(6)])
            
    def test_authors_sort_by(self):
        self.assertEqual(self.books_data_source.authors(start_year=2014, sort_by = 'birth_year'),
            [self.books_data_source.author(9), self.books_data_source.author(6)])
            
    def test_authors_search_text(self):
        self.assertEqual(self.books_data_source.authors(search_text='Dickens'),
            [self.books_data_source.author(23)])
            
    def test_authors_search_text_empty(self):
        self.assertEqual(self.books_data_source.authors(search_text='Karl Marx'), [])
        
    def test_authors_end_year(self):
        self.assertEqual(self.books_data_source.authors(end_year=1812),
            [self.books_data_source.book(4), self.books_data_source.book(23)])
            
            
    def test_authors_allAuthors(self):
        self.assertEqual(self.books_data_source.authors(),
            [self.books_data_source.author(x) for x in range(25)])
            
         
         
         
         
unittest.main()