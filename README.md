# FinLLM 🏦 - Financial AI Agent 

# What is this repo?
FinLLM is an AI agent for financial documents.

Features:
- Generative legals: Generate and query legal private fund documents
- Generative research: Generate and query investment memos
- Generative compliance: Generate and query regulatory filings

![FinLLM Logo](https://i.ibb.co/ryRCKvc/Screenshot-2023-10-07-at-16-52-49.png)

This README provides an overview of the FinLLM project and can be added to the project's GitHub repository to provide information to visitors and potential collaborators.

# Technology used

![FinLLM Logo](https://github.com/pinecone-io/examples/raw/master/learn/images/pinecone_logo_w_background.png)
![FinLLM Logo](https://uploads-ssl.webflow.com/62a8755be8bcc86e6307def8/645b98e5fd715675483a4100_Untitled-2.png)
![FinLLM Logo](https://ml.globenewswire.com/Resource/Download/3034f6cd-48c3-4b5e-bd7f-242dbaecaab4?size=2)

# User Guide
To run, first add your OpenAI API key and Pinecone API key to your environment and install the requirements. To run the streamlit demo run: streamlit run st_finllm_demo.py

```python
llm = OpenAI(model="gpt-3.5-turbo")
openai.api_key = os.environ.get("OPENAI_API_KEY")
pinecone_api_key =  os.environ.get("PINECONE_API_KEY")
# api_key = ""
environment = "gcp-starter"
index_name = "pellm"
