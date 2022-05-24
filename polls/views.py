from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def victor(reques):
    return HttpResponse(
        """
            <nav>
                <h1>Polls APP</h1>
                <h3>Víctor Manuel Tamayo Briones</h3>
            </nav>
        """
    )