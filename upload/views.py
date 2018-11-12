from django.views import generic
from .models import Author,Saying
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from .forms import UserForm,LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin

class home(generic.ListView):
    template_name = 'upload/home.html'

    def get_queryset(self):
        return Author.objects.all()

class detail(generic.DetailView):
    model = Author
    template_name = 'upload/detail.html'

class AuthorCreate(LoginRequiredMixin,CreateView):
    login_url = "upload:login"
    model = Author
    fields = ['author','author_logo']

class AuthorUpdate(LoginRequiredMixin,UpdateView):
    login_url = "upload:login"
    model = Author
    fields = ['author','author_logo']

class AuthorDelete(LoginRequiredMixin,DeleteView):
    login_url = "upload:login"
    model = Author
    success_url = reverse_lazy('upload:home')

class SayingCreate(LoginRequiredMixin,CreateView):
    login_url = "upload:login"
    model = Saying
    fields = ['speaker','category','content']
class SayingUpdate(LoginRequiredMixin,UpdateView):
    login_url = "upload:login"
    model = Saying
    fields = ['category','content']


class UserFormView(View):
    form_class= UserForm
    template_name = 'upload/registration_form.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form= self.form_class(request.POST)

        if form.is_valid():
            user = form.save()

            username=form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)

            user.save()


            user = authenticate(username=username,password=password)

            if user is not None:



                if user.is_active:
                    login(request, user)
                    return redirect('upload:home')

        return render(request, self.template_name, {'form': form})


class LoginUser(View):
    template_name='upload/login_form.html'
    form_class= LoginForm

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None and user.is_active:
            login(request,user)
            return redirect('upload:home')

        return render(request, self.template_name, {'form': form})


def logoutuser(request):
        logout(request)

        return redirect('upload:login')



















