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


fact_sheet_chair = """
    OVERVIEW
    - Part of a beautiful family of mid-century inspired office furniture, 
    including filing cabinets, desks, bookcases, meeting tables, and more.
    - Several options of shell color and base finishes.
    - Available with plastic back and front upholstery (SWC-100) 
    or full upholstery (SWC-110) in 10 fabric and 6 leather options.
    - Base finish options are: stainless steel, matte black, 
    gloss white, or chrome.
    - Chair is available with or without armrests.
    - Suitable for home or business settings.
    - Qualified for contract use.

    CONSTRUCTION
    - 5-wheel plastic coated aluminum base.
    - Pneumatic chair adjust for easy raise/lower action.

    DIMENSIONS
    - WIDTH 53 CM | 20.87”
    - DEPTH 51 CM | 20.08”
    - HEIGHT 80 CM | 31.50”
    - SEAT HEIGHT 44 CM | 17.32”
    - SEAT DEPTH 41 CM | 16.14”

    OPTIONS
    - Soft or hard-floor caster options.
    - Two choices of seat foam densities: 
    medium (1.8 lb/ft3) or high (2.8 lb/ft3)
    - Armless or 8 position PU armrests 

    MATERIALS
    SHELL BASE GLIDER
    - Cast Aluminum with modified nylon PA6/PA66 coating.
    - Shell thickness: 10 mm.
    SEAT
    - HD36 foam

    COUNTRY OF ORIGIN
    - Italy
    """

def first_iteration():
    prompt = f"""
    Your task is to help a marketing team create a 
    description for a retail website of a product based 
    on a technical fact sheet.

    Write a product description based on the information 
    provided in the technical specifications delimited by 
    triple backticks.

    Technical specifications: ```{fact_sheet_chair}```
    """
    response = get_completion(prompt)
    print(response)
    # Introducing our stunning mid-century inspired office chair, 
    # the perfect addition to any home or business setting. Part of 
    # a beautiful family of office furniture, including filing cabinets, 
    # desks, bookcases, meeting tables, and more, this chair is 
    # available in several options of shell color and base finishes to 
    # suit your style. Choose from plastic back and front upholstery 
    # (SWC-100) or full upholstery (SWC-110) in 10 fabric and 6 leather options.

    # The chair is constructed with a 5-wheel plastic coated aluminum 
    # base and features a pneumatic chair adjust for easy raise/lower 
    # action. It is available with or without armrests and is qualified 
    # for contract use. The base finish options are stainless steel, 
    # matte black, gloss white, or chrome.

    # Measuring at a width of 53 cm, depth of 51 cm, and height of 80 cm, 
    # with a seat height of 44 cm and seat depth of 41 cm, this chair is 
    # designed for ultimate comfort. You can also choose between soft or 
    # hard-floor caster options and two choices of seat foam densities: 
    # medium (1.8 lb/ft3) or high (2.8 lb/ft3). The armrests are available 
    # in either an armless or 8 position PU option.

    # The materials used in the construction of this chair are of the 
    # highest quality. The shell base glider is made of cast aluminum 
    # with modified nylon PA6/PA66 coating and has a shell thickness 
    # of 10 mm. The seat is made of HD36 foam, ensuring maximum comfort
    #  and durability.

    # This chair is made in Italy and is the perfect combination of style 
    # and functionality. Upgrade your workspace with our mid-century
    #  inspired office chair today!


# Notes: result is too long. 

def second_iteration(): #  ask for shorter response
    prompt = f"""
    Your task is to help a marketing team create a 
    description for a retail website of a product based 
    on a technical fact sheet.

    Write a product description based on the information 
    provided in the technical specifications delimited by 
    triple backticks.

    Use at most 50 words.

    Technical specifications: ```{fact_sheet_chair}```
    """
    response = get_completion(prompt)
    print(response)
    len(response)  #  344
    # Introducing our mid-century inspired office chair, perfect for home
    #  or business settings. Available in a range of shell colors and base
    #  finishes, with or without armrests. Choose from 10 fabric and 6 
    # leather options for full or plastic upholstery. With a 5-wheel base 
    # and pneumatic chair adjust, it's both stylish and functional. Made in Italy.

#  Note: result text focuses on wrong idea

def third_iteration(): #  ask model to focus on aspects that are relevant to intended audience
    prompt = f"""
    Your task is to help a marketing team create a 
    description for a retail website of a product based 
    on a technical fact sheet.

    Write a product description based on the information 
    provided in the technical specifications delimited by 
    triple backticks.

    The description is intended for furniture retailers, 
    so should be technical in nature and focus on the 
    materials the product is constructed from.

    Use at most 50 words.

    Technical specifications: ```{fact_sheet_chair}```
    """
    response = get_completion(prompt)
    print(response)

    # Introducing our mid-century inspired office chair, perfect for both home 
    # and business settings. With a range of shell colors and base finishes, 
    # including stainless steel and matte black, this chair is available with 
    # or without armrests. The 5-wheel plastic coated aluminum base and pneumatic 
    # chair adjust make it easy to move and adjust to your desired height. 
    # Made with high-quality materials, including a cast aluminum shell and 
    # HD36 foam seat, this chair is built to last.

