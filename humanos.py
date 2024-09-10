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
zoila = cb.Collection(name="humanos")
 
st.write("""
         **Zoológicos humanos: infamias desde la IA. Prototipo de sistema QA.**""")

query_str = st.text_input("Pregunta algo sobre los zoológicos humanos. Además de ser respetuosos, te sugerimos formular preguntas específicas.",
                          value="¿qué son los zoológicos humanos?")

answer = dict(zoila.ask(query_str))

st.write("""
         **respuesta**
""")
st.write(answer['answer'])

st.write("""
         **referencias**
""")
st.write(answer['refs'])