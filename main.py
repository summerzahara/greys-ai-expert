from llm_helper import generate_summary
import streamlit as st

st.title('Grey Character Summaries')

character = st.text_input(
    "Enter Character Name:",
    placeholder="Meredith Grey"
)

generate = st.button(
    "Generate",
    type="primary",
)

if character and generate:
    response = generate_summary(character)
    st.write(response['char_summary'])