#  ask model to focus on aspects that are relevant to intended audience
#  ask for product id 
def fourth_iteration(): 
    prompt = f"""
    Your task is to help a marketing team create a 
    description for a retail website of a product based 
    on a technical fact sheet.

    Write a product description based on the information 
    provided in the technical specifications delimited by 
    triple backticks.

    The description is intended for furniture retailers, 
    so should be technical in nature and focus on the 
    materials the product is constructed from.

    At the end of the description, include every 7-character 
    Product ID in the technical specification.

    Use at most 50 words.

    Technical specifications: ```{fact_sheet_chair}```
    """
    response = get_completion(prompt)
    print(response)

    # Introducing our mid-century inspired office chair, perfect for 
    # home or business settings. With a range of shell colors and base 
    # finishes, and the option of plastic or full upholstery in 
    # various fabrics and leathers, this chair is both stylish and 
    # versatile. Constructed with a 5-wheel plastic coated aluminum base 
    # and pneumatic chair adjust, it's also practical. Available with or 
    # without armrests and suitable for contract use. Product IDs: SWC-100, SWC-110.

# Note: result needs a table dimensions

# ask model to extract infof and organize in a table
def fifth_iteration():
    prompt = f"""
    Your task is to help a marketing team create a 
    description for a retail website of a product based 
    on a technical fact sheet.

    Write a product description based on the information 
    provided in the technical specifications delimited by 
    triple backticks.

    The description is intended for furniture retailers, 
    so should be technical in nature and focus on the 
    materials the product is constructed from.

    At the end of the description, include every 7-character 
    Product ID in the technical specification.

    After the description, include a table that gives the 
    product's dimensions. The table should have two columns.
    In the first column include the name of the dimension. 
    In the second column include the measurements in inches only.

    Give the table the title 'Product Dimensions'.

    Format everything as HTML that can be used in a website. 
    Place the description in a <div> element.

    Technical specifications: ```{fact_sheet_chair}```
    """

    response = get_completion(prompt)
    print(response)

    # <div>
    # <h2>Mid-Century Inspired Office Chair</h2>
    # <p>Introducing our mid-century inspired office chair, part of a beautiful family of office furniture that includes filing cabinets, desks, bookcases, meeting tables, and more. This chair is available in several options of shell color and base finishes, allowing you to customize it to your liking. You can choose between plastic back and front upholstery or full upholstery in 10 fabric and 6 leather options. The base finish options are stainless steel, matte black, gloss white, or chrome. The chair is also available with or without armrests, making it suitable for both home and business settings. Plus, it's qualified for contract use, ensuring its durability and longevity.</p>
    # <p>The chair's construction features a 5-wheel plastic coated aluminum base and a pneumatic chair adjust for easy raise/lower action. You can also choose between soft or hard-floor caster options and two choices of seat foam densities: medium (1.8 lb/ft3) or high (2.8 lb/ft3). The armrests are also customizable, with the option of armless or 8 position PU armrests.</p>
    # <p>The materials used in the chair's construction are of the highest quality. The shell base glider is made of cast aluminum with modified nylon PA6/PA66 coating, with a shell thickness of 10 mm. The seat is made of HD36 foam, ensuring maximum comfort and support.</p>
    # <p>Made in Italy, this mid-century inspired office chair is the perfect addition to any office space. Order yours today!</p>
    # <h3>Product IDs:</h3>
    # <ul>
    # <li>SWC-100</li>
    # <li>SWC-110</li>
    # </ul>
    # </div>

    # <table>
    #   <caption>Product Dimensions</caption>
    #   <tr>
    #     <th>Dimension</th>
    #     <th>Measurement (inches)</th>
    #   </tr>
    #   <tr>
    #     <td>Width</td>
    #     <td>20.87"</td>
    #   </tr>
    #   <tr>
    #     <td>Depth</td>
    #     <td>20.08"</td>
    #   </tr>
    #   <tr>
    #     <td>Height</td>
    #     <td>31.50"</td>
    #   </tr>
    #   <tr>
    #     <td>Seat Height</td>
    #     <td>17.32"</td>
    #   </tr>
    #   <tr>
    #     <td>Seat Depth</td>
    #     <td>16.14"</td>
    #   </tr>
    # </table>

    # from IPython.display import display, HTML
    # display(HTML(response))