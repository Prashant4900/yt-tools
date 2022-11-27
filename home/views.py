from django.shortcuts import render

from .forms import YouTubeForm

# Create your views here.
def index(request):
    context = {}
    if request.method == 'POST':
        form = YouTubeForm(request.POST)
        # print("POST", form)
        if form.is_valid():
            context['form'] = form
    else:
        form = YouTubeForm()
        # print("GET", form)
    context['form'] = form
    # print("context", context['form'])
    return render(request, 'base.html', context)
    # return render(request, 'base.html')