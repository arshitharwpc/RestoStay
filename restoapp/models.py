from django.db import models

# Create your models
class registers(models.Model):
	userfname=models.CharField(max_length=255)
	userlname=models.CharField(max_length=255)
	useremail=models.CharField(max_length=255)
	userphone=models.CharField(max_length=255)
	userpassword=models.CharField(max_length=255)
	hashpass=models.TextField()

	
class contacts(models.Model):
	username=models.CharField(max_length=255)
	useremail=models.CharField(max_length=255)
	userphone=models.CharField(max_length=255)
	message=models.CharField(max_length=255)

class hcontacts(models.Model):
	username=models.CharField(max_length=255)
	useremail=models.CharField(max_length=255)
	userphone=models.CharField(max_length=255)
	message=models.CharField(max_length=255)


class bookers(models.Model):
	uid=models.ForeignKey(registers,on_delete=models.CASCADE,null=True)
	date=models.CharField(max_length=255)
	time=models.CharField(max_length=255)
	select=models.CharField(max_length=255)
	message=models.CharField(max_length=255)



class aregisters(models.Model):
	userfname=models.CharField(max_length=255)
	userlname=models.CharField(max_length=255)
	useremail=models.CharField(max_length=255)
	userphone=models.CharField(max_length=255)
	userpassword=models.CharField(max_length=255)

class breakfast(models.Model):
	itemname=models.CharField(max_length=255)
	price=models.CharField(max_length=255)
	image=models.ImageField(upload_to='media/')

class lunch(models.Model):
	itemname=models.CharField(max_length=255)
	price=models.CharField(max_length=255)
	image=models.ImageField(upload_to='media/')

class dinner(models.Model):
	itemname=models.CharField(max_length=255)
	price=models.CharField(max_length=255)
	image=models.ImageField(upload_to='media/')

class cart(models.Model):
	tid=models.ForeignKey(breakfast,on_delete=models.CASCADE)
	uid=models.ForeignKey(registers,on_delete=models.CASCADE)
	totalamount=models.CharField(max_length=255)
	quantity=models.CharField(max_length=255,default="")

class rooms(models.Model):
	rname=models.CharField(max_length=255)
	price=models.CharField(max_length=255)
	description=models.CharField(max_length=255)
	image=models.ImageField(upload_to='media/')

class review(models.Model):
	uid=models.ForeignKey(registers,on_delete=models.CASCADE)
	rev=models.CharField(max_length=255)

class hreview(models.Model):
	uid=models.ForeignKey(registers,on_delete=models.CASCADE)
	rev=models.CharField(max_length=255)

class foodcart(models.Model):
	itemname=models.CharField(max_length=255)
	price=models.CharField(max_length=255)
	image=models.ImageField(upload_to='media/')

class order(models.Model):
	tid=models.ForeignKey(foodcart,on_delete=models.CASCADE)
	uid=models.ForeignKey(registers,on_delete=models.CASCADE)
	totalamount=models.CharField(max_length=255)
	quantity=models.CharField(max_length=255,default="")

class rbookers(models.Model):
	#tid=models.ForeignKey(rooms,on_delete=models.CASCADE)
	uid=models.ForeignKey(registers,on_delete=models.CASCADE,null=True)
	chein=models.CharField(max_length=255)
	cheout=models.CharField(max_length=255)
	adult=models.CharField(max_length=255)
	child=models.CharField(max_length=255)
	room=models.CharField(max_length=255)
	req=models.CharField(max_length=255)
	
class pay(models.Model):
	uid=models.ForeignKey(registers,on_delete=models.CASCADE)
	totalamount=models.CharField(max_length=255)
	date=models.CharField(max_length=255)
	time=models.CharField(max_length=255)
	status=models.CharField(max_length=255,default="pending")

class offer(models.Model):
	itemname=models.CharField(max_length=255)
	price=models.CharField(max_length=255)
	description=models.CharField(max_length=255)
	image=models.ImageField(upload_to='media/')

	













