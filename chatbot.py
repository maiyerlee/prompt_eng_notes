import openai 
import os

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
openai.api_key  = os.getenv('OPENAI_API_KEY')


# helper function
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )

    return response.choices[0].message["content"]


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]


def ex1():
    messages =  [  
        {'role':'system', 'content':'You are an assistant that speaks like Shakespeare.'},    
        {'role':'user', 'content':'tell me a joke'},   
        {'role':'assistant', 'content':'Why did the chicken cross the road'},   
        {'role':'user', 'content':'I don\'t know'}  
    ]
    response = get_completion_from_messages(messages, temperature=1)
    print(response)
    #  To get to the other side, verily! A classic jest, methinks.
    #  'Twas a quest to reach th' oth'r side, my good fellow!


def ex2():
    messages =  [  
        {'role':'system', 'content':'You are friendly chatbot.'},    
        {'role':'user', 'content':'Hi, my name is Isa'}  
    ]
    response = get_completion_from_messages(messages, temperature=1)
    print(response)
    # Hello Isa, it's nice to meet you. How can I assist you today?


def ex3():
    messages =  [  
        {'role':'system', 'content':'You are friendly chatbot.'},    
        {'role':'user', 'content':'Yes,  can you remind me, What is my name?'}  
    ]
    response = get_completion_from_messages(messages, temperature=1)
    print(response)
    # I apologize, but since we are communicating through a computer, 
    # I do not have access to your name. Can you please provide me with your name?


def ex4():
    messages =  [  
        {'role':'system', 'content':'You are friendly chatbot.'},
        {'role':'user', 'content':'Hi, my name is Isa'},
        {'role':'assistant', 'content': "Hi Isa! It's nice to meet you. \
        Is there anything I can help you with today?"},
        {'role':'user', 'content':'Yes, you can remind me, What is my name?'}  
    ]
    response = get_completion_from_messages(messages, temperature=1)
    print(response)
    #  Your name is Isa, you mentioned it earlier. Is there anything else you need help with?'


# ChatBot Example

