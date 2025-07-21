import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory

# Load environment variables from .env file
load_dotenv()
openai_api_key = os.environ["OPENAI_API_KEY"]

# Load the model
llm = OpenAI(
    openai_api_key=openai_api_key,
    temperature=0.7,
    model_name="gpt-3.5-turbo-instruct"
)

# Memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True, output_key="summary")

# Title Generator
title_prompt = PromptTemplate.from_template("Write a catchy blog title about {topic}")
title_chain = LLMChain(llm=llm, prompt=title_prompt, output_key="title")

# Intro Generator
intro_prompt = PromptTemplate.from_template("Write an engaging intro for a blog titled '{title}'")
intro_chain = LLMChain(llm=llm, prompt=intro_prompt, output_key="intro")

# Main Content Generator
main_prompt = PromptTemplate.from_template("Based on the intro: '{intro}', write the main content of the blog.")
main_chain = LLMChain(llm=llm, prompt=main_prompt, output_key="main")

# Summary Generator
summary_prompt = PromptTemplate.from_template("Based on the blog content: '{main}', write a concise summary.")
summary_chain = LLMChain(llm=llm, prompt=summary_prompt, output_key="summary")

# Sequential Chain
blog_chain = SequentialChain(
    chains=[title_chain, intro_chain, main_chain, summary_chain],
    input_variables=["topic"],
    output_variables=["title", "intro", "main", "summary"],
    memory=memory,
    verbose=True
)

def generate_blog_from_topic(topic: str):
    result = blog_chain.invoke({"topic": topic})
    return {
        "title": result["title"],
        "intro": result["intro"],
        "mainContent": result["main"],
        "summary": result["summary"],
    }

# response = generate_blog_from_topic("The Future of AI in Everyday Life")
# print(response)