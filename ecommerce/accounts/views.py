import re
from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, RegistrationForm
from .models import EmailConfirmed, UserDefaultAddress
from django.contrib import messages
from django.urls import reverse
from accounts.forms import UserAddressForm
# Create your views here.



def logout_view(request):
    logout(request)
    messages.success(request, "succesfully logged out!")
    return HttpResponseRedirect('%s' % (reverse("auth_login")))


def login_view(request):
    form = LoginForm(request.POST or None)
    btn = "Login"
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request, "succesfully logged in!")
        return HttpResponseRedirect("/")
        # user.emailconfirmed.activate_user_email()

    context = {'form': form, "btn": btn}
    return render(request, 'form.html', context)


def registration_view(request):
    form = RegistrationForm(request.POST or None)
    btn = "Join"
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.save()
        messages.success(request, "succesfully registered!")
        return HttpResponseRedirect("/")
        # username = form.cleaned_data['username']
        # password = form.cleaned_data['password']
        # user = authenticate(username=username, password=password)
        # login(request, user)

    context = {'form': form, "btn": btn}
    return render(request, 'form.html', context)


SHA1_RE = re.compile('^[a-f0-9]{40}$')


def activation_view(request, activation_key):
    if SHA1_RE.search(activation_key):
        print("Activation key is real")
        try:
            instance = EmailConfirmed.objects.get(activation_key=activation_key)
        except EmailConfirmed.DoesNotExist:
            instance = None
            messages.success(request, "There was an error with your request")

        if instance is not None and not instance.confirmed:
            page_message = "Confirmation sucessful"
            instance.confirmed = True
            instance.activation_key = "CONFIRMED"
            instance.save()
        elif instance is not None and instance.confirmed:
            page_message = "Already confirmed"
        else:
            page_message = ""

        context = {"page_message": page_message}
        return render(request, "accounts/activation_complete.html", context)
    else:
        raise Http404


def add_user_address(request):
    print(request.GET)
    try:
        next_page = request.GET.get("next")
    except:
        next_page = None
    form = UserAddressForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_address = form.save(commit=False)
            new_address.user = request.user
            new_address.save()
            is_default = form.cleaned_data["default"]
            if is_default:
                default_address, created = UserDefaultAddress.objects.get_or_create(user=request.user)
                default_address.shipping = new_address
                default_address.save()
            if next_page is not None:
                return HttpResponseRedirect(reverse(str(next_page))+"?address_added=true")

    btn = "Save Address"
    form_title = "Add New Address"
    return render(request, "form.html", {"form": form, "btn": btn, "form_title": form_title})
