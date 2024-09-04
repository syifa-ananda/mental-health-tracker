from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306173656',
        'name': 'Syifa',
        'class': 'KKI'
    }

    return render(request, "main.html", context)