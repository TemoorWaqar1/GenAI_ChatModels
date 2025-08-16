from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=6, max_completion_tokens=10)

result = model.invoke("What is national food of Pakistan?")
print(result
print(result.content)