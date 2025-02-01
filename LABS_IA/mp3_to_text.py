import assemblyai as aai

# Replace with your API key
aai.settings.api_key = "199a9b26a6a64b9f87c797cd69964e1b"

# URL of the file to transcribe
FILE_URL = r"IMPACTA\LABS_IA\files\6e9756e29e8948a89cf12a96cf375973.mp3"

transcriber = aai.Transcriber()

configuracoes = aai.TranscriptionConfig(
    speaker_labels= True,
    speakers_expected= 2,
    language_code= 'pt'

)

transcript = transcriber.transcribe(FILE_URL, config=configuracoes)

if transcript.status == aai.TranscriptStatus.error:
    print(transcript.error)
else:
    for utt in transcript.utterances:
        print(f"{utt.speaker}: {utt.text}")
        print('\n')
