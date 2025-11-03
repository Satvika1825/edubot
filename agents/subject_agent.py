from pydantic import BaseModel

class AgentInput(BaseModel):
    subject: str
    topic: str

class SubjectAgent:
    def __init__(self):
        self.explanations = {
            "math": {
                "algebra": """Algebraic expressions are combinations of numbers, variables (like x, y), and mathematical operations (addition, subtraction, multiplication, division). They are fundamental in algebra and can represent a wide range of mathematical relationships and calculations.

Here's a more detailed explanation:
Key Components:
- Constants: These are fixed numerical values, like 3, -5, or 1/2.
- Variables: These are symbols (usually letters) that represent unknown or changing values.
- Operations: These are the mathematical actions that connect constants and variables, including addition (+), subtraction (-), multiplication (× or implied), and division (÷ or /).

Examples:
- 5x + 2: This expression includes the variable x, the constant 2, and the operations of multiplication (by 5) and addition.
- 3y - 7: This expression involves the variable y, the constant 7, and operations of multiplication (by 3) and subtraction.
- 4xy + 2x - 5: This expression has two variables, x and y, constants 4, 2, and -5, and the operations of multiplication and addition/subtraction.
- (a + b) / c: This expression includes variables a, b, and c, and operations of addition and division.
""",
                "geometry": "Geometry deals with shapes, angles, and sizes.",
                "calculus": "Calculus studies change using derivatives and integrals.",
                "linear algebra": "Linear Algebra focuses on vector spaces and matrix operations.",
                "differential equations": "It involves solving equations that relate functions with their derivatives."
            },
            "science": {
                "photosynthesis": "Photosynthesis is the process by which plants convert carbon dioxide and water into chemical energy and oxygen using light energy from the sun. It is the basis of all life on Earth, as it produces the oxygen that we breathe. The process takes place in the chloroplasts of the plant cells",
                "gravity": "Gravity is a force that pulls objects toward each other.",
                "atom": "An atom is the smallest unit of matter.",
                "thermodynamics": "Thermodynamics deals with heat, work, and energy in physical systems.",
                "electromagnetism": "It studies electric and magnetic fields and how they interact."
            },
            "english": {
                "noun": "A noun is a person, place, thing, or idea.",
                "verb": "A verb expresses an action or state of being.",
                "adjective": "An adjective describes a noun.",
                "essay writing": "Essay writing involves structured writing with an introduction, body, and conclusion.",
                "report writing": "Report writing presents factual information in a formal layout."
            },
            "computer science": {
                "data structures": "Data structures are ways to organize and store data for efficient access.",
                "algorithms": "Algorithms are step-by-step procedures to solve problems.",
                "operating systems": "Operating systems manage hardware and software resources.",
                "dbms": "DBMS stands for Database Management System and is used to store and manage data efficiently.",
                "networking": "Computer Networking deals with communication between computers and devices."
            },
            "electronics": {
                "digital circuits": "Digital circuits use binary signals to perform logical operations.",
                "microprocessors": "Microprocessors are small CPUs used to control electronic devices.",
                "semiconductors": "Semiconductors are materials used to build transistors and diodes.",
                "communication systems": "They involve transmission and reception of data over distances."
            }
        }

    async def run_async(self, input: AgentInput):
        subject = input.subject.strip().lower()
        topic = input.topic.strip().lower()
        explanation = self.explanations.get(subject, {}).get(topic)

        if explanation:
            yield {"message": explanation}
        else:
            yield {"message": f"Sorry, no explanation found for '{topic}' in '{subject}'."}