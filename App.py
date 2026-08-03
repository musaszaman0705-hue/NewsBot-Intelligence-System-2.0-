import streamlit as st
from newsbot import NewsBot2, NewsBotAssistant


st.title("📰 NewsBot 2.0")
st.write(
    "AI-powered news analysis assistant"
)


bot = NewsBot2()
assistant = NewsBotAssistant(bot)


article = st.text_area(
    "Paste your news article here"
)


query = st.text_input(
    "Ask NewsBot a question"
)


if st.button("Analyze"):

    if article and query:

        response = assistant.chat(
            query,
            article
        )

        st.write(response)

    else:
        st.warning(
            "Please enter an article and question."
        )
