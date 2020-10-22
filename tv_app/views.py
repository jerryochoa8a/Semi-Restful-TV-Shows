from django.shortcuts import render, HttpResponse, redirect
from tv_app.models import Show
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "shows":Show.objects.all(),
    }
    return render(request, "all_shows.html", context)

def add_show_page(request):# <----taking us to the "add show page"
    return render(request, 'add_new_show.html')

def add_show(request):# <---Adds a show
#####################################
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/shows/new')
    else:
####################################
        add_title = request.POST['title']
        add_network = request.POST['network']
        add_release = request.POST['release']
        add_desc = request.POST['desc']
        new_show = Show.objects.create(title=f"{add_title}", network=f"{add_network}", release=f"{add_release}", desc=f"{add_desc}")
        new_show_id = new_show.id
        return redirect(f'/shows/new/{new_show_id}')

def tv_show_page(request, new_show_id):
    context={
        "show": Show.objects.get(id=new_show_id)
    }
    return render(request, 'tv_show.html', context)

def edit_show(request, show_id):
    context = {
        "show": Show.objects.get(id=show_id)
    }
    return render(request,'edit_show.html', context)

def edit_done(request, show_id):
    context={
        "show":Show.objects.get(id=show_id)
    }
    new_title = request.POST['title_edit']
    new_network = request.POST['network']
    new_release = request.POST['release']
    new_desc = request.POST['desc']
    
    this_show = Show.objects.get(id=show_id)
    this_show.title = f"{new_title}"
    this_show.network = f"{new_network}"
    this_show.release = f"{new_release}"
    this_show.desc = f"{new_desc}"
    this_show.save()
    return render(request, 'tv_show.html', context)

def delete(request, show_id):
    this_show = Show.objects.get(id=show_id)
    this_show.delete()
    return redirect('/')