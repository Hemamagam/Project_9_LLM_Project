from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import fitz  # PyMuPDF

# Read the PDF content
pdf_path = 'TOI Delhi 23 Jul 2023.pdf'
pdf_document = fitz.open(pdf_path)
pdf_content = ""

for page_num in range(len(pdf_document)):
    page = pdf_document.load_page(page_num)
    pdf_content += page.get_text()

# OpenAI API key
openai_api_key = 
openai = OpenAI(api_key=openai_api_key)

# Prompt template
template = """
You are an AI assistant helping an equity research analyst. Given
the following query and PDF content, summarize the most relevant news articles.
Query: {query}
PDF Content: {pdf_content}
"""
prompt = PromptTemplate(template=template, input_variables=['query', 'pdf_content'])

# LLM Chain
llm_chain = LLMChain(prompt=prompt, llm=openai)

# Example query
query = "Latest news on Delhi markets"
response = llm_chain.run(query=query, pdf_content=pdf_content)

print(response)