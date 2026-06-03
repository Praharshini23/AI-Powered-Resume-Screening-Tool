def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text


def preprocess(text):
    text = text.lower()
    text = re.sub(r"\d+", "", text)  # remove digits
    text = text.translate(str.maketrans("", "", string.punctuation))  # remove punctuation
    return text

def calculate_score(resume_text, job_description):
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([resume_text, job_description])
    score = cosine_similarity(vectors[0], vectors[1])[0][0]
    return score * 100  # percentage


def generate_suggestions(resume_text, job_description, raw_resume_text):
    suggestions = []

    resume_lines = raw_resume_text.split("\n")

    
    stop_words = set(stopwords.words("english"))
    resume_words = set([w for w in resume_text.split() if w not in stop_words])
    job_words = set([w for w in job_description.split() if w not in stop_words])

    missing_keywords = job_words - resume_words

    if missing_keywords:
        keyword_suggestions = []
        for kw in list(missing_keywords)[:5]:  # limit to 5 keywords
            found_lines = [i + 1 for i, line in enumerate(resume_lines) if kw in line.lower()]
            if not found_lines:
                keyword_suggestions.append(f"Keyword '{kw}' is missing. Consider adding it.")
        if keyword_suggestions:
            suggestions.extend(keyword_suggestions)

    word_count = len(resume_text.split())
    if word_count < 200:
        suggestions.append("Your resume seems short. Add more details about your skills and experience.")
    elif word_count > 2000:
        suggestions.append("Your resume seems too long. Try making it more concise.")

    if not suggestions:
        suggestions.append("Your resume looks strong. Good match!")

    return suggestions
