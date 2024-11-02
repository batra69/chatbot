from langchain_cohere import ChatCohere
import os
from django.conf import settings

def get_llm():
    os.environ['COHERE_API_KEY'] = settings.COHERE_API_KEY #please enter your api key in settings.py file for safety of key
    return ChatCohere()


def chatbot_reply(query):
    llm=get_llm()
    # temp=f"{query} give the response in structured format and please only include answer to the query in your response"
    response=llm.invoke(query)
    return str(response.content)

# if __name__=='__main__':
#     import langchain_cohere
#     print(dir(langchain_cohere))



