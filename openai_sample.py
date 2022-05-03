import os
import openai

openai.api_key = ''

#prompt = input("Question:\n")

prompt = """

"""

response = openai.Completion.create(
    engine= 'text-davinci-002',
    prompt=prompt,
    temperature=.3,
    max_tokens=3000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print()
print("Answer:")
print(response['choices'][0]['text'].strip())
