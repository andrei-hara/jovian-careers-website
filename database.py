from sqlalchemy import create_engine, text
from dotenv import dotenv_values


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


def add_application_to_db(job_id, data):
     with engine.connect() as conn:
            print(data['email'])
            # query = text(f"INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES ({job_id}, '{data['full_name']}', '{data['email']}', '{data['linkedin']}', '{data['education']}', '{data['work_experience']}', '{data['work_experience']}')")
            query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience) VALUES (:job_id, :full_name, :email, :linkedin, :education, :work_experience)")
            # conn.execute(query, job_id=job_id, full_name=data['full_name'],
            #              email=data['email'], linkedin=data['linkedin'],
            #              education=data['education'], work_experience = data['work_experience'])
            bind_params = {
            'job_id': job_id,
            'full_name': data['full_name'],
            'email': data['email'],
            'linkedin': data['linkedin'],
            'education': data['education'],
            'work_experience': data['work_experience']
            }
            query = query.bindparams(**bind_params)
            conn.execute(query)
            conn.commit()


if __name__ == "__main__":
    print(load_job_from_db(2))