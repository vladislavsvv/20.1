from django.shortcuts import render


def home_page(request):
    return render(request, 'main/home_page.html')


def contact_info(request):
    return render(request, 'main/contact_info.html')
