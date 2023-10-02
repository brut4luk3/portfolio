from django.shortcuts import render
import requests
import json

def index_api_replace_text(request):
    if request.method == 'GET':

        return render(request, 'api_replace_text.html')

    elif request.method == 'POST':

        post_data = request.POST.copy()
        CasoParcialQuantidade = post_data.get('CasoParcialQuantidade')

        if CasoParcialQuantidade != '0':

            CasoParcialQuantidade_convertida = int(CasoParcialQuantidade)
            post_data['CasoParcialQuantidade'] = CasoParcialQuantidade_convertida

        response = requests.post('https://api-replace-text.onrender.com/api/replace_text', json=post_data)

        try:
            response_json = response.json()

        except json.JSONDecodeError as e:
            print(f'Erro ao decodificar JSON: {e}')
            response_json = None

        if response.status_code == 200 and response_json is not None:

            resultado = response_json.get('result')

            return render(request, 'api_replace_text.html', {'resultado': resultado})

        else:

            resultado = 'Houve um erro na API!'

            return render(request, 'api_replace_text.html', {'resultado': resultado})