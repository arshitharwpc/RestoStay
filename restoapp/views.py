from django.shortcuts import render,redirect,get_object_or_404
from django.conf import settings
from django.http import HttpResponseRedirect
from  .models import *
from django.core.mail import send_mail
import datetime
from django.core.exceptions import ObjectDoesNotExist

def home(request):
	return render(request,'home.html')

def index(request):
	idata=review.objects.all()
	return render(request,'index.html',{'rdata':idata})

def about(request):
	return render(request,'about.html')
#################################################################################################################
def food(request):
    sdata = foodcart.objects.all()
    odata = offer.objects.all() 

    context = {
        'fdata': sdata,
        'odata': odata
    }

    return render(request, 'food.html', context)


def ftable(request):
	idata=foodcart.objects.all()
	return render(request,'admin/ftable.html',{'fdata':idata})

def finput(request):
	if request.method=='POST':
		iname=request.POST['text1']
		price=request.POST['text2']  
		image=request.FILES['text7']

		add=foodcart(price=price,itemname=iname,image=image)
		add.save()
		return render(request,'admin/index.html')
	else:
		return render(request,'admin/finput.html')

def ftableupdate(request):
	if request.method == 'POST':
		iname = request.POST.get('text1')
		price = request.POST.get('text2')
		image = request.FILES.get('text7')
		tid = request.GET.get('tid')

		item = foodcart.objects.get(id=tid)
		item.itemname = iname
		item.price = price

		if image: 
			item.image = image

		item.save()
		return render(request, 'admin/ftable.html', {'fdata': foodcart.objects.all()})
	else:
		tid = request.GET.get('tid')
		admin = foodcart.objects.filter(id=tid)
		return render(request, 'admin/fupdate.html', {'newdata5': admin})	

def ftabledelete(request):
	tid=request.GET['tid']
	tdata=foodcart.objects.filter(id=tid).delete()
	return redirect('/ftable/')
#####################################################################################################################

def addtocart(request):
    if request.session.has_key('myid'):
        uid = request.session['myid']
        
        if request.method == 'POST':
            tid = request.GET['tid']
            qty = request.POST['text1']
            
            item = foodcart.objects.filter(id=tid)
            for x in item:
                price = x.price
            
            totalamount = int(price) * int(qty)
            user = registers.objects.get(id=uid)
            item1 = foodcart.objects.get(id=tid)
            check = order.objects.filter(tid=item1, uid=user)
            data = order.objects.filter(uid=uid)
            
            total = 0
            for x in data:
                price = x.totalamount
                total = int(price) + total
            
            if check:
                return render(request, 'cart.html', {"error": "The product is already in the cart", 'cdata': data, "total": total})
            else:
                new_cart = order(tid=item1, uid=user, totalamount=totalamount, quantity=qty)
                new_cart.save()
                data = order.objects.filter(uid=uid)
                return render(request, "cart.html", {'cdata': data, "total": total})
        else:
            tid = request.GET['tid']
            data = foodcart.objects.filter(id=tid)
            return render(request, 'cart2.html', {'bdata': data})
    else:
        return render(request, "login.html")

def acart(request):
	if request.session.has_key('myid'):
		uid=request.session['myid']
		data=order.objects.filter(uid=uid)
		total=0
		for x in data:
			price=x.totalamount
			total=int(price)+total			
		return render(request, "cart.html",{'cdata':data,"total":total})
	else:
		return render(request,'login.html')

def updatecart(request):
	cid=request.GET['cid']
	qty=request.POST['quantity']
	data=order.objects.filter(id=cid)
	
	for x in data:
		price=x.tid.price
	total=int(price)*int(qty)
	totalamount=int(total)
	order.objects.filter(id=cid).update(totalamount=totalamount,quantity=qty)
	return redirect('/acart/')


def cartdelete(request):
	cid=request.GET['cid']
	tdata=order.objects.filter(id=cid).delete()
	return redirect('/acart/')

def carttable(request):
	idata=order.objects.all()
	return render(request,'admin/carttable.html',{'cadata':idata})
#####################################################################################################################
def service(request):
	return render(request,'service.html')

def menu(request):
    bdata = breakfast.objects.all()  
    ldata = lunch.objects.all()      
    ddata = dinner.objects.all()  

    context = {
        'bdata': bdata,
        'ldata': ldata,
        'ddata': ddata,
    }
    return render(request, 'menu.html', context)

