from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def registration(request):
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    email = request.POST['email']
    password = request.POST['password']
    request.session['userId'] = user.id
    return redirect('/dashboard')

def login(request):
    pass

def dashboard(request):
    if 'userId' not in request.session:
        return redirect('/')
    else:
        context = {
            'user': User.objects.get(id=request.session['userId'])
        }
        return redirect(request, 'dashboard.html', context)

