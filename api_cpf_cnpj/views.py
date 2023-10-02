from django.shortcuts import render
import requests
import json

def index_api_cpf_cnpj(request):
    if request.method == 'GET':

        return render(request, 'api_cpf_cnpj.html')

    elif request.method == 'POST':

        post_data = request.POST

        response = requests.post('https://api-valida-cpf-cnpj.onrender.com/api/valida_cpf_cnpj', json=post_data)

        try:
            response_json = response.json()

        except json.JSONDecodeError as e:
            print(f'Erro ao decodificar JSON: {e}')
            response_json = None

        if response.status_code == 200 and response_json is not None:

            resultado = response_json.get('result')

            if resultado == True:

                resultado_descricao = 'Este documento está em um formato válido.'

                return render(request, 'api_cpf_cnpj.html', {'resultado_descricao': resultado_descricao})

        else:

            resultado_descricao = 'Este documento está em um formato inválido.'

            return render(request, 'api_cpf_cnpj.html', {'resultado_descricao': resultado_descricao})