import sys
import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from alembic.config import Config
from alembic import command

# Add the backend directory to the Python path
backend_dir = Path(__file__).parent.parent
sys.path.append(str(backend_dir))

from src.core.config import settings

def init_database():
    """Initialize the database and run migrations"""
    # Create database if it doesn't exist
    if not database_exists(settings.SQLALCHEMY_DATABASE_URI):
        print(f"Creating database: {settings.SQLALCHEMY_DATABASE_URI}")
        create_database(settings.SQLALCHEMY_DATABASE_URI)
    
    # Run migrations
    print("Running database migrations...")
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")
    
    print("Database initialization complete!")

if __name__ == "__main__":
    init_database()
