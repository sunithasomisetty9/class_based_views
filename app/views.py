from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from app.forms import *
# Create your views here.
def fbv_string(request):
    return HttpResponse("<h1>This is function based view for returning string as a response</h1>")


def fbv_render(request):
    return render(request,'fbv_render.html')


class CbvString(View):
    def get(self,request):
        return HttpResponse("<h1>This is class based view returning string as a response</h1>")


class CbvRender(View):
    def get(self,request):
        return render(request,'CbvRender.html')

class CbvTemp(TemplateView):
    template_name='CbvRender.html'


def fbv_form(request):
    MFO=MovieForm()
    d={'MFO':MFO}
    if request.method=='POST':
        MFD=MovieForm(request.POST)
        if MFD.is_valid():
            MFD.save()
            return HttpResponse('Data inserted succesfully')

    return render(request,'fbv_form.html',d)



class CbvForm(View):
    def get(self,request):
        MFO=MovieForm()
        d={'MFO':MFO}
        return render(request,'cbv_form.html',d)

    def post(self,request):
        MFD=MovieForm(request.POST)
        if MFD.is_valid():
            MFD.save()
            return HttpResponse('Data inserted')