def team(request):
	return render(request,'team.html')

def testimonial(request):
	return render(request,'testimonial.html')

def contact(request):
	if request.method=='POST':
		name=request.POST['text1']
		email=request.POST['text2']
		phone=request.POST['text3']
		#password=request.POST['text4']
		message=request.POST['text4']

		user=contacts(username=name,useremail=email,userphone=phone,message=message)
		user.save()
		return render(request,'index.html')
	else:
		return render(request,'contact.html')
def rctable(request):
	idata=contacts.objects.all()
	return render(request,'admin/restoctable.html',{'rcdata':idata})

def register(request):
    if request.method == 'POST':
        fname = request.POST['text1']
        lname = request.POST['text2']
        email = request.POST['text3']
        phone = request.POST['text4']
        password = request.POST['text5']
        #hashpass = hashlib.md5(password.encode('utf8')).hexdigest()

        user = registers(userfname=fname, userlname=lname, userpassword=password, useremail=email, userphone=phone)
        user.save()
        #fname = user.userfname
        #email = user.useremail

        # Corrected indentation for the following block
        #subject = 'Welcome to our site'
        #email_message = f'Hi {fname}, thank you for booking on our site. Your booking is confirmed for.'
        #email_from = settings.EMAIL_HOST_USER 
        #recipient_list = [email] 

        #Ssend_mail(subject, email_message, email_from, recipient_list)

        return render(request, 'index.html')
    else:
        return render(request, 'register.html')

def regtable(request):
	idata=registers.objects.all()
	return render(request,'admin/regtable.html',{'redata':idata})


def login(request):
	if request.method=='POST':
		email=request.POST['text3']
		password=request.POST['text5']
		#hashpass=hashlib.md5(password.encode('utf8')).hexdigest()

		check=registers.objects.filter(useremail=email,userpassword=password)
		if check:
			for x in check:
				request.session['myid']=x.id
				request.session['myname']=x.userfname
				return render(request,'index.html',{'success':'logged in'})
		else:
			return render(request,'login.html',{'error':'invalid emailid / password'})
	else:
		return render(request,'login.html')

def hlogin(request):
	if request.method=='POST':
		email=request.POST['text3']
		password=request.POST['text5']
		#hashpass=hashlib.md5(password.encode('utf8')).hexdigest()

		check=registers.objects.filter(useremail=email,userpassword=password)
		if check:
			for x in check:
				request.session['myid']=x.id
				request.session['myname']=x.userfname
				return render(request,'hotel/index.html',{'success':'logged in'})
		else:
			return render(request,'hotel/login.html',{'error':'invalid emailid / password'})
	else:
		return render(request,'hotel/login.html')

def logout(request):
	if request.session.has_key('myid'):
		del request.session['myid']
		del request.session['myname']
		return redirect('/index')
	else:
		return redirect('/index')

def hlogout(request):
	if request.session.has_key('myid'):
		del request.session['myid']
		del request.session['myname']
		return redirect('/hotel_index')
	else:
		return redirect('/hotel_index')

def booking(request):
    if request.session.has_key('myid'):
        uid = request.session['myid']
        
        if request.method == 'POST':
            select = request.POST.get('text4', '')  # Get form data safely
            date = datetime.datetime.now().date()
            time = datetime.datetime.now().time()
            message = request.POST.get('text7', '')

            # Get the user, handling potential errors
            user = get_object_or_404(registers, id=uid)

            # Save booking to database
            books = bookers(uid=user, select=select, date=date, time=time, message=message)
            books.save()

            # Send email confirmation
            fname = user.userfname  
            email = user.useremail
            subject = 'Welcome to our site'
            email_message = f'Hi {fname}, thank you for booking on our site. Your booking is confirmed for {date} at {time}.'
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = [email] 

            send_mail(subject, email_message, email_from, recipient_list)

            return render(request, 'review.html', {'message': 'Booking successful!'})
        else:
        	return render(request, 'booking.html') 


    else:
        return render(request, 'login.html')

def tbtable(request):
	tbdata=bookers.objects.all()
	return render(request,'admin/tbtable.html',{'tbdata':tbdata})



