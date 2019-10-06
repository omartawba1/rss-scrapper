from django.shortcuts import render


def homepage(request):
    """
    Render the homepage
    :param request:
    :return:
    """
    return render(request, 'homepage/index.html')
