# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 19:59:09 2024

@author: u_humanidades
"""

from langchain_community.vectorstores import Vectara
from langchain_community.vectorstores.vectara import (
    RerankConfig,
    SummaryConfig,
    VectaraQueryConfig,
)

vectara = Vectara(
                vectara_customer_id="2620549959",
                vectara_corpus_id=3,
                vectara_api_key="zwt_nDJrR3I0qtxKa5LPd3GgGzJp1O2AvzjAUEUl6Q"
            )


summary_config = SummaryConfig(is_enabled=True, max_results=5, response_lang="spa")
rerank_config = RerankConfig(reranker="mmr", rerank_k=50, mmr_diversity_bias=0.1)
config = VectaraQueryConfig(
    k=10, lambda_val=0.005, rerank_config=rerank_config, summary_config=summary_config
)

import streamlit as st
 
st.write("""
# Prototipo de *buscador!*
""")

query_str = st.chat_input("Pregunta algo sobre el Archivo Histórico IRA!")

rag = vectara.as_chat(config)
resp = rag.invoke(query_str)

st.write("La IA piensa que: " + resp["answer"])

import streamlit.components.v1 as components

components.html("""
<!DOCTYPE html>
<html>
  <head>
    <title>Hello, World!</title>
  </head>
  <body>
      <h1 class='title'>Hello World! </h1>
      <script src='https://www.chatbees.ai/embed.js' aid='SALTCRC6' colname='IRA' logoUrl='https://www.chatbees.ai/chatbees_logo_favicon_white.svg' brandName='Chatbees' thinkingHint='Bees are thinking...'></script>
  </body>
</html>""")