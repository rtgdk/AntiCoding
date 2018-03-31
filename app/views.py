#<<<<<<< HEAD
from django.shortcuts import render
from .models import Info,ForAdmin
from .forms import InfoForm,UserForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from anticoding import settings
def index(request):
	context_dict={}
	return render(request, 'app/finalindex.html', context_dict)

def ascii(request):
	context_dict={}
	return render(request, 'app/ascii.html', context_dict)
def round1(request):
	context_dict = {}
	fa = ForAdmin.objects.get(name="A")
	context_dict["admround1"] = fa.round1
	context_dict["admround2"] = fa.round2
	context_dict["admround3"] = fa.round3
	return render(request, 'app/round1.html', context_dict)

def round2(request):
	context_dict = {}
	fa = ForAdmin.objects.get(name="A")
	context_dict["admround1"] = fa.round1
	context_dict["admround2"] = fa.round2
	context_dict["admround3"] = fa.round3
	return render(request, 'app/round2.html', context_dict)

def register(request):
	context_dict = {}
	if request.method == 'POST':
		userform = UserForm(data=request.POST)
		form = InfoForm(data=request.POST)
		if userform.is_valid() and form.is_valid():
			user1 = userform.save(commit=False)
			user1.set_password(user1.password)
			user1.save()
			user = form.save(commit=False)
			user.teamname = user1
			user.save()
			context_dict["done"] = "Now you can login!"
			return render(request, 'app/register.html', context_dict)
			#return render(request, 'app/index.html', context_dict)
		else :
			# context_dict["error1"] = form.errors
			# context_dict["error2"] = userform.errors
			userform = UserForm()
			form = InfoForm()
			context_dict["form"] = form
			context_dict["userform"] = userform
			return render(request, 'app/register.html', context_dict)
	else :
		userform = UserForm()
		form = InfoForm()
		context_dict["userform"] = userform
		context_dict["form"] = form
		return render(request, 'app/register.html', context_dict)

def loginapp(request):
	context_dict = {}
	if request.method == 'POST':
		teamname = request.POST.get('teamname')
		password = request.POST.get('password')
		print(teamname)
		print(password)
		user = authenticate(username=teamname, password=password)
		if user:
			login(request, user)
			return HttpResponseRedirect('/app/')
		else:
			context_dict['invalid'] = "Invalid login details supplied."
			return render(request, 'app/login.html', context_dict)
	else :
		return render(request, 'app/login.html', context_dict)

def logoutapp(request):
	logout(request)
	return HttpResponseRedirect('/app/')

def foo1(string):
	x=0
	w=[-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6]
	print(string)
	substring_score=0
	for i in range(0,len(string)):
		substring_score=substring_score+(ord(string[x]))*w[x]
		x=x+1
	#foo2(substring_score)
	return substring_score

def foo2(program):
	s= len(program)
	print("len",s)
	k= s//13
	total_score = 0
	for i in range(0,k+1):
		print(i)
		total_score+=foo1(program[13*i:13*i+13])
	return total_score

def sumofP(program):
	s = len(program)
	return -3*122*s

def final(program):
	total_score=foo2(program)
	sumP = sumofP(program)
	fractional_score=total_score/sumP
	final_score= 100*fractional_score
	return final_score

def round2upload(request):
	context_dict = {}
	print("ehere")
	if request.user.is_authenticated():
		#print("ehere2")
		user = Info.objects.get(teamname=request.user)
		context_dict["username"]= user
		if request.method == 'POST':
			#print("ehere3")
			#print("ehere4")
			if request.FILES:
				#print("ehere5")
				codetype = request.POST.get('code')
				file = request.FILES['file']
				#print(file)
				if (codetype=="1"):
					user.ans1 = file
					user.save()
					print(user.ans1)
					with open(settings.MEDIA_ROOT+"/"+str(user.ans1)) as f:
						program = f.read()
						user.ans1score = final(program)
						user.round2score = user.ans1score+user.ans2score+user.ans3score+user.ans4score+user.ans5score
						user.save()
				elif (codetype=="2"):
					user.ans2 = file
					user.save()
					print(user.ans1)
					with open(settings.MEDIA_ROOT+"/"+str(user.ans2)) as f:
						program = f.read()
						user.ans2score = final(program)
						user.round2score = user.ans1score+user.ans2score+user.ans3score+user.ans4score+user.ans5score
						user.save()
				elif (codetype=="3"):
					user.ans3 = file
					user.save()
					print(user.ans1)
					with open(settings.MEDIA_ROOT+"/"+str(user.ans3)) as f:
						program = f.read()
						user.ans3score = final(program)
						user.round2score = user.ans1score+user.ans2score+user.ans3score+user.ans4score+user.ans5score
						user.save()
				elif (codetype=="4"):
					user.ans4 = file
					user.save()
					print(user.ans1)
					with open(settings.MEDIA_ROOT+"/"+str(user.ans4)) as f:
						program = f.read()
						user.ans4score = final(program)
						user.round2score = user.ans1score+user.ans2score+user.ans3score+user.ans4score+user.ans5score
						user.save()
				elif (codetype=="5"):
					user.ans5 = file
					user.save()
					print(user.ans1)
					with open(settings.MEDIA_ROOT+"/"+str(user.ans5)) as f:
						program = f.read()
						user.ans5score = final(program)
						user.round2score = user.ans1score+user.ans2score+user.ans3score+user.ans4score+user.ans5score
						user.save()
				else :
					print("No file selected")
			else :
				context_dict["error"] ="No file uploaded"
				return render(request, 'app/round2upload.html', context_dict)
		else:
			return render(request, 'app/round2upload.html', context_dict)
	else:
		return HttpResponseRedirect("/app/login/")
	return render(request, 'app/round2upload.html', context_dict)

