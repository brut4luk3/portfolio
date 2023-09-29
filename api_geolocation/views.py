from django.shortcuts import render
import requests
import json

def index_api_geolocation(request):
    if request.method == 'GET':

        return render(request, 'api_geolocation.html')

    elif request.method == 'POST':

        post_data = request.POST

        response = requests.post('https://api-geolocation.onrender.com/api/geolocation', json=post_data)

        try:
            response_json = response.json()

        except json.JSONDecodeError as e:
            print(f'Erro ao decodificar JSON: {e}')
            response_json = None

        if response.status_code == 200 and response_json is not None:

            cidade = response_json.get('cidade')
            estado = response_json.get('estado')
            pais = response_json.get('pais')

            context = {
                'cidade': cidade,
                'estado': estado,
                'pais': pais
            }

            return render(request, 'api_geolocation.html', context=context)

        else:

            cidade = 'null'
            estado = 'null'
            pais = 'null'

            context = {
                'cidade': cidade,
                'estado': estado,
                'pais': pais
            }

            return render(request, 'api_geolocation.html', context=context)