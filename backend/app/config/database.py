from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Create an async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create a session factory
async_session_maker = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

# Base for models
Base = declarative_base()

# Dependency to get DB session
async def get_db():
    async with async_session_maker() as session:
        yield session