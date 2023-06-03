from django.shortcuts import render
from .models import *
def home(request):
    qidiruv = request.GET.get('searched')
    togri = Togri.objects.filter(togri=qidiruv)
    if len(togri) == 0:
        notogri = Notogri.objects.filter(notogri=qidiruv)
        if len(notogri) == 0:
            togri = 'Bunaqa soz yoq'
            notogri = ''
            content = {'t':togri, 'n': notogri}
        else:
            togri = notogri[0].t_soz
            notogri = Notogri.objects.filter(t_soz=togri)
            content = {'t':togri, 'n':notogri}
    else:
        notogri = Notogri.objects.filter(t_soz=togri[0])
        content= {
            't':togri[0],
            'n':notogri
        }
    return render(request,'result.html',content)



