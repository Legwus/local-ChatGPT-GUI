import openai
import time

def loadToken():
    text_file = open("token.txt", "r")
    data = text_file.read()
    return data

openai.api_key = loadToken()

model_engine = "text-davinci-003"
time.sleep(3)

while True:
        prompt = input()
        if prompt == "":
            break
        else:
            completion = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=2048, n=1, stop=None, temperature=0.75)
            message = completion.choices[0].text
            print(message)