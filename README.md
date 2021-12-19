## Setup instructions
1. Initialize project's python virtual environment.
2. Install dependencies using either the Pipfile or requirements.txt.
3. Apply migrations; from inside the active venv, run python manage.py migrate. This project uses SQLite, so this will create a .db file.
4. Create a user; python manage.py createsuperuser

## API endpoints
  /movies/ - List movies (GET) or create new movie entry (POST; must be logged in)

  /movies/{movie-id} - See details of movie whose database primary key is {movie-id}, or edit movie details (must be logged in)
  
  /movies/{movie-id}/like - Increase a movie's "like" count by one
  
  /movies/{movie-id}/dislike - Decrease a movie's "like" count by one
  

## Tests
Test suite may be run with the command python manage.py test

## Online deployment
This API is deployed at https://ensemble-application.herokuapp.com/movies/ with the default user "admin", password "admin".
