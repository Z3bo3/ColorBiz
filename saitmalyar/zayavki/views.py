from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm



def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/zayavka_correct.html')
        else:
            error = 'Ошибка'
    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/zayavka.html', data)
