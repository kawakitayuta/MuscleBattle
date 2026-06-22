from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===== DB設定 =====
engine = create_engine("sqlite:///musclebattle.db")
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

# ===== テーブル定義 =====
class User(Base):
    __tablename__ = "users"
    id     = Column(Integer, primary_key=True)
    name   = Column(String)
    streak = Column(Integer, default=0)

class Workout(Base):
    __tablename__ = "workouts"
    id       = Column(Integer, primary_key=True)
    user_id  = Column(Integer)
    exercise = Column(String)
    reps     = Column(Integer)

# テーブル作成
Base.metadata.create_all(engine)

# ===== API =====

# ユーザー登録
@app.post("/user")
def create_user(name: str):
    db = SessionLocal()
    user = User(name=name, streak=0)
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return {"id": user.id, "name": user.name, "message": "登録しました！"}

# ワークアウト記録
@app.post("/workout")
def post_workout(user_id: int, exercise: str, reps: int):
    db = SessionLocal()
    workout = Workout(user_id=user_id, exercise=exercise, reps=reps)
    db.add(workout)
    db.commit()
    db.close()
    return {"message": f"{exercise} {reps}回を記録しました！"}

# ランキング取得
@app.get("/ranking")
def get_ranking():
    db = SessionLocal()
    results = db.query(
        Workout.user_id,
        User.name,
        func.sum(Workout.reps).label("total")
    ).join(User, User.id == Workout.user_id)\
     .group_by(Workout.user_id)\
     .order_by(func.sum(Workout.reps).desc())\
     .all()
    db.close()
    return [
        {"rank": i+1, "name": r.name, "total_reps": r.total}
        for i, r in enumerate(results)
    ]

# ユーザーの記録一覧
@app.get("/user/{user_id}/workouts")
def get_workouts(user_id: int):
    db = SessionLocal()
    workouts = db.query(Workout).filter(Workout.user_id == user_id).all()
    db.close()
    return [{"exercise": w.exercise, "reps": w.reps} for w in workouts]