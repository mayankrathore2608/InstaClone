from django.shortcuts import render
from UserInfo.models import UserCred




# Create your views here.
def index(request):
    return render(request, 'index.html')


def submit(request):
    user_name = request.POST['user']
    pass_word = request.POST['password']
    na_me = request.POST['name']
    ema_il = request.POST['email']
    print(user_name)
    data = UserCred(username=user_name, password=pass_word, name=na_me, email=ema_il)
    data.save()
    return render(request, 'home.html')
    #
    # db_data = user.objects.filter(username=user_name)
    # if db_data:
    #     return HttpResponse("<h1>Already hhhhhh present</h1>")
    # else:
    #     user_data.save()
    #     return render(request, 'home.html')


