from pydantic import BaseModel


class Team(BaseModel):
    id: int
    name: str


class Score(BaseModel):
    id: int
    match_id: int
    team_id: int
    score: int

