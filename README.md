# Game Leaderboard API

REST API for a game leaderboard. It stores games, players and the scores that players get in games.

## Technologies

- Python 3.12, Django, Django REST Framework, gunicorn
- PostgreSQL 16 (Django ORM)
- Docker and Docker Compose

## Running the project

The `.env` file is created by copying `.env.example` (the example values work as they are):

```
copy .env.example .env      (Windows)
cp .env.example .env        (Linux / macOS)
```

Then everything is started with:

```
docker compose up --build
```

The API is available at http://localhost:8000/api/ (for example http://localhost:8000/api/games/). The tables are created automatically when the backend starts (`python manage.py migrate` in the Dockerfile `CMD`).

`docker compose down` stops the containers and keeps the data. `docker compose down -v` deletes the data too.

There are two services: `backend` (the API, port 8000) and `db` (PostgreSQL, not published to the host). They are in one network, and the data is stored in the named volume `pgdata`.

## Data models

- **Game** - title, genre
- **Player** - username
- **Score** - player, game, points

Relationships: one player has many scores, and one game has many scores (two one-to-many relationships). A score belongs to one player and one game.

## API

There are 20 endpoints: GET, POST, PUT, PATCH and DELETE for games, players and scores, plus two endpoints for related data:

- `GET /api/games/{id}/scores/` - scores of a game
- `GET /api/players/{id}/scores/` - scores of a player

All endpoints (method, URL, body, responses and errors) are documented in [docs/API.md](docs/API.md).

## Postman

The collection is `postman/Game_Leaderboard_API.postman_collection.json`. It has a request for every endpoint and a few invalid requests. The requests are run from top to bottom: the create requests save the new ids in the variables `gameId`, `playerId` and `scoreId`, and the other requests use them. The delete requests at the end remove the test data. The variable `baseUrl` is `http://localhost:8000`.

## Project structure

```
compose.yaml            services, network and volume
.env.example            environment variables
backend/
    Dockerfile
    requirements.txt
    manage.py
    config/             Django settings and main urls
    leaderboard/        models, serializers, views, urls
docs/API.md             API documentation
postman/                Postman collection
```
