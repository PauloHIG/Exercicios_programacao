print('Não seja apegado ao código, faça qualquer coisa e apague')
bola = False
print(not bola)

headers = {'Authorization': f'Bearer {API_KEY}', 'content-type':'Application/json'}
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo-0301"
body_message = {
    'model': id_modelo,
    'messages': [{'role':'user',
                 'content':'explique como funciona a API do ChatGPT'}]
}
body_message = json.dumps(body_message)
requisicao = requests.post(link, headers=headers, data=body_message)
print(requisicao)
print(requisicao.text)
resposta_completa = requisicao.json()
resposta_refinada = resposta_completa['choices'][0]['message']['content']
print(resposta_refinada)