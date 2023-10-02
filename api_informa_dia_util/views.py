from django.shortcuts import render
from datetime import datetime
import requests
import json

def index_api_informa_dia_util(request):

    lista_estado = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PE', 'PI',
                    'RJ', 'RN', 'RS', 'RO', 'SC', 'SP', 'SE', 'TO', 'all']

    if request.method == 'GET':

        context = {
            'lista_estado': lista_estado
        }

        return render(request, 'api_informa_dia_util.html', context=context)

    elif request.method == 'POST':

        post_data = request.POST.copy()
        data_atual = datetime.strptime(post_data['data_atual'], '%Y-%m-%d').strftime('%d/%m/%Y')

        post_data['data_atual'] = data_atual

        response = requests.post('https://brut4luk3.onrender.com/api/informa_dia_util', json=post_data)

        try:
            response_json = response.json()

        except json.JSONDecodeError as e:
            print(f'Erro ao decodificar JSON: {e}')
            response_json = None

        if response.status_code == 200 and response_json is not None:

            resultado = response_json.get('result')

            context = {
                'resultado': resultado,
                'lista_estado': lista_estado
            }

            return render(request, 'api_informa_dia_util.html', context=context)

        else:

            resultado = 'Houve um erro na API!'

            context = {
                'resultado': resultado,
                'lista_estado': lista_estado
            }

            return render(request, 'api_informa_dia_util.html', context=context)