import mysql.connector

cursor = conn.cursor()

for _, row in df.iterrows():

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
        row["filename"],
        float(row["score"]),
        row["name_candidates"],
        row["top_skills"],
        row["education_hints"],
        float(row["estimated_experience_years"])
    )

    cursor.execute(query, values)

conn.commit()

cursor.close()
conn.close()

print("Data exported successfully.")
