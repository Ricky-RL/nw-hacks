# MOVIFY GAMES
A Python application gives users perfect movie recommendations based on their favourite games.

Made by: Karanveer Buttar, Jeanette Guo, Ricky Lin, William Sun for nwHacks 2023

## Functions
- 80,000 games from 75 genres are are sorted into 18 respective movie genres
    - Movie genres include: Action, Adventure, Animation, Comedy, Crime, Documentary, Drama, Family, Fantasy, History, Horror, Music, Mystery, Romance, Science Fiction, Thriller, TV Movie, War, and Western.
- A list of top-rated and relevant movies are outputted based on the genres of the inputted game

## Prerequisites
- Python
    - Libraries: pillow, tkinter, requests
- "secrets.ini" file in the following format with your own API keys from IMdb, TMdb and Giant Bomb 
```
[secrets]
game_api = YOUR_GIANTBOMB_API_KEY
movie_api = YOUR_TMDB_API_KEY
```

