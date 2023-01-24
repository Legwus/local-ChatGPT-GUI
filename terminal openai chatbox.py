import openai
import time

openai.api_key = "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"

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