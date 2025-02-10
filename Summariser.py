from llama_index.core import SummaryIndex, SimpleDirectoryReader
from llama_index.readers.web import SimpleWebPageReader
import openai
from colorama import Fore
import os
import httpx
from playwright.sync_api import Playwright, sync_playwright
import time as sleep
from llama_index.llms.openai import OpenAI
from llama_index.core import get_response_synthesizer
from llama_index.core.postprocessor import SentenceEmbeddingOptimizer
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.retrievers import SummaryIndexRetriever
from llama_index.llms.openai import OpenAI 
from colorama import Fore
import sqlite3 
import openai
import logging
import sys
from llama_index.core.llms import ChatMessage

#logging.basicConfig(stream=sys.stdout, level=logging.INFO)
#logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

openai.api_key = ''

def website():
    link = input("Enter the URL of the article: ")
    text = SimpleWebPageReader(html_to_text=True).load_data([link])
    return text

def pdf():
    link = input("Enter the URL of the PDF: ")
    response = httpx.get(link)
    response.raise_for_status()
    with open('temp.pdf', 'wb') as file:
        file.write(response.content)
    text = SimpleDirectoryReader(input_files=["temp.pdf"]).load_data()
    file_path = 'temp.pdf'
    if os.path.isfile(file_path):
        os.remove(file_path)
    return text

def word():
    link = input("Enter context: ")
    with open('temp.txt', 'w') as file:
        file.write(link)
    text = SimpleDirectoryReader(input_files=["temp.txt"]).load_data()
    file_path = 'temp.txt'
    if os.path.isfile(file_path):
        os.remove(file_path)
    return text

def youtube(playwright: Playwright):
    link = input("Enter the URL of the YouTube video: ")
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://kome.ai/tools/youtube-transcript-generator")
    page.get_by_placeholder("Enter a YouTube URL").click()
    page.get_by_placeholder("Enter a YouTube URL").fill(link)
    page.get_by_label("Generate Transcript").click()
    sleep.sleep(3)
    transcript_div = page.query_selector('.form_transcript__lUrwL')
    transcript = page.evaluate('(element) => element.textContent', transcript_div)
    context.close()
    browser.close()
    with open('temp.txt', 'w') as file:
        file.write(transcript)
    text = SimpleDirectoryReader(input_files=["temp.txt"]).load_data()
    file_path = 'temp.txt'
    if os.path.isfile(file_path):
        os.remove(file_path)
    return text

def query(text):
    index = SummaryIndex.from_documents(text, chunk_size=128)
    llm = OpenAI(model="gpt-3.5-turbo", temperature=0.2, frequency_penalty=10, presence_penalty=10, max_tokens=2048)
    retriever = SummaryIndexRetriever(index=index, similarity_top_k=2, similarity_threshold=0.7)
    response_synthesizer = get_response_synthesizer(response_mode="refine")
    postprocessor = SentenceEmbeddingOptimizer(percentile_cutoff=0.7, threshold_cutoff=0.7)
    query_engine = RetrieverQueryEngine.from_args(response_mode="Node", retriever=retriever, response_synthesizer=response_synthesizer, postprocessor=postprocessor)
    while True:
        prompt = input("Enter your query (or 'exit' to stop): ") 
        if prompt.lower() == 'exit':
            break
        query_engine = index.as_query_engine(llm=llm)
        response = query_engine.query(prompt)
        print(Fore.GREEN + "Summariser: " + str(response))

while True:
    choice = input("1. YouTube\n2. Website\n3. PDF\n4. Word\nChoose an option: ")
    if choice == '1':
        with sync_playwright() as playwright:
            query(text=youtube(playwright))
    elif choice == '2':
        query(text=website())
    elif choice == '3':
        query(text=pdf())
    elif choice == '4':
        query(text=word())
    else:
        print("Invalid choice. Please try again.")