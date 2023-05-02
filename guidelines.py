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


# principle 1: clear and specific instructions

def principle1_tatic1():  #  delimiters
    text = f"""
    You should express what you want a model to do by \ 
    providing instructions that are as clear and \ 
    specific as you can possibly make them. \ 
    This will guide the model towards the desired output, \ 
    and reduce the chances of receiving irrelevant \ 
    or incorrect responses. Don't confuse writing a \ 
    clear prompt with writing a short prompt. \ 
    In many cases, longer prompts provide more clarity \ 
    and context for the model, which can lead to \ 
    more detailed and relevant outputs.
    """
    prompt = f"""
    Summarize the text delimited by triple backticks \ 
    into a single sentence.
    ```{text}```
    """
    response = get_completion(prompt)
    print(response)

    # To guide a model towards the desired output and reduce the 
    # chances of irrelevant or incorrect responses, it is important 
    # to provide clear and specific instructions, which may be longer 
    # prompts that provide more clarity and context for the model.


def principle2_tatic2():  #  structured output 
    prompt = f"""
    Generate a list of three made-up book titles along \ 
    with their authors and genres. 
    Provide them in JSON format with the following keys: 
    book_id, title, author, genre.
    """
    response = get_completion(prompt)
    print(response)

    # [
    #     {
    #         "book_id": 1,
    #         "title": "The Lost City of Zorath",
    #         "author": "Aria Blackwood",
    #         "genre": "Fantasy"
    #     },
    #     {
    #         "book_id": 2,
    #         "title": "The Last Survivors",
    #         "author": "Ethan Stone",
    #         "genre": "Science Fiction"
    #     },
    #     {
    #         "book_id": 3,
    #         "title": "The Secret Life of Bees",
    #         "author": "Lila Rose",
    #         "genre": "Romance"
    #     }
    # ]


def principle1_tatic3_example1():  #  conditions
    text_1 = f"""
    Making a cup of tea is easy! First, you need to get some \ 
    water boiling. While that's happening, \ 
    grab a cup and put a tea bag in it. Once the water is \ 
    hot enough, just pour it over the tea bag. \ 
    Let it sit for a bit so the tea can steep. After a \ 
    few minutes, take out the tea bag. If you \ 
    like, you can add some sugar or milk to taste. \ 
    And that's it! You've got yourself a delicious \ 
    cup of tea to enjoy.
    """
    prompt = f"""
    You will be provided with text delimited by triple quotes. 
    If it contains a sequence of instructions, \ 
    re-write those instructions in the following format:

    Step 1 - ...
    Step 2 - …
    …
    Step N - …

    If the text does not contain a sequence of instructions, \ 
    then simply write \"No steps provided.\"

    \"\"\"{text_1}\"\"\"
    """
    response = get_completion(prompt)
    print("Completion for Text 1:")
    print(response)

    # Completion for Text 1:
    # Step 1 - Get some water boiling.
    # Step 2 - Grab a cup and put a tea bag in it.
    # Step 3 - Once the water is hot enough, pour it over the tea bag.
    # Step 4 - Let it sit for a bit so the tea can steep.
    # Step 5 - After a few minutes, take out the tea bag.
    # Step 6 - Add some sugar or milk to taste.
    # Step 7 - Enjoy your delicious cup of tea!


def principle1_tatic3_example2():  #  conditions
    text_2 = f"""
    The sun is shining brightly today, and the birds are \
    singing. It's a beautiful day to go for a \ 
    walk in the park. The flowers are blooming, and the \ 
    trees are swaying gently in the breeze. People \ 
    are out and about, enjoying the lovely weather. \ 
    Some are having picnics, while others are playing \ 
    games or simply relaxing on the grass. It's a \ 
    perfect day to spend time outdoors and appreciate the \ 
    beauty of nature.
    """
    prompt = f"""
    You will be provided with text delimited by triple quotes. 
    If it contains a sequence of instructions, \ 
    re-write those instructions in the following format:

    Step 1 - ...
    Step 2 - …
    …
    Step N - …

    If the text does not contain a sequence of instructions, \ 
    then simply write \"No steps provided.\"

    \"\"\"{text_2}\"\"\"
    """
    response = get_completion(prompt)
    print("Completion for Text 2:")
    print(response)

    # Completion for Text 2:
    # No steps provided.


def principle1_tatic4():  #  few-shot
    prompt = f"""
    Your task is to answer in a consistent style.

    <child>: Teach me about patience.

    <grandparent>: The river that carves the deepest \ 
    valley flows from a modest spring; the \ 
    grandest symphony originates from a single note; \ 
    the most intricate tapestry begins with a solitary thread.

    <child>: Teach me about resilience.
    """
    response = get_completion(prompt)
    print(response)

    # <grandparent>: Resilience is like a tree that bends with the 
    # wind but never breaks. It is the ability to bounce back from 
    # adversity and keep moving forward, even when things get tough. 
    # Just like a tree that grows stronger with each storm it weathers, 
    # resilience is a quality that can be developed and strengthened over time.


# principle 2 = give model time to think

text = f"""
    In a charming village, siblings Jack and Jill set out on \ 
    a quest to fetch water from a hilltop \ 
    well. As they climbed, singing joyfully, misfortune \ 
    struck—Jack tripped on a stone and tumbled \ 
    down the hill, with Jill following suit. \ 
    Though slightly battered, the pair returned home to \ 
    comforting embraces. Despite the mishap, \ 
    their adventurous spirits remained undimmed, and they \ 
    continued exploring with delight.
    """

