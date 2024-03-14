from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from icecream import ic

load_dotenv()


def generate_summary(character):
    llm = OpenAI()

    my_prompt = '''
    List five characters who have been in the show Grey's Anatomy.
    '''
    my_prompt_2 = '''
    You are an expert on the TV show Grey's Anatomy. Given a character name: {name}, respond with a brief summary of the character, including their surgical specialty. If the name provided is not a character on the show, respond with "This is not a character from Grey's Anatomy
    '''

    my_prompt_template = PromptTemplate(
        input_variables=['name'],
        template=my_prompt_2,
    )

    my_chain = LLMChain(
        llm=llm,
        prompt=my_prompt_template,
        output_key='char_summary'
    )

    # result = llm.invoke(my_prompt)
    result = my_chain.invoke(
        {'name': character}
    )

    # ic(result)
    return result


ic(generate_summary('kyle'))
