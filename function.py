from aiogram.types import Message
import requests

async def startCommandAnswer(message: Message):
    await message.answer("Assalomu Aleykum botimizga xush kelibsiz\n\n💬 Text yuboring...")

async def textAnswerAudio(message: Message):
    text = message.text
    print(text)
    url = "https://cloudlabs-text-to-speech.p.rapidapi.com/synthesize"

    payload = {
        "voice_code": "uz-UZ-1",
        "text": text,
        "speed": "1.00",
        "pitch": "1.00",
        "output_type": "audio_url"
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "34fe6d2e50msh7e10501cd13c417p19e723jsnc12607a15468",
        "X-RapidAPI-Host": "cloudlabs-text-to-speech.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)

    audio_url = response.json().get('result')['audio_url']

    await message.answer_audio(audio=audio_url, caption='Botimizdan foydalaganiz uchun rahmat 😉')
