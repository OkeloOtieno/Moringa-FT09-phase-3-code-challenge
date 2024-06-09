import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly")
        self.assertEqual(magazine.name, "Tech Weekly")
        
    def test_list_all_magazines(self):
        all_magazine = Magazine.list_all_magazines()
        self.assertGreaterEqual(len(all_magazine),1)

    def test_list_all_authors(self):
        all_author = Author.list_all_authors()
        self.assertGreaterEqual(len(all_author),1)

    def test_list_all_articles(self):
        all_article = Article.list_all_articles()
        self.assertGreaterEqual(len(all_article),1)

    def test_magazine_contributing_authors(self):
        magazine = Magazine(1, "Vogue", "Fashion")
        authors = magazine.contributing_authors
        self.assertIsInstance(authors, list)
        self.assertTrue(all(isinstance(author, Author) for author in authors))

if __name__ == "__main__":
    unittest.main()
