import os
import dotenv

from src.repository.bingoRepository import InMemoryBingoRepository

dotenv.load_dotenv()

if os.getenv("DATABSE_URL"):
    # sets_database
    pass
else:
    bingo_repository = InMemoryBingoRepository()
