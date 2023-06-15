#!/usr/bin/env python3
import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me a step by step on how to take any provided info and turn into a Doc for our team."}])
print(completion.choices[0].message.content)