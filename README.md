# user Register end point

curl --location 'http://127.0.0.1:5000/register' \
--header 'Content-Type: application/json' \
--data-raw '{"username":"padma sree","password":"Padam@123"}'
# Login endpoint

curl --location 'http://127.0.0.1:5000/login' \
--header 'Content-Type: application/json' \
--data-raw '{"username":"padma sree","password":"Padam@123"}'

# protected endpoint

curl --location 'http://127.0.0.1:5000/protected' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyMjc3NDI3NSwianRpIjoiMzAxYjFjYTQtY2E5MC00MzgyLWEwMjUtNDZlYmViMDJiYjUzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InBhZG1hIHNyZWUiLCJuYmYiOjE3MjI3NzQyNzUsImNzcmYiOiIzMWM2MTIyZS0zNjU3LTQ3ZjUtOGQ1Yy0wOWZmNjdkYmE0YTMiLCJleHAiOjE3MjI3NzUxNzV9.Q9etnqt4IP1Do15QSCWFmOXJKmNJn6HfHeEUBMhdyEY'