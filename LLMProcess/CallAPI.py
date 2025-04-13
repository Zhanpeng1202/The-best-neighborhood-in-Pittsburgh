import os
from openai import OpenAI


# client = OpenAI(
#     base_url="https://ark.cn-beijing.volces.com/api/v3",
#     api_key="e64a11e7-e9a2-4085-ba78-3db0ced3ce96",
# )


client = OpenAI(
    base_url="https://api.perplexity.ai",
    api_key="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",
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

def judge_hood_crime(hood_name, crime_records):
    message = [
        {"role": "system", "content": "You are a judge, you would be given large text of the crimes records happening in this neighborhood, read them all and summarize them, try to find three keywords for the crime happening in this neighborhood"}
    ]
    
    # we would have concat crime_records into one string
    message.append({"role": "user", "content": crime_records})

    completion = client.chat.completions.create(
        model="doubao-1-5-lite-32k-250115",
        messages=message,
    )
    return completion.choices[0].message.content, hood_name


def judge_hood_all(records):
    
    system_message = """
    You are a judge, you would help us find the best neighborhood in Pittsburgh, PA.
    You would be given, for each neighborhood, the score for the crime frequency,
    the score for facility, the score for steps in the neighborhood, the score for the park numbers and the score for the tree cover, and the score 
    for the students in the neighborhood. And finally, the detailed non-traffical crime records in the neighborhood.
    
    you would be given 5 top ranked neighborhoods, based on the scores above and your knowledge of the city, decide which one is the best. Do not fully rely
    on the scores, but also consider the crime records and your knowledge of the Pittsburgh city
    """
    message = [
        {"role": "system", "content": system_message}
    ]
    
    # for record in records:
    #     message.append({"role": "user", "content": record})
    
    # convert records to one string
    records_str = ""
    for record in records:
        records_str += record
    
    message.append({"role": "user", "content": records_str})
    
    completion = client.chat.completions.create(
        # model="doubao-1-5-lite-32k-250115",
        model="sonar-deep-research",
        messages=message,
    )
    
    
    return completion.choices[0].message.content

