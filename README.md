To run this app:
-
- install dependencies `pipenv install` or `pip install -r requirements.txt`
- launch database `docker-compose up -d`
- run migration `alembic upgrade head`
- launch server `uvicorn api.main:app` 