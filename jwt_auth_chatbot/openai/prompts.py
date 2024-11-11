from jwt_auth_chatbot.api.models import User
from langchain.prompts import ChatPromptTemplate

def generate_context(user: User) -> str:
    context =  f"""
    User profile: 
    ID: {user.id} 
    Username: {user.username}
    Email: {user.email}
    Age: {user.age}
    Fitness level: {user.level}
    """

    return context

qa_template_system = """
You are CoachAI, an intelligent virtual fitness coach dedicated to providing personalized workout and nutrition advice.
You always greet the user with his or her username.

With a deep understanding of the users fitness level, you can provide tailored workout plans and nutrition advice to help them achieve their fitness goals.
Always encouraging and positive, you are committed to helping users stay motivatd and achieve their fitness goals.

{context}
"""

qa_template_human = """
User query: {question}
CoachAI's advice:
"""

qa_template = ChatPromptTemplate.from_messages(
    [
        ("system", qa_template_system),
        ("human", qa_template_human)
    ]
)

