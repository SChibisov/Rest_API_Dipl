from django.shortcuts import render, redirect
from .forms import UsersForm
from .models import Users


def users_empty(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                pass
    else:
        form = UsersForm()
    return render(request, 'index.html', {'form': form})


def users_view(request):
    users = Users.objects.all()
    return render(request, 'view.html', {'users': users})


def users_edit(request, id):
    users = Users.objects.get(id=id)
    return render(request, 'edit.html', {'users': users})


def users_update(request, id):
    users = Users.objects.get(id=id)
    form = UsersForm(request.POST, instance=users)
    if form.is_valid():
        form.save()
        return redirect('/view')
    return render(request, 'edit.html', {'users': users})


def users_delete(request, id):
    users = Users.objects.get(id=id)
    users.delete()
    return redirect('/view')
