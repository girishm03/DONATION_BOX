from django.shortcuts import render, redirect
from Backend.models import CategoryDB, WebsiteDB, PersonDB
from Frontend.models import RegisterDB, contributionDB, itemsDB
from django.contrib import messages

# Create your views here.
def register_page(request):
    return render(request, "Registeration.html")
def registerdata(request):
    if request.method == "POST":
        una = request.POST.get('username')
        mob = request.POST.get('mobile')
        ema = request.POST.get('email')
        pwd = request.POST.get('password')
        obj = RegisterDB(UserName=una,Password=pwd , Email=ema, Mobile_Number=mob)
        obj.save()
        return redirect(register_page)
def UserLogin(request):
    if request.method=="POST":
        un = request.POST.get('User_Name')
        pwd = request.POST.get('Pass_Word')
        if RegisterDB.objects.filter(UserName=un,Password=pwd).exists():
            request.session['UserName']=un
            request.session['Password']=pwd
            return redirect(Homepage)
        else:
            return redirect(register_page)
    return redirect(register_page)
def User_logout(request):
    del request.session['UserName']
    del request.session['Password']

    return redirect(register_page)
def Homepage(request):
    web = WebsiteDB.objects.all()
    per = PersonDB.objects.all()
    return render(request, "Home.html",{'web':web,'per':per})
def about(request):
    per = PersonDB.objects.all()
    return render(request, "About.html",{'per':per})
def contact(request):
    data = RegisterDB.objects.all()
    return render(request, "Contact_us.html",{'data':data})
def Camp(request):
    return render(request, "Camp.html")
def donate(request):
    category = CategoryDB.objects.all()
    per = PersonDB.objects.all()
    con = contributionDB.objects.all()
    data2 = RegisterDB.objects.all()
    return render(request, "Donate.html",{'category':category,'per':per,'con':con,'data2':data2})
def contibdata(request):
    if request.method == "POST":
        cna = request.POST.get('dname')
        cmob = request.POST.get('dmobile')
        cema = request.POST.get('demail')
        camo = request.POST.get('damount')
        cocc = request.POST.get('doccupation')
        cat = request.POST.get('dcategory')
        cmsg = request.POST.get('dmessage')
        file = request.FILES['dfile']
        obj = contributionDB(CName=cna,CMobile=cmob,Cemail=cema,Camount=camo,Cmessage=cmsg,Ccategory=cat,Coccupation=cocc,Cfile=file)
        obj.save()
        return redirect(donate)
def itemdata(request):
    if request.method == "POST":
        ina = request.POST.get('Iname')
        imob = request.POST.get('Imobile')
        iema = request.POST.get('Iemail')
        iloc = request.POST.get('Ilocation')
        iitem = request.POST.get('Iitem')
        obj = itemsDB(IName=ina,IMobile=imob,Iemail=iema,Ilocation=iloc,Iitem=iitem)
        obj.save()
        messages.success(request, "Donation Made Successfully and will be collected as soon as possible...!")
        return redirect(donate)
def blog(request):
    return render(request, "Blog.html")
def gallery(request):
    return render(request, "Gallery.html")

def faq(r):
    return render(r, "FAQ.html")