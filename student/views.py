from django.shortcuts import render
from .forms import Postcomplain
def complain(request):
    if request.method == "POST":
        form = Postcomplain(request.POST)
    else:
        form = Postcomplain()
    return render(request, 'complainpage.html', {'form': form})