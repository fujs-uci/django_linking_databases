from django.shortcuts import render

# Create your views here.
def test1_home(request):
    user = request.user
    if user.is_authenticated and user.test_type() != 1:
        logout(request)
    if not user.is_authenticated:
        user = 'None'

    context = {'user': user, }
    template = 'test1/test1_home.html'
    return render(request, template, context)


def test1_signup(request):
    if request.method == "POST":
        signup_form = User1CreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            email = signup_form.cleaned_data.get('email')
            raw_password = signup_form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            User1.objects.get(email=email).set_test_type(1)
            return redirect('test1:test1_home')

    else:
        signup_form = User1CreationForm()

    context = {'signup_form': signup_form, }
    template = 'test1/signup.html'
    return render(request, template, context)
