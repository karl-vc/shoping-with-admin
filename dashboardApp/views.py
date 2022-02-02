from django.shortcuts import render,HttpResponse,HttpResponseRedirect

from django.views.generic import TemplateView

from django.views import View

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from productApp.models import *
from dashboardApp.models import *
from dashboardApp.admin_permission import AdminPermission

# Create your views here.



class Dashboard(TemplateView,AdminPermission):
	# template_name = 'dashboard.html'

	def get(self,request):
		# if request.user.is_superuser:
			# if request.user.is_superuser:
		product_data = ProductDetail.objects.all()
		product_count = product_data.count()
		user_data = User.objects.all()
		user_count = user_data.count()

		return render(request,'dashboard.html',locals())
			# else:
			# 	pass
		# else:
		# 	return HttpResponseRedirect('dashboardlogin')

		# return render(request,'dashboard.html')

	# def post(self,request):
	# 	return render(request,'dashboard.html')



class DashboardLogin(TemplateView):

	def get(self,request):
		# if request.user.is_authenticated:
		# 	return HttpResponseRedirect('/')
		# else:
		# 	return render(request,'dashboardlogin.html')
		if request.user.is_superuser:
			return HttpResponseRedirect('admindashboard')
		else:

			# logout(request)

			return render(request,'dashboardlogin.html')

	def post(self,request):
		email = request.POST.get('email') 
		password = request.POST.get('password')

		try:
			user = User.objects.get(email = email)
			userauth = authenticate(username = user.username , password = password)
			if userauth:
				login(request, user,backend='django.contrib.auth.backends.ModelBackend')


				# if request.user.is_authenticated:
				if request.user.is_superuser:
					return HttpResponseRedirect('admindashboard')
					# return render(request,'dashboard.html')
				else:
					return render(request,'dashboardlogin.html',{'notSuperuser':True})
				# else:
				# 	return render(request,'dashboardlogin.html',{'notAuthenticated':True})
			else:

				return render(request,'dashboardlogin.html',{'invalidCred':True})


		except:

			return HttpResponseRedirect('dashboardlogin')




class AdminLogout(View):
	def get(self,request):
		logout(request)
		return HttpResponseRedirect('dashboardlogin')




class AddProducts(TemplateView,AdminPermission):

	def get(self,request):
		# if request.user.is_superuser:
		product_data = ProductDetail.objects.all()
		product_count = product_data.count()
		user_data = User.objects.all()
		user_count = user_data.count()

		return render(request,'add_items.html',locals())
		# else:
		# 	return HttpResponseRedirect('dashboardlogin')
		

	def post(self,request,*args, **kwargs):

		number = kwargs.get('num')
		print(number,'slugggggggggggggggggggggggggggggggggggggggggggggggggg')

		productName = request.POST.get('product_name')
		productPrice = request.POST.get('product_price')
		productDescription = request.POST.get('product_description')
		image = request.FILES.get('image')
		# more_images = request.FILES.get('more_images')
		more_images = request.FILES.getlist('more_images[]')
		time_left_to_buy = request.POST.get('time_left')
		total_buyers = request.POST.get('total_buyers')
		for i in more_images:
			print(i,'more images................................................')
				
		price_length = len(productPrice)
		print(price_length,'--------------------XXXXX-------------------')

		if productName == "" or productPrice == "" or productDescription == "" or image is None or time_left_to_buy == "" or total_buyers == "":

			return render(request,'add_items.html',{'all_fields':True})

		elif price_length >= 7:

			return render(request,'add_items.html',{'price_len':True})
 
		else:
			# print('we are hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')

			products_data = ProductDetail(product_name = productName,product_price = productPrice,product_description = productDescription,product_image = image,time_left = time_left_to_buy,total_buyers = total_buyers)
	
			products_data.save()
			# print(more_images,'more imageeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
			for i in more_images:

				product_images = ProductImages(product_id = products_data,product_pictures =  i)

				product_images.save()



			return HttpResponseRedirect('add_items',{'success':True})
	
		


class AllProducts(TemplateView,AdminPermission):

	def get(self,request):
		# if request.user.is_superuser:
		product_data = ProductDetail.objects.all()
		product_count = product_data.count()
		user_data = User.objects.all()
		user_count = user_data.count()

		product_data = ProductDetail.objects.all()

		product_images = ProductImages.objects.all()

		return render(request,'all_products.html',locals())
		# else:
		# 	return HttpResponseRedirect('dashboardlogin')

	def post(self,request):
		# product_data = ProductDetail.objects.all()

		return render(request,'all_products.html')



class DeleteData(View):
	def get(self,request):

	    # user = kwargs.get('user_id')
	    productID = request.GET.get('productID')
	   	
	    # data = ProductDetail.objects.filter(id = int(productID),is_delete = True)
	    data = ProductDetail.objects.get(id = int(productID))
	    data.is_delete = True
	    data.save()

	    return HttpResponseRedirect("all_products")


	    # data(is_delete = True)


	    # print(data,'listtttttttttttttttttt...............data')
	    # for i in data:
	    # 	print(i,'data......................................')

	    # queryset = ABC.objects.filter(soft_delete=True)

	    # data.delete()

	    




	
class EditProduct(TemplateView,AdminPermission):
	
	def get(self,request):
		# if request.user.is_superuser:



		productID = request.GET.get('productID')
		# print(productID,'urlllllllllllllllllllllllllllllllllll..........idddddddddddddddd')
		product_obj = ProductDetail.objects.get(id = productID)

		product_images = ProductImages.objects.filter(product_id = product_obj)



		return render(request,'edit_product.html',locals())
		# else:
		# 	return HttpResponseRedirect('dashboardlogin')

	def post(self,request):
		
		if request.user.is_superuser:

			product_name = request.POST.get('product_name')
			product_price = request.POST.get('product_price')
			product_description = request.POST.get('product_description')
			product_image = request.FILES.get('image')
			more_images = request.FILES.getlist('more_images[]')
			time_left_to_buy = request.POST.get('time_left')
			total_buyers = request.POST.get('total_buyers')
			hidden = request.POST.get('hidden')
			print(hidden,'urlllllllllllllllllllllllllllllllllll..........idddddddddddddddd')


			productID = request.GET.get('productID')
			# print(productID,'urlllllllllllllllllllllllllllllllllll..........idddddddddddddddd')


			product_data = ProductDetail.objects.get(id = productID)
			# product_images = ProductImages.objects.get(product_id = product_data)
			product_images = ProductImages.objects.filter(product_id = product_data)
			product_images.delete()

			if hidden:
				product_data.is_delete = False

			if product_name:
				product_data.product_name = product_name
				# obj_name.model_filed_name = variable_where_inputtagValueIsGet
			if product_price:
				product_data.product_price = product_price
			if product_description:
				product_data.product_description = product_description
			if product_image:
				product_data.product_image = product_image
			if time_left_to_buy:
				product_data.time_left = time_left_to_buy
			if total_buyers:
				product_data.total_buyers = total_buyers

		
			product_data.save()

			if more_images:
				print(more_images,'more imageeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
				for i in more_images:
					# product_images.product_pictures = i
					ProductImages.objects.create(product_id = product_data,product_pictures = i)
					
			return HttpResponseRedirect('all_products')

		else:
			return HttpRespose('you are not authenticated user')
