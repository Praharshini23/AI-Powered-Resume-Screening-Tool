CREATE DATABASE resume_screening_db;

USE resume_screening_db;

CREATE TABLE candidate_rankings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    filename VARCHAR(255),
    score DECIMAL(10,4),
    name_candidates VARCHAR(255),
    top_skills TEXT,
    education_hints VARCHAR(255),
    estimated_experience_years DECIMAL(5,1),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
