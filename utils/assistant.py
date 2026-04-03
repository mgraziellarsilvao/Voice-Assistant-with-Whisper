from datetime import datetime
import random

def responder(texto):
    texto = texto.lower()

    if "horas" in texto:
        return f"Agora são {datetime.now().strftime('%H:%M')}"

    if "seu nome" in texto:
        return "Sou um assistente de voz offline."

    if "power bi" in texto:
        return "Power BI é uma ferramenta de análise de dados da Microsoft."

    if "terra" in texto:
        return "A Terra é o terceiro planeta do sistema solar e o único conhecido por abrigar vida."

    if "oi" in texto or "olá" in texto:
        return "Olá! Como posso te ajudar?"

    respostas_padrao = [
        "Boa pergunta! Ainda estou aprendendo.",
        "Interessante, ainda não sei responder isso.",
        "Posso melhorar com mais comandos no futuro."
    ]

    return random.choice(respostas_padrao)
