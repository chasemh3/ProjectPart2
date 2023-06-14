from django.shortcuts import render
from .models import Customer 

# Create your views here.
def indexPageView(request):
    childrenList = Customer.objects.all 
    return render(request, 'persons/index.html')

def kidsTable(request, last_name, first_name, age_at_missing, city, state, gender, race):
    context = {
        "last_name": last_name,
        "first_name": first_name,
        "age_at_missing" : age_at_missing,
        "city" : city,
        "state" : state,
        "gender" : gender, 
        "race" : race, 
     }


    return render (request,"persons/kidsTable.html", context)
