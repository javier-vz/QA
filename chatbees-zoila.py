# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 19:59:09 2024

@author: u_humanidades
"""

import chatbees as cb
import streamlit as st

# Create an API key on UI after signup/signin.
# Configure cb to use the newly minted API key.
cb.init(api_key="MDItMDAwMDAwMDAtNWY0OTdkODUtYjNlYy1hNjBhLTZkNjUtYmRjYzViMjNiZjc0", account_id="SALTCRC6")

# Create a new collection
ira = cb.Collection(name="zoila")
 
st.write("""
         **Prototipo de buscador en la obra de Zoila Cáceres**
""")

query_str = st.text_input("Pregunta algo sobre la obra de Zoila Cáceres",
                          value="Qué hicieron Dina Cornejo y Mariana Reyes?")

answer, refs = ira.ask(query_str)

st.write(answer)
st.write(refs)