def treview(request):
    if request.session.has_key('myid'):
        uid = request.session['myid']
        
        if request.method == 'POST':
            r1 = request.POST['text4']
            user = get_object_or_404(registers, id=uid)
            add = review(rev=r1, uid=user)
            add.save()
            return render(request, 'index.html')
        else:
            return render(request, 'review.html')
    
    else:
        return render(request, 'login.html')

def trtable(request):
	idata=review.objects.all()
	return render(request,'admin/trtable.html',{'trdata':idata})

def hrtable(request):
	idata=hreview.objects.all()
	return render(request,'admin/hrtable.html',{'hrdata':idata})

def rreview(request):
    if request.session.has_key('myid'):
        uid = request.session['myid']
        
        if request.method == 'POST':
            r1 = request.POST['text1']
            user = get_object_or_404(registers, id=uid)
            add = hreview(rev=r1, uid=user)
            add.save()
            return render(request, 'hotel/index.html')
        else:
            return render(request, 'hotel/review.html')
    
    else:
        return render(request, 'hotel/login.html')

#def cart(request):
	#return render(request,'cart.html');
def hindex(request):
	idata=hreview.objects.all()
	return render(request,'hotel/index.html',{'hrdata':idata})

def habout(request):
	return render(request,'hotel/about.html')

def hservice(request):
	return render(request,'hotel/service.html')

def hteam(request):
	return render(request,'hotel/team.html')

def htestimonial(request):
	return render(request,'hotel/testimonial.html')

def hbooking(request):
    if request.session.has_key('myid'):
        uid = request.session['myid']

        if request.method == 'POST':
            # Get current date for check-in and check-out
            chein = datetime.datetime.now().date()
            cheout = datetime.datetime.now().date()

            # Get form data safely with default values
            adult = request.POST.get('text3', '0')
            child = request.POST.get('text4', '0')
            room = request.POST.get('text5', '1')
            req = request.POST.get('text6', '')

            # Get the user, handling potential errors
            user = get_object_or_404(registers, id=uid)

            # Save booking to database
            book = rbookers(uid=user, chein=chein, cheout=cheout, adult=adult, child=child, room=room, req=req)
            book.save()

            # Send email confirmation
            fname = user.userfname  
            email = user.useremail
            subject = 'Welcome to our site'
            email_message = f'Hi {fname}, thank you for booking on our site. Your booking is confirmed for {chein}.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]

            send_mail(subject, email_message, email_from, recipient_list)

            return render(request, 'hotel/review.html', {'message': 'Booking successful!'})  # Pass confirmation message
        else:
            return render(request, 'hotel/booking.html')
    else:
        return render(request, 'hotel/login.html')

def rbtable(request):
	rbdata=rbookers.objects.all()
	return render(request,'admin/rbtable.html',{'rbdata':rbdata})

def hcontact(request):
	if request.method=='POST':
		name=request.POST['text1']
		email=request.POST['text2']
		phone=request.POST['text3']
		#password=request.POST['text4']
		message=request.POST['text4']

		user=hcontacts(username=name,useremail=email,userphone=phone,message=message)
		user.save()
		return render(request,'hotel/index.html')
	else:
		return render(request,'hotel/contact.html')

def hctable(request):
	idata=hcontacts.objects.all()
	return render(request,'admin/stayctable.html',{'hcdata':idata})

def hroom(request):
	sdata = rooms.objects.all()  
	return render(request,'hotel/room.html',{'rdata':sdata})

def hcart(request):
	return render(request,'hotel/cart.html')
###############################################################################################

def aindex(request):
	if request.session.has_key('myid'):
		return render(request,'admin/index.html')
	else:
		return render(request,'admin/signin.html')
def asignin(request):
	if request.method=='POST':
		email=request.POST['text1']
		password=request.POST['text2']
		#hashpass=hashlib.md5(password.encode('utf8')).hexdigest()

		check=aregisters.objects.filter(useremail=email,userpassword=password)
		if check:
			for x in check:
				request.session['myid']=x.id
				request.session['myname']=x.userfname
				return render(request,'admin/index.html',{'success':'logged in'})
		else:
			return render(request,'admin/signin.html',{'error':'invalid emailid / password'})
	else:
		return render(request,'admin/signin.html')