def scorecard(request):
	context_dict = {}
	user = Info.objects.get(teamname=request.user)
	print(user)
	context_dict["username"] = user
	context_dict["totalscore"] = user.round1score + user.round2score
	return render(request, 'app/scorecard.html', context_dict)

def adminmanage(request):
	context_dict = {}
	return render(request, 'app/adminmanage.html', context_dict)

def endround2(request):
	context_dict = {}
	user = Info.objects.get(teamname=request.user)
	user.round2score = user.ans1score+user.ans2score+user.ans3score+user.ans4score+user.ans5score
	user.endround2 = 1
	user.save()
	return HttpResponseRedirect('/app/scorecard/')


	# if request.method == 'POST':
	#     form = InfoForm(request.POST,request.FILES)
	#     if form.is_valid():
	#         user = form.save(commit=False)
	#         user.save()
	#         context_dict["success"] = "Submitted!"
	#         form = InfoForm()
	#         context_dict["form"]= form
	#         return render(request, 'app/finalindex.html', context_dict)
	#         #return render(request, 'app/index.html', context_dict)
	#     else :
	#         context_dict["error"] = form.errors
	#         form = InfoForm()
	#         context_dict["form"] = form
	#         return render(request, 'app/finalindex.html', context_dict)
	#         return render(request,'app/index.html',context_dict)
	# else :
	#     form = InfoForm()
	#     context_dict["form"] = form
	#     return render(request, 'app/index.html', context_dict)

#=======
from django.shortcuts import render
from .models import Info,ForAdmin
from .forms import InfoForm,UserForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from anticoding import settings
def index(request):
	context_dict={}
	return render(request, 'app/finalindex.html', context_dict)

def ascii(request):
	context_dict={}
	return render(request, 'app/ascii.html', context_dict)
def round1(request):
	context_dict = {}
	fa = ForAdmin.objects.get(name="A")
	context_dict["admround1"] = fa.round1
	context_dict["admround2"] = fa.round2
	context_dict["admround3"] = fa.round3
	return render(request, 'app/round1.html', context_dict)

def round2(request):
	context_dict = {}
	fa = ForAdmin.objects.get(name="A")
	context_dict["admround1"] = fa.round1
	context_dict["admround2"] = fa.round2
	context_dict["admround3"] = fa.round3
	return render(request, 'app/round2.html', context_dict)

def register(request):
	context_dict = {}
	if request.method == 'POST':
		userform = UserForm(data=request.POST)
		form = InfoForm(data=request.POST)
		if userform.is_valid() and form.is_valid():
			user1 = userform.save(commit=False)
			user1.set_password(user1.password)
			user1.save()
			user = form.save(commit=False)
			user.teamname = user1
			user.save()
			context_dict["done"] = "Now you can login!"
			return render(request, 'app/register.html', context_dict)
			#return render(request, 'app/index.html', context_dict)
		else :
			# context_dict["error1"] = form.errors
			# context_dict["error2"] = userform.errors
			userform = UserForm()
			form = InfoForm()
			context_dict["form"] = form
			context_dict["userform"] = userform
			return render(request, 'app/register.html', context_dict)
	else :
		userform = UserForm()
		form = InfoForm()
		context_dict["userform"] = userform
		context_dict["form"] = form
		return render(request, 'app/register.html', context_dict)

def loginapp(request):
	context_dict = {}
	if request.method == 'POST':
		teamname = request.POST.get('teamname')
		password = request.POST.get('password')
		print(teamname)
		print(password)
		user = authenticate(username=teamname, password=password)
		if user:
			login(request, user)
			return HttpResponseRedirect('/app/')
		else:
			context_dict['invalid'] = "Invalid login details supplied."
			return render(request, 'app/login.html', context_dict)
	else :
		return render(request, 'app/login.html', context_dict)

def logoutapp(request):
	logout(request)
	return HttpResponseRedirect('/app/')

