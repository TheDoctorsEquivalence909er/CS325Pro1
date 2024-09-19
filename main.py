import ollama

def askAI(question):
    preText = "Give concise answers to following questions and add \n if line goes over 80 charters long"
    stream = ollama.chat(
        model='phi3',
        messages=[{'role': 'user', 'content':preText+question}],
        stream=True,
    )

    return stream

with open('input.txt', 'r', encoding='utf-8', errors="ignore") as file:
    file_content = file.read()

print(file_content)
stream = askAI(file_content)

text_file = open("Output.txt", "w", encoding="utf-8", errors="ignore")
for chunk in stream:
    text_file.write(chunk['message']['content'])
    text_file.flush()  # Ensure the content is written immediately
text_file.close()

