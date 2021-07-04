from django.http import JsonResponse
import pandas as pd
import os
from django.conf import settings

url_original_data = os.path.join(settings.STATIC_ROOT,'original_data.xlsx')
url_data_with_native_name = os.path.join(settings.STATIC_ROOT,'data_with_native_names.xlsx')

def orginal_table(request):

    df = pd.read_excel(url_original_data)
    
    return JsonResponse(data=df.to_dict('records'), safe=False)

def table_with_native_name(request):

    df = pd.read_excel(url_data_with_native_name)

    return JsonResponse(data=df.to_dict('records'), safe=False)