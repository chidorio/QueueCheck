import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt

import core.firebase_script as core
import pytz
import pyrebase

#view
def index(request):
    context = {}
    print('='*10+'Index'+'='*10)
    # student = core.database.child("student").get()
    # for s in student.each():
    #     if request.session['idToken'] == s.key():
    #         context['name'] = s.val()['name']
    #         context['surname'] = s.val()['surname']
    #         context['email'] = s.val()['email']
    #         context['studentid'] = s.val()['studentid']
    #         context['name'] = s.val()['name']
    #         context['image'] = s.val()['url']
    # print(context)
    context = getbio(request.session['idToken'])
    return render(request, 'index.html', context=context)
#view
def login(request):
    print(request.session)
    return render(request, 'login.html')
#view
def profile(request):
    context = {}
    print('='*10+'Profile'+'='*10)
    context = getbio(request.session['idToken'])
    print(context)
    return render(request, 'profile.html', context)
#view
def editprofile(request):
    context = {}
    print('='*10+'editProfile'+'='*10)
    print(request.session['uid'])
    context = getbio(request.session['idToken'])
    print(context)
    return render(request, 'editProfile.html', context)

#controller
def validatelogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        user = core.auth_firebase.sign_in_with_email_and_password(email, password)
        print(user)
        request.session['uid'] = user['idToken']
        request.session['idToken'] = user['localId']

        return redirect('/core/index/', request)

#view
def testapi(request):
    return render(request, 'testapi.html')

#controller
def updateprofile(request):

    if request.method == 'POST':
        print('HERE')
        email = request.POST.get('email')
        phone = request.POST.get('phone_number')
        linecheck = request.POST.get('notificationline')
        emailcheck = request.POST.get('notificationemail')
        if str(linecheck) == 'None':
            print(str(linecheck), 0)
            check = 0
        elif str(linecheck) != 'None':
            check = 1
            print(str(linecheck), 1)
        data = {
            "linecheck":check,
            "email":email,
            "mobile":phone
        }

        #update firebase stu info here
        core.database.child("student").child(request.session['idToken']).update(data)
        print(email, phone, linecheck)
    return redirect(profile)

#controller
def logout(request):
    auth.logout(request)
    print('logout')
    return redirect(login)

#model
def getbio(key):
    context = {}
    student = core.database.child("student").child(key).get().val()
    context['name'] = student['name']
    context['surname'] = student['surname']
    context['email'] = student['email']
    context['studentid'] = student['studentid']
    context['image'] = student['url']
    context['mobile'] = student['mobile']
    context['line'] = student['linetoken']
    context['linecheck'] = student['linecheck']
    return context
#controller
@csrf_exempt
def api(request):
    response = {
        'input' : request.POST.get('username'),
        'output' : 'HELLO %s'% request.POST.get('username')
    }
    print(response)
    return JsonResponse(response, status=200)