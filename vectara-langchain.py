# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 19:04:03 2024

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
                vectara_corpus_id=2,
                vectara_api_key="zwt_nDJrRzeXqkymaH-tptpheMyOCzm4oL_NKD9hOw"
            )


summary_config = SummaryConfig(is_enabled=True, max_results=5, response_lang="eng", prompt_name='vectara-summary-ext-24-05-sml'
                               , citations='html', url_pattern='https://mypdf.doc/foo/{doc.id}#page={part.page}')
rerank_config = RerankConfig(reranker="mmr", rerank_k=50, mmr_diversity_bias=0.1)
config = VectaraQueryConfig(
    k=10, lambda_val=0.0075, rerank_config=rerank_config, summary_config=summary_config
)

query_str = "¿Por qué los danzantes usan máscaras?"

rag = vectara.as_rag(config)
resp = rag.invoke(query_str)
print(resp["answer"])
print(f"Vectara FCS = {resp['fcs']}")