def asignup(request):
	if request.method=='POST':
		fname=request.POST['text1']
		lname=request.POST['text2']
		email=request.POST['text3']
		phone=request.POST['text4']
		password=request.POST['text5']
		#hashpass=hashlib.md5(password.encode('utf8')).hexdigest()

		user=aregisters(userfname=fname,userlname=lname,userpassword=password,useremail=email,userphone=phone)
		user.save()
		return render(request,'admin/signin.html')
	else:	
		return render(request,'admin/signup.html')

def asignout(request):
	if request.session.has_key('myid'):
		del request.session['myid']
		del request.session['myname']
		return redirect('/asignin/')
	else:
		return redirect('/aindex/')

def table(request):
	return render(request,'admin/tables.html')

def achart(request):
	return render(request,'admin/chart.html')

def payment(request):
	return render(request,'payment/index.html')
###################################################################
def binput(request):
	if request.method=='POST':
		iname=request.POST['text1']
		price=request.POST['text2']  
		image=request.FILES['text7']

		add=breakfast(price=price,itemname=iname,image=image)
		add.save()
		return render(request,'admin/index.html')
	else:
		return render(request,'admin/input.html')

def btableupdate(request):
    if request.method == 'POST':
        iname = request.POST.get('text1')
        price = request.POST.get('text2')
        image = request.FILES.get('text7')
        tid = request.GET.get('tid')

        item = breakfast.objects.get(id=tid)
        item.itemname = iname
        item.price = price

        if image: 
            item.image = image

        item.save()
        return render(request, 'admin/btable.html', {'bdata': breakfast.objects.all()})
    else:
        tid = request.GET.get('tid')
        admin = breakfast.objects.filter(id=tid)
        return render(request, 'admin/bupdate.html', {'newdata2': admin})


def btabledelete(request):
	tid=request.GET['tid']
	tdata=breakfast.objects.filter(id=tid).delete()
	return redirect('/btable/')


def btable(request):
	idata=breakfast.objects.all()
	return render(request,'admin/btable.html',{'bdata':idata})
##########################################################################

def linput(request):
	if request.method=='POST':
		iname=request.POST['text1']
		price=request.POST['text2']  
		image=request.FILES['text7']

		add=lunch(price=price,itemname=iname,image=image)
		add.save()
		return render(request,'admin/index.html')
	else:
		return render(request,'admin/input.html')

def ltableupdate(request):
	if request.method == 'POST':
		iname = request.POST.get('text1')
		price = request.POST.get('text2')
		image = request.FILES.get('text7')
		tid = request.GET.get('tid')

		item = lunch.objects.get(id=tid)
		item.itemname = iname
		item.price = price

		if image: 
			item.image = image

		item.save()
		return render(request, 'admin/ltable.html', {'ldata': lunch.objects.all()})
	else:
		tid = request.GET.get('tid')
		admin = lunch.objects.filter(id=tid)
		return render(request, 'admin/lupdate.html', {'newdata3': admin})	

def ltabledelete(request):
	tid=request.GET['tid']
	tdata=lunch.objects.filter(id=tid).delete()
	return redirect('/ltable/')

def ltable(request):
	cdata=lunch.objects.all()
	return render(request,'admin/ltable.html',{'ldata':cdata})

###############################################################################

def dinput(request):
	if request.method=='POST':
		iname=request.POST['text1']
		price=request.POST['text2']  
		image=request.FILES['text7']

		add=dinner(price=price,itemname=iname,image=image)
		add.save()
		return render(request,'admin/index.html')
	else:
		return render(request,'admin/input.html')

def dtableupdate(request):
	if request.method == 'POST':
		iname = request.POST.get('text1')
		price = request.POST.get('text2')
		image = request.FILES.get('text7')
		tid = request.GET.get('tid')

		item = dinner.objects.get(id=tid)
		item.itemname = iname
		item.price = price

		if image: 
			item.image = image

		item.save()
		return render(request, 'admin/dtable.html', {'ddata': dinner.objects.all()})
	else:
		tid = request.GET.get('tid')
		admin = dinner.objects.filter(id=tid)
		return render(request, 'admin/dupdate.html', {'newdata4': admin})	

def dtabledelete(request):
	tid=request.GET['tid']
	tdata=dinner.objects.filter(id=tid).delete()
	return redirect('/dtable/')

def dtable(request):
	gdata=dinner.objects.all()
	return render(request,'admin/dtable.html',{'ddata':gdata})
