from django.shortcuts import render
import requests
import json

def index_api_telefone_latam(request):
    if request.method == 'GET':

        return render(request, 'api_telefone_latam.html')

    elif request.method == 'POST':

        post_data = request.POST

        response = requests.post('https://api-valida-telefone-latam.onrender.com/api/valida_telefone_latam', json=post_data)

        try:
            response_json = response.json()

        except json.JSONDecodeError as e:
            print(f'Erro ao decodificar JSON: {e}')
            response_json = None

        if response.status_code == 200 and response_json is not None:

            regiao = response_json.get('regiao')
            valid = response_json.get('valid')

            context = {
                'regiao': regiao,
                'valid': valid
            }

            return render(request, 'api_telefone_latam.html', context=context)

        else:

            regiao = response_json.get('regiao')
            valid = response_json.get('valid')

            context = {
                'regiao': regiao,
                'valid': valid
            }

            return render(request, 'api_telefone_latam.html', context=context)