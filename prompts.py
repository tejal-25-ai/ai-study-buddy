def explanation_prompt(topic):
    return f"""
Explain the following topic in simple terms for a student.

Topic: {topic}

Provide:
1. Simple explanation
2. Example
3. Short summary
"""


def summary_prompt(text):
    return f"""
Summarize the following notes into key bullet points.

{text}
"""


def quiz_prompt(topic):
    return f"""
Create 5 quiz questions with answers about the topic below.

Topic: {topic}

Format:
Question:
Answer:
"""


def flashcard_prompt(topic):
    return f"""
Create 5 study flashcards for the topic below.

Topic: {topic}

Format:
Front:
Back:
"""