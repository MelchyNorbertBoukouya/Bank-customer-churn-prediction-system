 # %%writefile database.py

from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

DATABASE_URL = "mysql+pymysql://root:@localhost/bank_churn_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


class Prediction(Base):

    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)

    credit_score = Column(Integer)
    geography = Column(String(50))
    gender = Column(String(20))
    age = Column(Integer)
    tenure = Column(Integer)

    balance = Column(Float)
    num_products = Column(Integer)

    has_credit_card = Column(Integer)
    is_active_member = Column(Integer)

    estimated_salary = Column(Float)

    prediction = Column(Integer)
    churn_probability = Column(Float)
    churn_percentage = Column(Float)

    risk_level = Column(String(20))

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


Base.metadata.create_all(bind=engine)