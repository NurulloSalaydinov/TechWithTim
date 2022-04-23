from .models import Settings

def view_all(request):
    context = {
        "setting":Settings.objects.first(),
    }
    return context