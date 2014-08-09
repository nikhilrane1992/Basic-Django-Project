#from django.core.context_processors import csrf as csrf1
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth 

def login(request):
	print "Hello From login function"
	"""c = {}
	c.update(csrf1(request))
	print c"""
	return render_to_response('login.html' )
	
def auth_view():
	username = request.POST.get('username' , ' ')
	password = request.POST.get('password' , ' ')
	user = auth.authenticate(username = username , password = password)
	
	if user is not none:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')
		
def loggedin(request):
	return render_to_response('loggedin.html' , {'fullname' : request.user.username })
	
def invalid_login(request):
	return render_to_response('invalid_login.html')
	
def invalid_login(request):
	auth.logout(request)
	return render_to_response('logout.html')
	