##############################################################################

'''def addtocart(request):
	if request.method=='POST':
		tid=request.GET['tid']
		uid=request.session['myid']
		qty=request.POST['text1']
		item=breakfast.objects.filter(id=tid)
		for x in item:
			price=x.price
		totalamount=int(price)*int(qty)
		user=registers.objects.get(id=uid)
		item1=breakfast.objects.get(id=tid)
		check=addcart.objects.filter(tid=item1,uid=user)
		data=addcart.objects.filter(uid=uid)
		total=0
		for x in data:
			price=x.totalamount
			total=int(price)+total
		if check:
			return render(request,'cart.html',{"error":"the product is already in the cart",'cdata':data,"total":total})
		else:
			addcart=addcart(tid=item1,uid=user,totalamount=totalamount,quantity=qty)
			addcart.save()
			data=addcart.objects.filter(uid=uid,status="pending")
			
			return render(request, "cart.html",{'cdata':data,"total":total})
	else:
		tid=request.GET['tid']
		data=lunch.objects.filter(id=tid)
		return render(request,'cart.html',{'bdata':data})'''

def cart(request):		
		return render(request, "cart1.html")

##################################################################
def rtable(request):
	idata=rooms.objects.all()
	return render(request,'admin/rtable.html',{'rdata':idata})

def rinput(request):
	if request.method=='POST':
		rname=request.POST['text1']
		price=request.POST['text2']  
		desc=request.POST['text3'] 
		image=request.FILES['text7']

		add=rooms(price=price,rname=rname,image=image,description=desc)
		add.save()
		return render(request,'admin/index.html')
	else:
		return render(request,'admin/rinput.html')

def rtableupdate(request):
    if request.method == 'POST':
        iname = request.POST.get('text1')
        price = request.POST.get('text2')
        image = request.FILES.get('text7')
        desc=request.POST.get('text3') 
        rid = request.GET.get('rid')

        item = rooms.objects.get(id=rid)
        item.itemname = iname
        item.price = price
        item.description = desc

        if image: 
            item.image = image

        item.save()
        return render(request, 'admin/rtable.html', {'rdata': rooms.objects.all()})
    else:
        rid = request.GET.get('rid')
        admin = rooms.objects.filter(id=rid)
        return render(request, 'admin/rupdate.html', {'newdata5': admin})


def rtabledelete(request):
	rid=request.GET['rid']
	tdata=rooms.objects.filter(id=rid).delete()
	return redirect('/rtable/')

def payment(request):
	if request.method == "POST":
		cdate=datetime.datetime.now().date()
		ctime=datetime.datetime.now().time()
		uid=request.session['myid']
		user=registers.objects.get(id=uid)
		total=request.POST["price"]
		add=pay(uid=user,totalamount=total,date=cdate,time=ctime,status="paid")
		add.save()
		order.objects.filter(uid=user)
		return redirect("/index")
	else:
		Total=request.GET["gt"]
		return render(request,"payment/index.html",{"gt":Total})

def oinput(request):
	if request.method=='POST':
		iname=request.POST['text1']
		price=request.POST['text2']  
		desc=request.POST['text3'] 
		image=request.FILES['text7']

		add=offer(price=price,itemname=iname,image=image,description=desc)
		add.save()
		return render(request,'admin/index.html')
	else:
		return render(request,'admin/oinput.html')	

def otable(request):
	idata=offer.objects.all()
	return render(request,'admin/otable.html',{'odata':idata})

def otableupdate(request):
    if request.method == 'POST':
        iname = request.POST.get('text1')
        price = request.POST.get('text2')
        image = request.FILES.get('text7')
        desc=request.POST.get('text3') 
        oid = request.GET.get('oid')

        item = offer.objects.get(id=oid)
        item.itemname = iname
        item.price = price
        item.description = desc

        if image: 
            item.image = image

        item.save()
        return render(request, 'admin/otable.html', {'odata': offer.objects.all()})
    else:
        oid = request.GET.get('oid')
        admin = offer.objects.filter(id=oid)
        return render(request, 'admin/oupdate.html', {'newdata6': admin})


def otabledelete(request):
	oid=request.GET['oid']
	tdata=offer.objects.filter(id=oid).delete()
	return redirect('/otable/')