def foo1(string):
	x=0
	w=[-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6]
	print(string)
	substring_score=0
	for i in range(0,len(string)):
		substring_score=substring_score+(ord(string[x]))*w[x]
		x=x+1
	#foo2(substring_score)
	return substring_score

def foo2(program):
	s= len(program)
	print("len",s)
	k= s//13
	total_score = 0
	for i in range(0,k+1):
		print(i)
		total_score+=foo1(program[13*i:13*i+13])
	return total_score

def sumofP(program):
	s = len(program)
	return -3*122*s

def final(program):
	total_score=foo2(program)
	sumP = sumofP(program)
	fractional_score=total_score/sumP
	final_score= 100*fractional_score
	return final_score

def round2upload(request):
	context_dict = {}
	print("ehere")
	if request.user.is_authenticated():
		#print("ehere2")
		user = Info.objects.get(teamname=request.user)
		context_dict["username"]= user
		if request.method == 'POST':
			#print("ehere3")
			#print("ehere4")
			if request.FILES:
				#print("ehere5")
				codetype = request.POST.get('code')
				file = request.FILES['file']
				#print(file)
				if (codetype=="1"):
					user.ans1 = file
					user.save()
					print(user.ans1)
					with open(settings.MEDIA_ROOT+"/"+str(user.ans1)) as f:
						program = f.read()
						user.ans1score = final(program)
						user.round2score = user.ans1score+user.ans2score+user.ans3score+user.ans4score+user.ans5score
						user.save()
				elif (codetype=="2"):
					user.ans2 = file
					user.save()
					print(user.ans1)
					with open(settings.MEDIA_ROOT+"/"+str(user.ans2)) as f:
						program = f.read()
						user.ans2score = final(program)
						user.round2score = user.ans1score+user.ans2score+user.ans3score+user.ans4score+user.ans5score
						user.save()
				elif (codetype=="3"):
					user.ans3 = file
					user.save()
					print(user.ans1)
					with open(settings.MEDIA_ROOT+"/"+str(user.ans3)) as f:
						program = f.read()
						user.ans3score = final(program)
						user.round2score = user.ans1score+user.ans2score+user.ans3score+user.ans4score+user.ans5score
						user.save()
				elif (codetype=="4"):
					user.ans4 = file
					user.save()
					print(user.ans1)
					with open(settings.MEDIA_ROOT+"/"+str(user.ans4)) as f:
						program = f.read()
						user.ans4score = final(program)
						user.round2score = user.ans1score+user.ans2score+user.ans3score+user.ans4score+user.ans5score
						user.save()
				elif (codetype=="5"):
					user.ans5 = file
					user.save()
					print(user.ans1)
					with open(settings.MEDIA_ROOT+"/"+str(user.ans5)) as f:
						program = f.read()
						user.ans5score = final(program)
						user.round2score = user.ans1score+user.ans2score+user.ans3score+user.ans4score+user.ans5score
						user.save()
				else :
					print("No file selected")
			else :
				context_dict["error"] ="No file uploaded"
				return render(request, 'app/round2upload.html', context_dict)
		else:
			return render(request, 'app/round2upload.html', context_dict)
	else:
		return HttpResponseRedirect("/app/login/")
	return render(request, 'app/round2upload.html', context_dict)

def scorecard(request):
	context_dict = {}
	user = Info.objects.get(teamname=request.user)
	print(user)
	context_dict["username"] = user
	context_dict["totalscore"] = user.round1score + user.round2score
	return render(request, 'app/scorecard.html', context_dict)

def adminmanage(request):
	context_dict = {}
	return render(request, 'app/adminmanage.html', context_dict)

def endround2(request):
	context_dict = {}
	user = Info.objects.get(teamname=request.user)
	user.round2score = user.ans1score+user.ans2score+user.ans3score+user.ans4score+user.ans5score
	user.endround2 = 1
	user.save()
	return HttpResponseRedirect('/app/scorecard/')


	# if request.method == 'POST':
	#     form = InfoForm(request.POST,request.FILES)
	#     if form.is_valid():
	#         user = form.save(commit=False)
	#         user.save()
	#         context_dict["success"] = "Submitted!"
	#         form = InfoForm()
	#         context_dict["form"]= form
	#         return render(request, 'app/finalindex.html', context_dict)
	#         #return render(request, 'app/index.html', context_dict)
	#     else :
	#         context_dict["error"] = form.errors
	#         form = InfoForm()
	#         context_dict["form"] = form
	#         return render(request, 'app/finalindex.html', context_dict)
	#         return render(request,'app/index.html',context_dict)
	# else :
	#     form = InfoForm()
	#     context_dict["form"] = form
	#     return render(request, 'app/index.html', context_dict)

#>>>>>>> 76810e78b27247731da679ef829a38aa5a8475ff
