import mysql.connector

def save_to_database(filename,
                     score,
                     name_candidates,
                     top_skills,
                     education_hints,
                     experience_years):

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="resume_screening_db"
    )

    cursor = conn.cursor()

    query = """
    INSERT INTO candidate_rankings
    (
        filename,
        score,
        name_candidates,
        top_skills,
        education_hints,
        estimated_experience_years
    )
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    values = (
        filename,
        score,
        name_candidates,
        top_skills,
        education_hints,
        experience_years
    )

    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()