def principle2_tatic1():  #  specift steps
    # example 1
    prompt_1 = f"""
    Perform the following actions: 
    1 - Summarize the following text delimited by triple \
    backticks with 1 sentence.
    2 - Translate the summary into French.
    3 - List each name in the French summary.
    4 - Output a json object that contains the following \
    keys: french_summary, num_names.

    Separate your answers with line breaks.

    Text:
    ```{text}```
    """
    response = get_completion(prompt_1)
    print("Completion for prompt 1:")
    print(response)

    # Completion for prompt 1:
    # Two siblings, Jack and Jill, go on a quest to fetch water from a well on a hilltop, but misfortune strikes and they both tumble down the hill, returning home slightly battered but with their adventurous spirits undimmed.

    # Deux frères et sœurs, Jack et Jill, partent en quête d'eau d'un puits sur une colline, mais un malheur frappe et ils tombent tous les deux de la colline, rentrant chez eux légèrement meurtris mais avec leurs esprits aventureux intacts. 
    # Noms: Jack, Jill. 

    # {
    #   "french_summary": "Deux frères et sœurs, Jack et Jill, partent en quête d'eau d'un puits sur une colline, mais un malheur frappe et ils tombent tous les deux de la colline, rentrant chez eux légèrement meurtris mais avec leurs esprits aventureux intacts.",
    #   "num_names": 2
    # }


def principle2_tatic2():  #  ask output in specific format
    prompt_2 = f"""
    Your task is to perform the following actions: 
    1 - Summarize the following text delimited by 
    <> with 1 sentence.
    2 - Translate the summary into French.
    3 - List each name in the French summary.
    4 - Output a json object that contains the 
    following keys: french_summary, num_names.

    Use the following format:
    Text: <text to summarize>
    Summary: <summary>
    Translation: <summary translation>
    Names: <list of names in Italian summary>
    Output JSON: <json with summary and num_names>

    Text: <{text}>
    """
    response = get_completion(prompt_2)
    print("\nCompletion for prompt 2:")
    print(response)

    # Completion for prompt 2:
    # Summary: Jack and Jill go on a quest to fetch water, but misfortune strikes and they tumble down the hill, returning home slightly battered but with their adventurous spirits undimmed. 
    # Translation: Jack et Jill partent en quête d'eau, mais la malchance frappe et ils dégringolent la colline, rentrant chez eux légèrement meurtris mais avec leurs esprits aventureux intacts.
    # Names: Jack, Jill
    # Output JSON: {"french_summary": "Jack et Jill partent en quête d'eau, mais la malchance frappe et ils dégringolent la colline, rentrant chez eux légèrement meurtris mais avec leurs esprits aventureux intacts.", "num_names": 2}


def principle2_tatic3_example1():  #  ask model to work out it's own solution before rushing to a conclusion
    prompt = f"""
    Determine if the student's solution is correct or not.

    Question:
    I'm building a solar power installation and I need \
    help working out the financials. 
    - Land costs $100 / square foot
    - I can buy solar panels for $250 / square foot
    - I negotiated a contract for maintenance that will cost \ 
    me a flat $100k per year, and an additional $10 / square \
    foot
    What is the total cost for the first year of operations 
    as a function of the number of square feet.

    Student's Solution:
    Let x be the size of the installation in square feet.
    Costs:
    1. Land cost: 100x
    2. Solar panel cost: 250x
    3. Maintenance cost: 100,000 + 100x
    Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
    """
    response = get_completion(prompt)
    print(response)
    # The student's solution is correct.

    # Note: Student solution is actually not correct. 
    #       Total cost calculation is correct but the overall solution is incorrect.
    #       Additional maintenance cost should be 10x and not 100x.
    #       Model "scans" vs "think".
    #       principle2_tatic2_example2() will fix issue by instructing model to work out it's own solution first.


def principle2_tatic3_example2():  
    prompt = f"""
    Your task is to determine if the student's solution \
    is correct or not.
    To solve the problem do the following:
    - First, work out your own solution to the problem. 
    - Then compare your solution to the student's solution \ 
    and evaluate if the student's solution is correct or not. 
    Don't decide if the student's solution is correct until 
    you have done the problem yourself.

    Use the following format:
    Question:
    ```
    question here
    ```
    Student's solution:
    ```
    student's solution here
    ```
    Actual solution:
    ```
    steps to work out the solution and your solution here
    ```
    Is the student's solution the same as actual solution \
    just calculated:
    ```
    yes or no
    ```
    Student grade:
    ```
    correct or incorrect
    ```

    Question:
    ```
    I'm building a solar power installation and I need help \
    working out the financials. 
    - Land costs $100 / square foot
    - I can buy solar panels for $250 / square foot
    - I negotiated a contract for maintenance that will cost \
    me a flat $100k per year, and an additional $10 / square \
    foot
    What is the total cost for the first year of operations \
    as a function of the number of square feet.
    ``` 
    Student's solution:
    ```
    Let x be the size of the installation in square feet.
    Costs:
    1. Land cost: 100x
    2. Solar panel cost: 250x
    3. Maintenance cost: 100,000 + 100x
    Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
    ```
    Actual solution:
    """
    response = get_completion(prompt)
    # print(response)
    # Let x be the size of the installation in square feet.

    # Costs:
    # 1. Land cost: 100x
    # 2. Solar panel cost: 250x
    # 3. Maintenance cost: 100,000 + 10x

    # Total cost: 100x + 250x + 100,000 + 10x = 360x + 100,000

    # Is the student's solution the same as actual solution just calculated:
    # No

    # Student grade:
    # Incorrect


if __name__ == "__main__":
    principle2_tatic3_example2()