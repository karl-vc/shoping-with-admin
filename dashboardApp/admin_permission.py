from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView

from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,HttpResponse,HttpResponseRedirect


# class AdminPermission(LoginRequiredMixin,View):
# 	def get(self,request):
# 		if request.user.is_superuser or request.user.is_staff:
# 			login(request)

# 		else:
# 			return HttpResponse('you are not admin')



# class AdminPermission(LoginRequiredMixin, FormView):

#     def dispatch(self, *args, **kwargs):
#         if self.request.user.is_authenticated() and not (
#             self.request.user.is_superuser or
#             self.request.user.is_staff
#         ):
#             raise Http404
#         return super(AdminPermission, self).dispatch(*args, **kwargs)

class AdminPermission(LoginRequiredMixin, FormView):

    def dispatch(self, *args, **kwargs):
        if not (
            self.request.user.is_superuser or
            self.request.user.is_staff
        ):
            # return HttpResponse('you are not admin')
            return HttpResponseRedirect('dashboardlogin')
        return super(AdminPermission, self).dispatch(*args, **kwargs)