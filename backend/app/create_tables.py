import asyncio
from app.config.database import engine, Base
import logging

logging.basicConfig(level=logging.INFO)

async def create_tables():
    async with engine.begin() as conn:
        logging.info("🔍 Running create_all()...")
        await conn.run_sync(Base.metadata.create_all)
        logging.info("✅ Tables created successfully!")

if __name__ == "__main__":
    asyncio.run(create_tables())