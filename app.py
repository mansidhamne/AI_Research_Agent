import streamlit as st
import os
from mem0 import Memory
from openai import OpenAI
from multion.client import MultiOn

st.title("AI Research Assistant")

api_keys = {
    k: st.text_input(f"{k.capitalize()} API Key", type="password")
    for k in ["openai", "multion"]
}

if all(api_keys.values()):
    os.environ["OPENAI_API_KEY"] = api_keys["openai"]
    config = {
        "vector_store": {
            "provider": "qdrant",
            "config": {
                "model" : "gpt-4o-mini",
                "host" : "localhost",
                "port" : 6333,
            }
        }
    }
    memory = Memory.from_config(config)
    multion = MultiOn(api_key=api_keys["multion"])
    openai_client = OpenAI(api_key=api_keys["openai"])

    user_id = st.sidebar.text_input("Username")
    search = st.text_input("Enter the search query")

    def process_with_gpt(result):
        prompt = f"""
        Based on the following search result, provide a proper output in markdown, readable for users.
        Include title, year of publication, authors, abstract, and link to the paper. Display 5 papers at a time.
        Result : {result}
        Output: Table with the following columns: [{{'title': "Title", 'authors': "Authors", 'abstract':"Abstract", 'link':"Link"}}, ...]
        """
        res = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": prompt
            }],
            temperature=0.2
        )
        return res.choices[0].message.content

    if st.button("Search"):
        with st.spinner('Scouring for papers...'):
            memories = memory.search(search, user_id = user_id, limit = 3)
            prompt = f"Search for papers IEEE: {search}\nPrevious searches: {' '.join(mem['text'] for mem in memories)}"
            result = process_with_gpt(multion.browse(cmd=prompt, url="https://ieeexplore.ieee.org/Xplore/home.jsp"))
            st.markdown(result)

    if st.sidebar.button("View Memory"):
        st.sidebar.write("\n".join([f"- {mem['text']}" for mem in memory.get_all(user_id=user_id)]))