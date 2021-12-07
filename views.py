from django.shortcuts import render

# Create your views here.
def serve(request):
    serve1={'serv':'active'}
    return render(request, 'sarve/server.html',serve1)
