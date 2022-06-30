from django.shortcuts import render


# Create your views here.
def setsession(request):

    # setting session name to sumit
    # this is a dummy session
    request.session['name'] = 'sumit'

    # setting epiry time as x seconds

    x_seconds=60
    request.session.set_expiry(x_seconds)
    return render(request, "student/setsession.html")


def getsession(request):
    name = request.session['name']
    return render(request, 'student/getsession.html', {'name': name})


def delsession(request):

    # first checking key in session db
    if 'name' in request.session:
        del request.session['name']

    return render(request, 'student/delsession.html')

