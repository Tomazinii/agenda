from app.models import Agenda
from django.shortcuts import redirect, render

from .forms import AgendaForm
from .models import Agenda



def add_agenda(request):
    date = ""
    qs = Agenda.objects.all()
    submitted = False
    if request.method =="POST":
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            AgendaForm
            return redirect("app:add_agenda")

    else:
        form = AgendaForm
        if 'submitted' in request.GET:
            submitted = True
    


    form = AgendaForm
    return render(request, 'index.html', {'form': form, 'submitted': submitted, 'qs': qs})
    

def list_agenda(request, list_id):
    lista = Agenda.objects.get(pk=list_id)
    return render(request, 'list.html', {'lista':lista})

    
def delete_agenda(request, list_id):
    item = Agenda.objects.get(pk=list_id)
    item.delete()
    return redirect("app:add_agenda")


def calendar(request):
    return render(request, "calendar.html")



