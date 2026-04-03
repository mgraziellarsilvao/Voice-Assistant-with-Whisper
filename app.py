import whisper
import pyttsx3

from utils.audio import gravar_audio
from utils.assistant import responder

# 🔊 Inicializa voz
engine = pyttsx3.init()

def falar(texto):
    engine.say(texto)
    engine.runAndWait()

# 🧠 Carrega modelo
model = whisper.load_model("base")

print("🤖 Assistente iniciado! Diga 'sair' para encerrar.\n")

while True:
    arquivo = gravar_audio(5)

    result = model.transcribe(arquivo)
    texto = result["text"]

    print(f"🧑 Você: {texto}")

    if "sair" in texto.lower():
        print("👋 Encerrando...")
        break

    resposta = responder(texto)

    print(f"🤖 Assistente: {resposta}")
    falar(resposta)
