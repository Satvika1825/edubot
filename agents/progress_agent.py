class ProgressAgent:
    async def run_async(self, _input=None):
        subject = getattr(_input, "subject", "Unknown Subject")
        yield {"message": f"📈 Progress: You are making great progress in {subject}! Keep it up!"}
