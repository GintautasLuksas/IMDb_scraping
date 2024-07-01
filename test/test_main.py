import unittest
import subprocess
import os
import pandas as pd

class TestMainScript(unittest.TestCase):

    def test_reload_data(self):
        # Run IMDb_collector.py to generate imdb_movies.csv
        subprocess.run(["python", "IMDb_collector.py"])

        # Import main.py and reload the data
        import src.main
        src.main.reload_data()

        # Assert that df is a pandas DataFrame and is not empty
        self.assertIsInstance(src.main.df, pd.DataFrame)
        self.assertFalse(src.main.df.empty)

    def test_top_10_movies_by_rating(self):
        import src.main
        src.main.reload_data()
        src.main.show_top_10_movies_by_rating()

        # Assert that the top 10 movies by rating are displayed correctly
        # Example assertion: Check if the first movie in the list has a valid title and rating
        top_10_movies = src.main.df.nlargest(10, 'Rating')
        self.assertEqual(len(top_10_movies), 10)  # Check if there are exactly 10 movies
        self.assertTrue(all(top_10_movies['Title']))  # Check if all titles are non-empty strings
        self.assertTrue(all(top_10_movies['Rating'] >= 0))  # Check if all ratings are non-negative

    def test_top_10_movies_by_rating_amount(self):
        import src.main
        src.main.reload_data()
        src.main.show_top_10_movies_by_rating_amount()

        # Assert that the top 10 movies by rating amount are displayed correctly
        # Example assertion: Check if the top movie has a valid title and rating amount
        top_10_movies = src.main.df.sort_values('Rating Amount', ascending=False).head(10)
        self.assertEqual(len(top_10_movies), 10)  # Check if there are exactly 10 movies
        self.assertTrue(all(top_10_movies['Title']))  # Check if all titles are non-empty strings
        self.assertTrue(all(top_10_movies['Rating Amount'] >= 0))  # Check if all rating amounts are non-negative

    def test_top_10_movies_by_length(self):
        import src.main
        src.main.reload_data()
        src.main.show_top_10_movies_by_length()

        # Assert that the top 10 movies by length are displayed correctly
        # Example assertion: Check if the first movie in the list has a valid title and duration
        top_10_movies = src.main.df.nlargest(10, 'Duration (minutes)')
        self.assertEqual(len(top_10_movies), 10)  # Check if there are exactly 10 movies
        self.assertTrue(all(top_10_movies['Title']))  # Check if all titles are non-empty strings
        self.assertTrue(all(top_10_movies['Duration (minutes)'] >= 0))  # Check if all durations are non-negative

    # Add more test cases for other functions in main.py as needed

if __name__ == '__main__':
    unittest.main()

