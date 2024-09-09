# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 19:59:09 2024

@author: u_humanidades
"""
import streamlit as st
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

lambda_val = float(st.text_input("Elige el grado de alucinación:",value="0.005"))

config = VectaraQueryConfig(
    k=10, lambda_val=lambda_val, rerank_config=rerank_config, summary_config=summary_config
)


st.write("""
         **Prototipo de sistema QA con la obra de Zoila Cáceres** Parte del [álbum](https://repositorio.pucp.edu.pe/index/handle/123456789/64206) de Zoila Cáceres
         , la [base de datos](https://datos.pucp.edu.pe/dataset.xhtml?persistentId=hdl:20.500.12534/VDSQKG) disponible [aquí](https://datos.pucp.edu.pe/), entre otros documentos, forman el conocimiento de esta 
         inteligencia artificial. 
""")

query_str = st.text_input("Pregunta algo sobre la obra de Zoila Cáceres. En lo posible, te sugerimos formular preguntas específicas.",
                          value="¿qué documentos hablan del centro social?")

rag = vectara.as_chat(config)
resp = rag.invoke(query_str)

st.write("""
         **respuesta :)**
""")
st.write(resp['answer'])
