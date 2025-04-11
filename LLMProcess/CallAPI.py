import os
from openai import OpenAI


client = OpenAI(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    api_key="e64a11e7-e9a2-4085-ba78-3db0ced3ce96",
)

# # Non-streaming:
# print("----- standard request -----")
# completion = client.chat.completions.create(
#     model="doubao-1-5-lite-32k-250115",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant Read the following Legal codes and descriptions of the citations (e.g., disorderly conduct, public drunkenness) use one or few words to describe the citation. Only return the words, no other text."},
#         {"role": "user",
#          "content": "5503(a)(2) DISORDERLY CONDUCT - UNREASONABLE NOISE"},
#     ],
# )
# print(completion.choices[0].message.content)

def summarize_citation(citation, neighborhood):
    completion = client.chat.completions.create(
        model="doubao-1-5-lite-32k-250115",
        messages=[
            {"role": "system", "content": "You are a helpful assistant Read the following Legal codes and descriptions of the citations (e.g., disorderly conduct, public drunkenness) use one or few words to describe the citation. Only return the words, no other text."},
            {"role": "user",
             "content": citation},
        ],
    )
    return completion.choices[0].message.content , neighborhood


