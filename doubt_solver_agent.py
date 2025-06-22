import re
import difflib

class DoubtSolverAgent:
    async def run_async(self, _input=None):
        doubt = getattr(_input, "doubt", "")
        
        # Normalize function
        norm = lambda s: re.sub(r'[^\w\s]', '', s).strip().lower()
        processed_doubt = norm(doubt)

        # Define sample doubts (normalized)
        example_doubts = {
            norm("what is photosynthesis?"): "Photosynthesis is the process by which green plants use sunlight to make their own food from carbon dioxide and water. It produces oxygen as a byproduct.",
            norm("what is algebra?"): "Algebra is a branch of mathematics dealing with symbols and the rules for manipulating those symbols to solve equations.",
            norm("who wrote romeo and juliet?"): "Romeo and Juliet was written by William Shakespeare.",
            norm("what is gravity?"): "Gravity is a force that attracts two bodies toward each other. On Earth, it gives weight to physical objects."
        }

        if processed_doubt:
            # Find closest match (not exact match)
            closest_match = difflib.get_close_matches(processed_doubt, example_doubts.keys(), n=1, cutoff=0.6)
            if closest_match:
                answer = example_doubts[closest_match[0]]
                yield {"message": f"🤔 Doubt: '{doubt}'\n\n💡 Solution: {answer}"}
            else:
                available = "\n".join([f"- {q}" for q in example_doubts])
                yield {"message": f"❌ I couldn't find an answer for:\n'{doubt}'\n\nTry asking:\n{available}"}
        else:
            yield {"message": "❗ Please enter your doubt in the sidebar to get it solved."}
