import pandas as pd
import os

class DataService:
    def load_data(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # In a real app, you might load from a database or multiple sources
        books_df = pd.read_csv(os.path.join(script_dir,'../datasets/books.csv'), sep=',')
        movies_df = pd.read_csv(os.path.join(script_dir,'../datasets/movies.csv'), sep=',')
        games_df = pd.read_csv(os.path.join(script_dir,'../datasets/games.csv'), sep=',')

        # Combine all items into a single dataframe
        all_items = pd.concat([books_df, movies_df, games_df], ignore_index=True)
        return all_items