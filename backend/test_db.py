from app.database import engine

try:
    engine.connect()
    print("Database connection successful!")
except Exception as e:
    print(f"Database connection failed: {e}")
