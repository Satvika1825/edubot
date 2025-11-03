import random

class QuizAgent:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Rome"],
                "answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Earth", "Mars", "Jupiter", "Venus"],
                "answer": "Mars"
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
                "answer": "William Shakespeare"
            },
            {
                "question": "What is 7 x 8?",
                "options": ["54", "56", "58", "60"],
                "answer": "56"
            },
            {
                "question": "What is the boiling point of water at sea level?",
                "options": ["90°C", "100°C", "110°C", "120°C"],
                "answer": "100°C"
            }
        ]

    async def run_async(self, _input=None):
        q = random.choice(self.questions)
        options = q["options"]
        random.shuffle(options)
        options_letters = [f"{chr(65+i)}) {opt}" for i, opt in enumerate(options)]
        answer_letter = chr(65 + options.index(q["answer"]))
        message = (
            f"<b>Quiz:</b> {q['question']}<br><br>"
            + "<br>".join(options_letters)
            + f"<br><br><i>(Answer: {answer_letter})</i>"
        )
        yield {"formatted_message": message}
