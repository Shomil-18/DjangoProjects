from django.shortcuts import render, HttpResponse
from .models import Member
form .forms import MemberForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')   # PRG Pattern
    else:
        form = MemberForm()

    all_members = Member.objects.all()

    return render(request, 'home.html', {'form': form,'all': all_members})


def about(request):
    return HttpResponse("This is about page")
