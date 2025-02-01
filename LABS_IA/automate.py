from mp4_to_mp3 import mp4_to_mp3
from mp3_to_text import mp3_to_text
from chat_openai import conversa_com_openai

import assemblyai as aai
from openai import OpenAI

import uuid


if __name__ == "__main__":

	mp4_filename = "IMPACTA\LABS_IA\files\file.mp4"
	mp3_filename = uuid.uuid4().hex + ".mp3"

	print('Convertendo de MP4 para MP3')
	mp4_to_mp3(mp4_filename, mp3_filename)

	print('Convertendo de MP3 para texto')
	transcript = mp3_to_text(mp3_filename)

	transcricao = ''

	if transcript.status == aai.TranscriptStatus.error:
	    print(transcript.error)
	else:
	    for sentenca in transcript.utterances:
	        transcricao = transcricao + f"{sentenca.speaker}: {sentenca.text}"
	        transcricao = transcricao + '\n'


	print('Geração da ata de reunião')
	openai_client = OpenAI(api_key = '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')

	system_prompt = "Você é um ótimo gerente de projetos com grandes capacidades de criação de atas de reunião."

	user_prompt = """Em uma redação de nível especializado, resuma as notas da reunião em um único parágrafo.
	Em seguida, escreva uma lista de cada um de seus pontos-chaves tratados na reunião.
	Por fim, liste as próximas etapas ou itens de ação sugeridos pelos palestrantes, se houver."""

	prompt_final = user_prompt + ' Transcrição da reunião::: ' + transcricao

	resposta = conversa_com_openai(openai_client, system_prompt, prompt_final)
	print(resposta)