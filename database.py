from sqlalchemy import create_engine, text
from dotenv import dotenv_values
import os

#securing the key storing it into .env
key = dotenv_values(".env")

def load_jobs_from_db():
    engine = create_engine(key["DB_KEY"])

    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())

    return jobs