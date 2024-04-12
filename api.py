import requests

url = "https://cloudlabs-text-to-speech.p.rapidapi.com/synthesize"

payload = {
    "voice_code": "en-US-1",
    "text": "hello, what is your name?",
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

print(audio_url)