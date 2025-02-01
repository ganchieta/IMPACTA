from openai import OpenAI

def conversa_com_openai(openai_client, system_prompt, user_prompt):

    resposta = openai_client.chat.completions.create(
        model = "gpt-4o-mini", #modelo que estamos usando
        messages =[
            {'role': 'system', 'content': system_prompt}, #como eu quero que ele se comporte (a perspectiva)
            {'role': 'user', 'content': user_prompt}

        ],
        temperature = 0.7 # parametro para criatividade 0.1 sem criativiade 0.9 muito criativo na resposta
    )
    print(resposta.choices[0].message.content)

if __name__ == "__main__":
    openai_client =OpenAI(api_key='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') 
    system_prompt ="Você é um cientista muito famoso sua especialidade é o campo da fisica"
    user_prompt ="me explique sobre a teoria da relatividade"

    resposta = conversa_com_openai(openai_client,system_prompt,user_prompt)
    print(resposta)


# #CÓDIGO COM A API TOKEN DO PROFESSOR PAGA

# from openai import OpenAI

# def conversa_com_openai(openai_client, system_prompt, user_prompt):


# 	resposta = openai_client.chat.completions.create(
# 		model = "gpt-4o-2024-08-06",
# 		messages = [
# 			{'role': 'system', 'content': system_prompt},#como eu quero que ele se comporte (a perspectiva)
# 			{'role': 'user', 'content': user_prompt}
# 		],
# 		temperature=0.7 # parametro para criatividade 0.1 sem criativiade 0.9 muito criativo na resposta
# 		)

# 	print(resposta.choices[0].message.content)
# if __name__ == "__main__":

# 	openai_client = OpenAI(api_key = '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')
# 	system_prompt = "Você é um cientista muito famoso como por exemplo Einstein."
# 	user_prompt = "Me explique a teoria da relatividade."

# 	resposta = conversa_com_openai(openai_client, system_prompt, user_prompt)
# 	print(resposta)