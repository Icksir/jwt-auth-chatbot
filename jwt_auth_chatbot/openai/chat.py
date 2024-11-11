from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from jwt_auth_chatbot.openai.prompts import qa_template

def conversation(context, question):

    model = ChatOpenAI(model="gpt-4o")

    chain = qa_template | model | StrOutputParser()
    result = chain.invoke({"context": context, "question": question})

    return result