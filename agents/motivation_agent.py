import random

class MotivationAgent:
    def __init__(self):
        self.quotes = [
            "Believe in yourself. You are capable of amazing things!",
            "Don’t watch the clock; do what it does. Keep going.",
            "The secret of getting ahead is getting started.",
            "Push yourself, because no one else is going to do it for you.",
            "Success is not for the lazy."
        ]

    async def run_async(self, _input=None):
        quote = random.choice(self.quotes)
        yield {"message": f"💡 Motivation: {quote}"}
