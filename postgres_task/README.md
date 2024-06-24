Initialize Alembic for managing database migrations:
flask db init

After making changes to your models, generate a migration script:
flask db migrate -m "Initial migration"

Apply the migrations to your database:
flask db upgrade
