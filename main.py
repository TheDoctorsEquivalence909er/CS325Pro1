# -----------------------------------------------------------------------------
# Project: CS325 Project 1 
# Author: Francesco henrichs
# Email: jane.doe@example.com
# License: Apache License 2.0
# Created: September 2024
# -----------------------------------------------------------------------------
# Description:
# Takes in a text file respones to it with A.I and puts that respones in text file
# It takes user input, processes the data, and outputs the result.
# -----------------------------------------------------------------------------

import ollama

# function for asking the AI
def askAI(question):
    # preText to give better respones 
    preText = "Give concise answers to following questions and add \n if line goes over 80 charters long"
    # Asking ollama and Specifying parameters
    stream = ollama.chat(
        model='phi3',
        messages=[{'role': 'user', 'content':preText+question}],
        stream=True,
    )
    # stream of AI output 
    return stream

# open input file and stores the text into file_content
with open('input.txt', 'r', encoding='utf-8', errors="ignore") as file:
    file_content = file.read()

# bose the questions to the AI 
stream = askAI(file_content)

# openes the file for the output and write to it 
text_file = open("Output.txt", "w", encoding="utf-8", errors="ignore")
# as the AI is generating the answer it wirte it to the text file 
for chunk in stream:
    text_file.write(chunk['message']['content'])
    text_file.flush()  # Ensure the content is written immediately
text_file.close()

