from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    # Definieer een relatie om scores op te halen die aan dit team zijn gekoppeld
    scores = relationship("Score", back_populates="team")


class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True, index=True)
    match_id = Column(Integer, index=True)
    team_id = Column(Integer, ForeignKey("teams.id"))
    score = Column(Integer)

    # Definieer een relatie om het bijbehorende team op te halen
    team = relationship("Team", back_populates="scores")

