from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from apps.users.forms import userForm, profileForm
from apps.users.models import Profile

# Create your views here.

class userCreate(CreateView):
    model=User
    template_name="usersForm.html"
    form_class=userForm
   # second_form_class = profileForm
    success_url=reverse_lazy('users:usersList')

class userDelete(ListView):
    model = User
    template_name = "usersDelete.html"
    success_url = reverse_lazy('users:usersList')

class userEdit(UpdateView):
    model = User
    template_name = "usersForm.html"
    form_class = userForm
    success_url = reverse_lazy('users:usersList')

class userList(ListView):
    model=User
    template_name="UsersList.html"

def user_create(request):
    if request.method == 'POST':
        form = userForm(request.POST, request.FILES)
        form2 = profileForm(request.POST, request.FILES)
        if form.is_valid() and form2.is_valid():
            #form.groups.add(form.cleaned_data['group'])
            user = form.save()
            # in case you need to assign a new group without admin permision
            #user.groups.add(form.cleaned_data['group'])
            profile = form2.save(commit=False)
            #form2.save()
            profile.user_id = user.id
            profile.save()
            return redirect('users:user_list')
    else:
        form = userForm()
        form2 = profileForm()
    return render(request, 'usersForm.html', {'form': form, 'form2': form2})

def user_list(request):
    userList = User.objects.all().order_by('id')
    contexto = {'object_list': userList}
    return render(request, 'users_list.html', contexto)
    #return render(request, 'appointment_list.html', {'appointments', 'test'})
    #return render_to_response("appointment_list.html", {'appointments', applist}, RequestContext(request))

def user_edit(request, pk):
    user = User.objects.get(id=pk)
    profile = Profile.objects.get(user=user)
    if request.method == 'GET':
        form=userForm(instance=user)
        form2=profileForm(instance=user.profile)
    else:
        form = userForm(request.POST, instance=user)
        form2 = profileForm(request.POST, instance=user.profile)
        if form.is_valid() and form2.is_valid():
            user = form.save()
            user.groups.clear()
            user.groups.add(form.cleaned_data['group'])
            form2.save()
        return redirect('users:user_list')
    return render(request, 'users_form.html', {'form': form, 'form2': form2})

def user_delete(request, pk):
    user=User.objects.get(id=pk)
    if request.method=='POST':
        user.delete()
        return redirect('users:user_list')
    return render(request, 'users_delete.html', {'user': user})