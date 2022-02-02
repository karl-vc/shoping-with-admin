from django.shortcuts import render,HttpResponse,HttpResponseRedirect

from django.views.generic import TemplateView

from django.views import View

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from productApp.models import *
from dashboardApp.models import *

from django.core.files.storage import FileSystemStorage
import uuid
# # Create your views here.


class HomePage(TemplateView):
	def get(self,request):

		# if request.user.is_authenticated:
		if request.user.is_superuser:
			logout(request)
			# return render(request,'index.html',locals())
			return HttpResponseRedirect('/')

			# product_data = ProductDetail.objects.filter(is_delete = False)
		# Page.objects.filter(site=site).exclude(pk__in=[p.pk for p in pages])
		else:
			product_data = ProductDetail.objects.filter(is_delete = False)


			return render(request,'index.html',locals())
		# else:
		# 	return render(request,'')

		
	def post(self,request):
		return render(request,'index.html')



class Signup(TemplateView):

	def get(self,request):

		return render(request,'sign-up.html')

		# if request.user.is_authenticated:
		# 	return HttpResponseRedirect('/')
		# else:
		# 	return render(request,'index.html')

	def post(self,request):


		firstname = request.POST.get('firstname')
		lastname = request.POST.get('lastname')
		email = request.POST.get('email')
		rawpassword= request.POST.get('rawpassword')
		confirmpasssword= request.POST.get('confirmpassword')
		

		if firstname is None or lastname == "" or email=="" or rawpassword=='' or confirmpasssword=='':

			print('all fields are mandatory')
			return render(request,'sign-up.html',{'all_fields':True})

		else:
			if rawpassword == confirmpasssword:
				try:
					user = User.objects.get(email = email)
					print("user already exists")
					return render(request,'sign-up.html',{'already_exist':True})

				except:

					user = User(first_name = firstname ,last_name = lastname, username = email,email = email)
					user.set_password(confirmpasssword)
					user.save()
										
					return HttpResponseRedirect('login')
			else:
				print('password does not match...')
				return render(request,'sign-up.html',{'invalid_password':True})
	

		return render(request,'sign-up.html')



class Login(TemplateView):
	# template_name = 'login.html'

	def get(self,request):
		return render(request,'login.html')
		# if request.user.is_authenticated:                                                     
		# 	return HttpResponseRedirect("/")
		# else:
		# 	return render(request,self.template_name,{})
		

	def post(self,request):

		email = request.POST.get('email')
		password = request.POST.get('password')
	
	
		try:
			user = User.objects.get(email=email)
			userauth = authenticate(username=user.username, password=password)
			if userauth:
				login(request, user,backend='django.contrib.auth.backends.ModelBackend')
				if request.user.is_authenticated:
					return HttpResponse('yes i am logged-in')
				else:
					return HttpResponseRedirect('login')
			else:
				return HttpResponseRedirect('login')
		except Exception as e:
			
			return HttpResponseRedirect('login')




		return render(request,'login.html')


class AboutUs(TemplateView):

	def get(self,request):
		return render(request,'aboutus.html')




class ViewProducts(TemplateView):

	def get(self,request):
		# if request.user.is_authenticated:

		# 	product_data = ProductDetail.objects.filter(is_delete = False)
		# 	# Page.objects.filter(site=site).exclude(pk__in=[p.pk for p in pages])

		# 	return render(request,'index.html',locals())
		# else:
		# 	return render(request,'/')

		return render(request,'index.html')


	def post(self,request):
		return render(request,'index.html')



class ProductDetailPage(TemplateView):

	def get(self,request,*args, **kwargs):
		# if request.user.is_authenticated:

		data = kwargs.get('slug')
		product_data = ProductDetail.objects.get(slug = data)

		picture_data = ProductImages.objects.filter(product_id = product_data)
		print(picture_data,'pictureeeeeeeeeeeeeee/.................................')
		
		return render(request,'product_page.html',locals())

		# else:
		# 	return render(request,'product_page.html')




	def post(self,request):

		return render(request,'product_page.html')



class UserLogout(View):
	def get(self,request):
		logout(request)
		return HttpResponseRedirect('/')




class ForgetPassword(TemplateView):

	def get(self,request):
		return render(request,'forget_password.html')

	def post(self,request):
		email = request.POST.get('email')

		try:
			user_data = User.objects.get(email = email)
			# return render(request,'reset_password.html')
			# if user_data:
			unique_id = uuid.uuid4()
			uiid_data = ForgetPasswordModel.objects.create(user_id = user_data,verification_id = unique_id)

			print(unique_id,'iidddddddddddd.......unique...............')
		
			link = f'http://127.0.0.1:8000/reset_password/{unique_id}'
			# link = 'http://127.0.0.1:8000/reset_password/'+str(unique_id)

			print(link,'id...................................linkkkk')


			return HttpResponse('check your mail')
			# return HttpResponseRedirect('reset_password',pk = uiid_data.uiid_id , permanent = True)

			# else:
			# 	return HttpResponseRedirect('forget_password',{'no_ema
		except:
			return HttpResponseRedirect('forget_password',{'no_email':True})


class ResetPassword(TemplateView):
	def get(self,request,*args, **kwargs):
		verification_id = kwargs.get('verification_id')
		print(verification_id,'linkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkuserrrrrrrrrrr')
		try:
			verification_data = ForgetPasswordModel.objects.get(verification_id = verification_id)
		except:
			return HttpResponse('verification token has been expired')


		# print(verification_data.verification_id,'verificationnnn....................nnn')
		
		# user_data = User.objects.get(email = verification_data.user_id)
		# print(user_data,'userrrrrrrrrrrrr_______________________dataaaaaaaaa')


		return render(request,'reset_password.html')

	def post(self,request,*args, **kwargs):
		
		verification_id = kwargs.get('verification_id')

		# user_data = User.objects.get(email = verification_data.user_id)
		# print(user_data,'userrrrrrrrrrrrr_______________________dataaaaaaaaa')
	
		raw_password = request.POST.get('raw_password')
		confirm_password = request.POST.get('confirm_password')

		if raw_password == confirm_password:
			try:
				verification_data = ForgetPasswordModel.objects.get(verification_id = verification_id)
			except:
				return HttpResponse('verification token has been expired')

			user_data = User.objects.get(email = verification_data.user_id)
			print(user_data,'userrrrrrrrrrrrr_______________________dataaaaaaaaa')

			user_data.set_password(confirm_password)

			user_data.save()
			verification_data.delete()

			
			return HttpResponse('password successfully changed')
		else:
			return HttpResponse('password do not match')	
		# else:

		# 	return render(request,'reset_password.html')