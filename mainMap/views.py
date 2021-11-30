from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from .models import Chunk, Lock, Marina, Weir
from django.http import JsonResponse
from django.db.models import Q
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def landing_view(request):
    return render(request, "landing.html")

def map_view(request):
    chunks = Chunk.objects.all()
    return render(request, "map.html", {"chunks":chunks})

def chunk_view(request, slug):
    chunk = Chunk.objects.filter(slug=slug)[0]
    chunks = Chunk.objects.all().order_by('-order_number')
    locks = Lock.objects.filter(chunk=chunk)
    marinas = Marina.objects.filter(chunk=chunk)
    weirs = Weir.objects.filter(chunk=chunk)
    try:
        next = Chunk.objects.filter(order_number=chunk.order_number+1)[0]
    except:
        next = []
    try:
        prev = Chunk.objects.filter(order_number=chunk.order_number-1)[0]
    except:
        prev = []
    try:
        print("next", next, "prev", prev)
    except:
        pass
    return render(request, "mapChunk.html", {"locks":locks, 'chunk':chunk, 'marinas':marinas, 'weirs': weirs, 'next':next, 'prev':prev})

def get_lock_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        locks = Lock.objects.filter(Q(name__icontains=q) | Q(contact__icontains=q) | Q(localization__icontains=q) | Q(distance__icontains=q) | Q(meta__icontains=q)).distinct()
        for lock in locks:
            queryset.append(lock)
    return list(queryset)

def get_marina_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        marinas = Marina.objects.filter(Q(name__icontains=q) | Q(contact__icontains=q) | Q(localization__icontains=q) | Q(distance__icontains=q) | Q(meta__icontains=q)).distinct()
        for marina in marinas:
            queryset.append(marina)
    return list(queryset)

def get_weir_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        weirs = Weir.objects.filter(Q(name__icontains=q) | Q(contact__icontains=q) | Q(localization__icontains=q) | Q(distance__icontains=q) | Q(meta__icontains=q)).distinct()
        for weir in weirs:
            queryset.append(weir)
    return list(queryset)

def search(request):
    print(request)
    if request.method == "POST":
        input = str(request.POST.get("input"))
        slug = str(request.POST.get("slug"))
        chunk = Chunk.objects.filter(slug=slug)
        try:
            next = chunk[0].nextChunk.all()[0]
        except:
            next = ""
        try:
            prev = chunk[0].prevChunk.all()[0]
        except:
            prev = ""
        ###przeszukiwanie bazy danych
        marinas = get_marina_queryset(input)
        locks = get_lock_queryset(input)
        weirs = get_weir_queryset(input)
        return render(request, "mapChunk.html", {'chunk':chunk[0], 'next':next, 'prev':prev, 'locks': locks, 'marinas': marinas, 'weirs':weirs})


def lock_details(request, slug):
    lock = Lock.objects.filter(slug=slug)[0]
    return JsonResponse({"name":lock.name, "dimensions":lock.dimensions, "contact":lock.contact, "distance":lock.distance, "localization":lock.localization, 'state':lock.state, 'img': lock.imageURL()})

def marina_details(request, slug):
    marina = Marina.objects.filter(slug=slug)[0]
    return JsonResponse({"name":marina.name, "dimensions":marina.dimensions, "contact":marina.contact, "distance":marina.distance, "localization":marina.localization, 'state':marina.state, 'img': marina.imageURL()})

def weir_details(request, slug):
    weir = Weir.objects.filter(slug=slug)[0]
    return JsonResponse({"name":weir.name, "dimensions":weir.dimensions, "contact":weir.contact, "distance":weir.distance, "localization":weir.localization, 'state':weir.state, 'img': weir.imageURL()})

def water_safety_view(request):
    return render(request, "water_safety.html")

def messages_view(request):
    url = "https://wroclaw.wody.gov.pl/komunikaty-nawigacyjne/114-nieprzypisany/1089-komunikaty-nawigacyjne"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find_all("div", {"class": "item-page"})
    raw_text = ""
    for item in article:
        raw_text = str(item.get_text())
    raw_text = raw_text.split("\n")
    raw_text = [x.rstrip() for x in raw_text if x != '']
    raw_text = [x.replace("\t","") for x in raw_text if x!='']
    raw_text = [x.replace("\xa0", "") for x in raw_text if x != '']
    #print(raw_text)
    formated_text = []
    tmp = []
    first = True
    for item in raw_text:
        if not first:
            if "KOMUNIKAT NAWIGACYJNY" not in item:
                tmp.append(item)
            else:
                formated_text.append(tmp)
                tmp=[]
                tmp.append(item)
        else:
            if "KOMUNIKAT NAWIGACYJNY" in item:
                tmp.append(item)
                first = False
    for i in range(len(formated_text)):
        del formated_text[i][-1]
    return render(request, "komunikaty.html", {"komunikaty":formated_text})

def locks_table_view(request):
    url = "https://wroclaw.wody.gov.pl/komunikaty-nawigacyjne/114-nieprzypisany/1090-sluzy-zeglugowe"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    td = soup.find_all("td")
    city, state, kilometer, nr_tel = [], [], [], []
    for result in td:
        c = result.find_all("strong")
        s = result.find_all("span")
        # print(result)
        if any(chr.isdigit() for chr in str(result.get_text())) and "+" in str(result.get_text()):
            kilometer.append(result.get_text()[1:-2])
        if c:
            city.append(c[-1].get_text())
        if s and ("otwarta" in str(s).lower() or "zamknięta" in str(s).lower()):
            state.append(s[0].get_text())
        if not re.search('[a-zA-Z]', result.get_text()) and "-" in result.get_text():
            nr_tel.append(result.get_text()[1:-2])
    city = city[5:] ###usuniecie z listy naglowkow
    locks = []
    for s,c,k,t in zip(state, city, kilometer, nr_tel):
        locks.append({'nazwa_stopnia_wodnego':c, 'km_odry':k, 'nr_tel': t, 'status_sluzy': s})

    for item in locks:
        print(item)
    return render(request, "locks.html", {"locks":locks})
