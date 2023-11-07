from sqlalchemy.orm import Session
import models


def create_team(db: Session, team: models.Team):
    db_team = models.Team(**team.dict())
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team


def read_team(db: Session, team_id: int):
    return db.query(models.Team).filter(models.Team.id == team_id).first()


def read_teams(db: Session):
    return db.query(models.Team).all()


def update_team(db: Session, team_id: int, team: models.Team):
    db_team = db.query(models.Team).filter(models.Team.id == team_id).first()
    for key, value in team.dict().items():
        setattr(db_team, key, value)
    db.commit()
    db.refresh(db_team)
    return db_team


def delete_team(db: Session, team_id: int):
    db_team = db.query(models.Team).filter(models.Team.id == team_id).first()
    if db_team:
        db.delete(db_team)
        db.commit()
    return db_team

def create_score(db: Session, score: models.Score):
    db_score = models.Score(**score.dict())
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score

def read_score(db: Session, score_id: int):
    return db.query(models.Score).filter(models.Score.id == score_id).first()

def read_scores(db: Session):
    return db.query(models.Score).all()

def update_score(db: Session, score_id: int, score: models.Score):
    db_score = db.query(models.Score).filter(models.Score.id == score_id).first()
    for key, value in score.dict().items():
        setattr(db_score, key, value)
    db.commit()
    db.refresh(db_score)
    return db_score

def delete_score(db: Session, score_id: int):
    db_score = db.query(models.Score).filter(models.Score.id == score_id).first()
    if db_score:
        db.delete(db_score)
        db.commit()
    return db_score

