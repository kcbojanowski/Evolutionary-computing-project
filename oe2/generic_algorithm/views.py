from django.shortcuts import render
from .forms import MyForm

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process the form data
            pass  # Placeholder for form data processing
    else:
        form = MyForm()
    return render(request, 'generic.html', {'form': form})