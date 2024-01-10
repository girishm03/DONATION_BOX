from django.shortcuts import render, redirect
from Backend.models import CategoryDB, WebsiteDB, PersonDB
from Frontend.models import RegisterDB, itemsDB, contributionDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def admin_login(r):
    return render(r,"AdminLogin.html")
def adminlogin(request):
    if request.method=="POST":
        un=request.POST.get('user_name')
        pwd=request.POST.get('pass_word')

        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                return redirect('INDEX')
            else:
                messages.success(request, "Admin login unsuccessfully...!")
                return redirect('admin_login')
        else:
            messages.success(request, "Admin login unsuccessfully...!")
            return redirect('admin_login')
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Admin Logout successfully...!")
    return redirect(admin_login)

def INDEX(r):
    data = RegisterDB.objects.all()
    messages.success(r, "Admin login successfully...!")
    return render(r,"index.html", {'data': data})
def Users(r):
    data = RegisterDB.objects.all()
    return render(r,"Registered_users.html", {'data': data})

def items(r):
    da = itemsDB.objects.all()
    return render(r, "ItemOrders.html", {'da': da})

def contribution(r):
    do = contributionDB.objects.all()
    return render(r, "Donations.html", {'do': do})


def Category(r):
    return render(r,"DonorCategory.html")
def cdata(request):
    if request.method == "POST":
        na = request.POST.get('Cname')
        dec = request.POST.get('description')
        img = request.FILES['Cimage']
        obj = CategoryDB(C_name=na, Desciption=dec, C_image=img)
        obj.save()
        messages.success(request, "Category added successfully...!")
        return redirect(Category)
def displaycat(request):
    data = CategoryDB.objects.all()
    return render(request, "DisplayCategory.html", {'data': data})
def Editcat(request, dataid):
    cdata = CategoryDB.objects.get(id=dataid)
    return render(request,"EditCategory.html",{'cdata':cdata})
def updatecategory(request, dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        dec = request.POST.get('description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=dataid).C_image
        CategoryDB.objects.filter(id=dataid).update(C_name=na, Desciption=dec, C_image=file)
        messages.info(request, "Category updated successfully...!")
        return redirect(displaycat)
def deletecategory(request, dataid):
    donation = CategoryDB.objects.filter(id=dataid)
    donation.delete()
    messages.error(request, "Category deleted successfully...!")
    return redirect(displaycat)
def weblink(r):
    return render(r,"Other_Site.html")
def wdata(request):
    if request.method == "POST":
        wna = request.POST.get('wname')
        wab = request.POST.get('webabout')
        wimg = request.FILES['Wimage']
        obj = WebsiteDB(WebName=wna, WebAbout=wab, WebImage=wimg)
        obj.save()
        messages.success(request, "link added successfully...!")
        return redirect(weblink)
def displayWeb(request):
    data = WebsiteDB.objects.all()
    return render(request, "Site_Display.html", {'data': data})
def EditWeb(request, dataid):
    wdata = WebsiteDB.objects.get(id=dataid)
    return render(request,"Site_Edit.html",{'wdata':wdata})
def updateWeb(request, dataid):
    if request.method == "POST":
        wna = request.POST.get('wname')
        wab = request.POST.get('webabout')
        try:
            wimg = request.FILES['Wimage']
            fs = FileSystemStorage()
            file = fs.save(wimg.name, wimg)
        except MultiValueDictKeyError:
            file = WebsiteDB.objects.get(id=dataid).WebImage
        WebsiteDB.objects.filter(id=dataid).update(WebName=wna, WebAbout=wab, WebImage=file)
        messages.info(request, "link updated successfully...!")
        return redirect(displayWeb)
def deleteWeb(request, dataid):
    website = WebsiteDB.objects.filter(id=dataid)
    website.delete()
    messages.error(request, "link deleted successfully...!")
    return redirect(displayWeb)

def Person_DV(r):
    category = CategoryDB.objects.all()
    return render(r,"Add_DV.html", {'category':category})
def pdata(request):
    if request.method == "POST":
        pna = request.POST.get('pname')
        pema = request.POST.get('pemail')
        pgen = request.POST.get('pgender')
        ploc = request.POST.get('plocation')
        pocc = request.POST.get('poccupation')
        pcat = request.POST.get('pcategory')
        pdv = request.POST.get('pdov')
        pam = request.POST.get('pamount')
        pab = request.POST.get('pabout')
        pimg = request.FILES['pimage']
        obj = PersonDB(Pname=pna,Pemail=pema,Pgender=pgen,Plocation=ploc,Poccupation=pocc,Pcategory=pcat,
                       pDOV=pdv,pamount=pam,Pabout=pab,Pimage=pimg)
        obj.save()
        messages.success(request, "Person added successfully...!")
        return redirect(Person_DV)
def displayper(request):
    data = PersonDB.objects.all()
    return render(request, "Display_DV.html", {'data': data})
def Editper(request, dataid):
    person_data = PersonDB.objects.get(id=dataid)
    category = CategoryDB.objects.all()
    return render(request,"Edit_DV.html",{'category':category,'person_data':person_data})
def updateper(request, dataid):
    if request.method == "POST":
        pna = request.POST.get('pname')
        pema = request.POST.get('pemail')
        pgen = request.POST.get('pgender')
        ploc = request.POST.get('plocation')
        pocc = request.POST.get('poccupation')
        pcat = request.POST.get('pcategory')
        pdv = request.POST.get('pdov')
        pam = request.POST.get('pamount')
        pab = request.POST.get('pabout')
        try:
            pimg = request.FILES['pimage']
            fs = FileSystemStorage()
            file = fs.save(pimg.name, pimg)
        except MultiValueDictKeyError:
            file = PersonDB.objects.get(id=dataid).Pimage
        PersonDB.objects.filter(id=dataid).update(Pname=pna,Pemail=pema,Pgender=pgen,Plocation=ploc,Poccupation=pocc,Pcategory=pcat,
                       pDOV=pdv,pamount=pam,Pabout=pab,Pimage=file)
        messages.info(request, "Person updated successfully...!")
        return redirect(displayper)
def deleteper(request, dataid):
    Person = PersonDB.objects.filter(id=dataid)
    Person.delete()
    messages.error(request, "Person deleted successfully...!")
    return redirect(displayper)
