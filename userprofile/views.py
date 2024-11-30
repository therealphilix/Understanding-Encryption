from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile

def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {'form': form})

def view_profile(request):
    profile = Profile.objects.last()
    if profile:
        decrypted_data = profile.get_decrypted_data()
    else:
        decrypted_data = None
    return render(request, 'view_profile.html', {'profile': decrypted_data})