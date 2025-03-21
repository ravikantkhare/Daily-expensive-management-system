from django.shortcuts import render,redirect
from .models import User,Expence,Income

# def Home(req):
#     return render(req,'index.html')
def signup(req):
    return render(req,'signup.html') 
def login(req):
    return render(req,'login.html') 
def dashbord(req):
    return render(req,'dashbord.html')
def Addexpence(req):
    return render(req,'expenceadd.html')
def Addincome(req):
    return render(req,'incomeadd.html')
def signupsave(req):
    obj=User()
    obj.uname=req.POST.get('uname')
    obj.age=req.POST.get('age')
    obj.upassword=req.POST.get('upass')
    obj.mobile=req.POST.get('umobile')
    obj.address=req.POST.get('uaddress')
    obj.save()
    return  redirect('/login')
def loginsave(req):
    uname=req.POST.get('unm')
    upassword=req.POST.get('pwd')
    record=User.objects.filter(uname=uname,upassword=upassword) 
    if(record):
        listData=record.values()
        uid=listData[0]['id']
        uname=listData[0]['uname'] 
        req.session['uid']=uid 
        req.session['uname']=uname
        return render(req,'dashbord.html')
    else:
        return render(req,'login.html',{'Error':'invaild choice'})
    
def ExpenceSAve(req):
    if 'uid' in  req.session:
        uid=req.session['uid']
        obj=Expence() 
        obj.time=req.POST.get('time')
        obj.date=req.POST.get('date')
        obj.remark=req.POST.get('remark')
        obj.amount=req.POST.get('amount')
        obj.category=req.POST.get('category')
        obj.user_id=uid
        obj.save() 
        return redirect('/Addexpence')
def IncomeSAve(req):
    if 'uid' in  req.session:
        uid=req.session['uid']
        obj=Income() 
        obj.time=req.POST.get('time')
        obj.date=req.POST.get('date')
        obj.remark=req.POST.get('remark')
        obj.amount=req.POST.get('amount')
        obj.category=req.POST.get('category')
        obj.user_id=uid
        obj.save() 
        return redirect('/Addincome')
def AllIncome(req):
    if 'uid' in req.session:
        uid=req.session['uid']
        record=Income.objects.filter(user_id=uid)
        if(record):
            # list_data=record.values() 
            return render(req,"allincome.html",{'data':record})
    else:
        return redirect("/")
def Allexpence(req):
    if 'uid' in req.session:
        uid=req.session['uid']
        record=Expence.objects.filter(user_id=uid)
        if(record):
            listData=record.values() 
            return render(req,"allexpence.html",{'data':listData})
    else:
        return redirect("/")
def logout(req):
    del req.session['uid']
    del req.session['uname']
    return redirect('/')