from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Andhika Reihan Hervito',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)