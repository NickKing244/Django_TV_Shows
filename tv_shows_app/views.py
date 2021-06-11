from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

def index(request):
    context = {
        'all_the_shows': Show.objects.all()
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new_show.html')

def show(request, show_id):
    context = {
        'show': Show.objects.get(id=show_id)
    }
    return render(request, 'show_info.html', context)

def create(request):
    errors = Show.objects.Show_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/shows/new')
    else:
        Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
        new_show = Show.objects.last()
        new_show_id = new_show.id
        return redirect(f'/shows/{new_show_id}')

def destroy(request, show_id):
        to_delete = Show.objects.get(id=show_id)
        to_delete.delete()
        return redirect('/')

def edit(request, show_id):
    context = {
        'show': Show.objects.get(id=show_id)
    }
    return render(request, 'edit.html', context)

def update(request, show_id):
    errors = Show.objects.Show_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect(f'/shows/{show_id}/edit')
        else:
            update_show = Show.objects.get(id=show_id)
            update_show.title = request.POST['title']
            update_show.network = request.POST['network']
            update_show.release_date = request.POST['release_date']
            update_show.description = request.POST['description']
            update_show.save()
            return redirect(f'/shows/{show_id}')