from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

import crud
import database
import models
from schemas import Team, Score
app = FastAPI()


# Dependency to get a SQLAlchemy session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# API endpoints for teams
@app.post("/teams/", response_model=Team)  # Use Team from schemas.py
def create_team(team: Team, db: Session = Depends(get_db)):
    return crud.create_team(db, team)

@app.get("/teams/{team_id}", response_model=Team)  # Use Team from schemas.py
def read_team(team_id: int, db: Session = Depends(get_db)):
    team = crud.read_team(db, team_id)
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return team


@app.get("/teams/", response_model=list[Team])  # Use Team from schemas.py
def read_teams(db: Session = Depends(get_db)):
    return crud.read_teams(db)


@app.put("/teams/{team_id}", response_model=Team)  # Use Team from schemas.py
def update_team(team_id: int, team: Team, db: Session = Depends(get_db)):
    existing_team = crud.read_team(db, team_id)
    if existing_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return crud.update_team(db, team_id, team)


@app.delete("/teams/{team_id}", response_model=Team)  # Use Team from schemas.py
def delete_team(team_id: int, db: Session = Depends(get_db)):
    team = crud.delete_team(db, team_id)
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return team


# API endpoints for scores
@app.post("/scores/", response_model=Score)  # Use Score from schemas.py
def create_score(score: Score, db: Session = Depends(get_db)):
    return crud.create_score(db, score)


@app.get("/scores/{score_id}", response_model=Score)  # Use Score from schemas.py
def read_score(score_id: int, db: Session = Depends(get_db)):
    score = crud.read_score(db, score_id)
    if score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return score


@app.get("/scores/", response_model=list[Score])  # Use Score from schemas.py
def read_scores(db: Session = Depends(get_db)):
    return crud.read_scores(db)


@app.put("/scores/{score_id}", response_model=Score)  # Use Score from schemas.py
def update_score(score_id: int, score: Score, db: Session = Depends(get_db)):
    existing_score = crud.read_score(db, score_id)
    if existing_score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return crud.update_score(db, score_id, score)


@app.delete("/scores/{score_id}", response_model=Score)  # Use Score from schemas.py
def delete_score(score_id: int, db: Session = Depends(get_db)):
    score = crud.delete_score(db, score_id)
    if score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return score


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)