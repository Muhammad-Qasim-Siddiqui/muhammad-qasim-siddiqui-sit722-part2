import os

class Settings:
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", 
        "postgresql://book_catalog_db_sit722_part_2_db_user:j0i1YQYQGPqf7tygbu7jl7Dc23Gk2N75@dpg-crlfifjtq21c73eeh8pg-a.oregon-postgres.render.com/book_catalog_db_sit722_part_2_db"
    )

    def __init__(self):
        if not self.DATABASE_URL:
            raise ValueError("DATABASE_URL environment variable is not set")

settings = Settings()
