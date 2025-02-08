import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from helper import *

# Heading
st.markdown("""
<style>
    #MainMenu
    {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)
st.markdown("""
Made with ❤️ by [Soumya](https://github.com/imsoumya18)\n
Star ⭐ this repo on [GitHub](https://github.com/imsoumya18/SavageCV)
""", unsafe_allow_html=True)
st.title("SavageCV 🤪")
st.write("Roast yourself 😈")

# Sidebar
with st.sidebar:
    st.title('SavageCV 🤪')
    st.markdown('''
    ## About
    This app is an LLM-powered CV roaster built using:
    - [Streamlit](https://streamlit.io/)
    - [OpenAI](https://platform.openai.com/docs/models) LLM model

    ''')
    add_vertical_space(5)
    st.write('Made with ❤️ by [Soumya](https://github.com/imsoumya18)')


def main():
    # upload a PDF file
    uploaded_file = st.file_uploader("Choose a PDF", type="pdf")
    lang = st.text_input("Enter language (Optional, default: English)")

    if uploaded_file is not None:
        # Save uploaded file to a temporary location
        with open("uploaded_temp.pdf", "wb") as temp_file:
            temp_file.write(uploaded_file.read())

        # Extract text using the provided function
        extracted_text = read_pdf("uploaded_temp.pdf")

        if extracted_text:
            st.write(get_openai_response(extracted_text, lang))


if __name__ == '__main__':
    main()
