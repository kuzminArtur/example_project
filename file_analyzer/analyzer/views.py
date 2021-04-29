# from django.shortcuts import render
#
#
# def index(request):
#     return render(
#         request,
#         'index.html',
#     )
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
import time


def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            result = handle_uploaded_file(request.FILES['file'])
            return render(request, 'result.html', {
                'file': request.FILES['file'],
                'result': result
            })
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form})


def handle_uploaded_file(f):
    analyze_result = f"Дофига умный отчет по файлу {f.name}"
    time.sleep(2)
    return analyze_result
