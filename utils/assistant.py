from datetime import datetime

def responder(texto):
    texto = texto.lower()

    if "horas" in texto:
        return f"Agora são {datetime.now().strftime('%H:%M')}"

    if "seu nome" in texto:
        return "Sou seu assistente de voz offline."

    if "power bi" in texto:
        return "Power BI é uma ferramenta de análise de dados da Microsoft."

    return "Desculpe, ainda estou aprendendo."
