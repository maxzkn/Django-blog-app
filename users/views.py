from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':  # if we get a POST request
        # form = UserCreationForm(request.POST)  # create a form with that POST data (username and two passwords) (bound form to POST data)
        form = UserRegisterForm(request.POST)
        if form.is_valid():  # POST data could be anything, so we need to validate it so that we know that we're getting
            # the fields and data that we expect
            # is valid: Django does backend checks with our UserCreationForm, which handles that for us, and it can say
            # for e.g. no it's not valid bc this username already exists, the two passwords don't match, etc...
            # actually save the user
            form.save()  # and that will automatically hash the psw and do everything else
            username = form.cleaned_data.get('username')  # the validated data will be in form.cleaned_data dictionary,
            # and this will be nicely converted to Python data types for us from the form
            # Now we want to show flash message to show that we've received valid data
            # messages.success(request, f'Account created for {username}!')
            messages.success(request, f'Account created for {username}! You are now able to log in.')
            # return redirect('blog-home')  # redirect user to home page after submitting data
            return redirect('login')  # redirect user to login page after submitting data
    else:  # anything that is not a POST request we will just create a blank form
        # form = UserCreationForm()
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error


@login_required
def profile(request):
    if request.method == "POST":
        # Also pass in post data (request.POST):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # we also have additional file data request when user tries to upload an image (request.FILES)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account has been updated!')
            return redirect('profile')  # us redirecting here causes the browser to send GET request and then we don't
            # get that message when reloading the page that are you sure bc the form will be resubmitted (another POST)
    else:
        # populate these regular forms with user info that is currently logged in
        # remember: these are model forms that are expecting to be working on a specific model object, so
        # so we can populate the fields of the form just by passing in an instance of the object that it expects.
        u_form = UserUpdateForm(instance=request.user)  # user update form will have username and email filled in
        p_form = ProfileUpdateForm(instance=request.user.profile)  # profile form will have image filled in

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

