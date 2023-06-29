from sqlalchemy import create_engine, text
from dotenv import dotenv_values
import os

#securing the key storing it into .env
key = dotenv_values(".env")
engine = create_engine(key["DB_KEY"])

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())

    return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
            result = conn.execute(text(f"select * from jobs where id = {id}"))
    
    row = result.all()
    if len(row) == 0:
        return None
    else:
        return row[0]._asdict()


if __name__ == "__main__":
    print(load_job_from_db(2))