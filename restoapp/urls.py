from django.urls import path
from restoapp import views



urlpatterns=[   

				path('',views.home),
				path('index',views.index),
				path('about',views.about),
				path('service',views.service),
				path('menu',views.menu),
				path('booking',views.booking),
				path('team',views.team),
				path('testimonial',views.testimonial),
				path('contact',views.contact),
				path('login',views.login),
				path('register',views.register),
				path('logout',views.logout),
			
				path('hotel_index',views.hindex),
				path('hotel_login',views.hlogin),
				path('hotel_about',views.habout),
				path('hotel_service',views.hservice),
				path('hotel_room',views.hroom),
				path('hotel_booking',views.hbooking),
				path('hotel_team',views.hteam),
				path('hotel_testimonial',views.htestimonial),
				path('hotel_contact',views.hcontact),
				path('payment',views.payment),
				
				path('aindex/',views.aindex),
             	path('asignin/',views.asignin),
             	path('asignup/',views.asignup),
            	path('asignout/',views.asignout),
             	path('table/',views.table),
             	path('achart/',views.achart),
             	path('input/',views.binput),
             	path('binput/',views.binput),
             	path('linput/',views.linput),
             	path('dinput/',views.dinput),
             	path('rinput/',views.rinput),
             	path('finput/',views.finput),
                  path('oinput/',views.oinput),
             	path('btable/',views.btable),
             	path('ltable/',views.ltable),
             	path('dtable/',views.dtable),
             	path('rtable/',views.rtable),
             	path('ftable/',views.ftable),
             	path('rctable/',views.rctable),
             	path('hctable/',views.hctable),
             	path('hrtable/',views.hrtable),
             	path('trtable/',views.trtable),
                  path('otable/',views.otable),
                  path('regtable/',views.regtable),
                  path('carttable/',views.carttable),
                  path('rbtable/',views.rbtable),
                  path('tbtable/',views.tbtable),
             	path('btableupdate/',views.btableupdate),
             	path('btabledelete/',views.btabledelete),
             	path('rtableupdate/',views.rtableupdate),
             	path('rtabledelete/',views.rtabledelete),
             	path('ltableupdate/',views.ltableupdate),
             	path('ftableupdate/',views.ftableupdate),
             	path('ftabledelete/',views.ftabledelete),
             	path('ltabledelete/',views.ltabledelete),
             	path('dtableupdate/',views.dtableupdate),
             	path('dtabledelete/',views.dtabledelete),
                  path('otableupdate/',views.otableupdate),
                  path('otabledelete/',views.otabledelete),
             	path('cart',views.cart),
             	path('treview',views.treview),
             	path('rreview',views.rreview),
             	path('foodcart',views.food),
             	path('addtocart/',views.addtocart),
             	path('acart/',views.acart),
                path('updatecart/',views.updatecart),
             	path('cartdelete/',views.cartdelete),
             	path('payment/',views.payment),







]

