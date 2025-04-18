import requests
from django.shortcuts import render

def fetch_data(request):
    api_url = "https://deckmount.in/api/web/indresh.php"
    try:
        response = requests.get(api_url)
        data = response.json() if response.status_code == 200 else {}
    except Exception as e:
        data = {"error": str(e)}

    return render(request, 'main.html', {'api_data': data})
