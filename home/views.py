from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def contact(reques):
    return HttpResponse(
        """
            <div>
                <h2>Contact Page</h2>
                <p>Here is the conctac page</p>
            </div>
        """
    )

def saludo(reques):
    name = "Víctor"
    gretting = "Hola " + name +", como estas?"

    return HttpResponse(gretting)

def about(reques):
    return HttpResponse(
        """
            <div>
                <h2>Here is the about Page</h2>
            </div>
        """
    )