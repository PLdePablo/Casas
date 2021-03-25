from django.shortcuts import render

# Create your views here.
# from pisos.models import Pisos, Inquilinos

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    # num_pisos = Piso.objects.all().count()
    # num_inquilinos = Inquilino.objects.all().count()

    context = {
        # 'num_pisos': num_pisos,
        # 'num_inquilinos': num_inquilinos,
        'num_pisos': 11,
        'num_inquilinos': 9,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
