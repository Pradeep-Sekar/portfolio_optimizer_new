import asyncio
from app.config.database import init_db

async def main():
    await init_db()
    print("✅ Database tables created successfully!")

if __name__ == "__main__":
    asyncio.run(main())