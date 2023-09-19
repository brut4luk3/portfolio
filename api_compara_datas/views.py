from django.shortcuts import render
import requests
from datetime import datetime
import json

def index_api_compara_datas(request):
    if request.method == 'GET':

        return render(request, 'api_compara_datas.html')

    elif request.method == 'POST':

        post_data = request.POST.copy()
        data1 = datetime.strptime(post_data['data1'], '%Y-%m-%d').strftime('%d/%m/%Y')
        data2 = datetime.strptime(post_data['data2'], '%Y-%m-%d').strftime('%d/%m/%Y')
        modo = post_data.get('modo')

        post_data['data1'] = data1
        post_data['data2'] = data2

        response = requests.post('http://brut4luk3.pythonanywhere.com/api/compara_datas', json=post_data)

        try:
            response_json = response.json()

        except json.JSONDecodeError as e:
            print(f'Erro ao decodificar JSON: {e}')
            response_json = None

        if response.status_code == 200 and response_json is not None:

            resultado = response_json.get('result')

            if modo == 'comparacao':
                if resultado == '1':
                    resultado_formatado = 'Data 1 é maior que Data 2'
                    return render(request, 'api_compara_datas.html', {'resultado_formatado': resultado_formatado})

                elif resultado == '-1':
                    resultado_formatado = 'Data 1 é menor que Data 2'
                    return render(request, 'api_compara_datas.html', {'resultado_formatado': resultado_formatado})

                elif resultado == '0':
                    resultado_formatado = 'Data 1 é igual a Data 2'
                    return render(request, 'api_compara_datas.html', {'resultado_formatado': resultado_formatado})

            else:
                resultado_formatado = resultado
                return render(request, 'api_compara_datas.html', {'resultado_formatado': resultado_formatado})

        else:
            resultado_formatado = 'Houve um erro na API!'
            return render(request, 'api_compara_datas.html', {'resultado_formatado': resultado_formatado})