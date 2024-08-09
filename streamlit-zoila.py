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
                vectara_corpus_id=4,
                vectara_api_key="zwt_nDJrRwRHtr31pOA0qHxov2hKV61hdrbFupsptQ"
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

query_str = st.chat_input("Pregunta algo sobre el álbum de Zoila!")

rag = vectara.as_chat(config)
resp = rag.invoke(query_str)

st.write("La IA piensa que: " + resp["answer"])

