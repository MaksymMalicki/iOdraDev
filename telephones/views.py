from django.shortcuts import render
from .models import TelephoneBlock, TelephoneUnit

def contact_view(request):
    blocks = TelephoneBlock.objects.all()
    info = []
    for block in blocks:
        info.append(TelephoneUnit.objects.filter(telephoneUnit=block))
    return render(request, "contact.html", {"data": zip(blocks, info)})
