from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from models import Team, Score

# Define your database URL (change it if your database is in a different location)
DATABASE_URL = "sqlite:///./sqlitedb/voetbal.db"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

# Initialize the database tables
Base.metadata.create_all(bind=engine)

# Insert sample data
sample_team_1 = Team(name="Team 1")
sample_team_2 = Team(name="Team 2")

sample_score_1 = Score(match_id=1, team_id=1, score=2)
sample_score_2 = Score(match_id=1, team_id=2, score=1)

# Add data to the session and commit
db.add(sample_team_1)
db.add(sample_team_2)
db.add(sample_score_1)
db.add(sample_score_2)

db.commit()

# Close the session
db.close()
