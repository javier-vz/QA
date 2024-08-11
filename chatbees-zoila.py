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
zoila = cb.Collection(name="zoila")

# Add custom CSS to hide the GitHub icon
hide_github_icon = """
#GithubIcon {
  visibility: hidden;
}
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)
 
st.write("""
         **Prototipo de sistema QA con la obra de Zoila Cáceres!** Parte del [álbum](https://repositorio.pucp.edu.pe/index/handle/123456789/64206) de Zoila Cáceres
         , la [base de datos](https://datos.pucp.edu.pe/dataset.xhtml?persistentId=hdl:20.500.12534/VDSQKG) (disponible [aquí](https://datos.pucp.edu.pe/)), entre otros documentos, forman el conocimiento de esta 
         inteligencia artificial. 
""")

query_str = st.text_input("Pregunta algo sobre la obra de Zoila Cáceres. En lo posible, te sugerimos formular preguntas específicas.",
                          value="qué documentos hablan del centro social?")

answer = dict(zoila.ask(query_str))

st.write("""
         **respuesta :)**
""")
st.write(answer['answer'])

st.write("""
         **referencias**
""")
st.write(answer['refs'])