from core.api.game_api import *

class GameList:
    def __init__(self):
        self.gameAPI = GameAPI()
        self.games = []

    def add_game(self, name):
        self.games.append(self.gameAPI.get_game_by_name(name))

    def get_games(self):
        return self.games

    def get_game_by_name(self, name):
        for game in self.games:
            if game["name"] == name:
                return game
        return None

    def get_games_by_genre(self, genre):
        games_by_genre = []
        for game in self.games:
            if genre in game["genres"]:
                games_by_genre.append(game)
        return games_by_genre

    def remove_game(self, name):
        for i in range(len(self.games)):
            if self.games[i]["name"] == name:
                del self.games[i]
                return
        print("Game not found.")

    def update_game(self, name, new_name=None, new_genres=None):
        for i in range(len(self.games)):
            if self.games[i]["name"] == name:
                if new_name:
                    self.games[i]["name"] = new_name
                if new_genres:
                    self.games[i]["genres"] = new_genres
                return
        print("Game not found.")


movie_genres = ["Action", "Adventure", "Animation", "Comedy", "Crime", "Documentary", "Drama", "Family", "Fantasy",
                "Historical", "Horror", "Musical", "Mystery", "Romance", "Science Fiction", "Thriller", "War",
                "Western"]

