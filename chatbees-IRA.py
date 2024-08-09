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
ira = cb.Collection(name="IRA")
 
st.write("""
         **Prototipo de buscador en las colecciones del Archivo Histórico IRA**
""")

query_str = st.text_input("Pregunta algo sobre las colección del Archivo Histórico IRA",
                          value="Qué recortes periodísticos en la colección Belaúnde son los de años 60?")

st.write(ira.ask(query_str))