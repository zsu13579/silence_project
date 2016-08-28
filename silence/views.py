# -*- coding: utf-8 -*-
from django.shortcuts import render,loader,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from models import *
from django.http import HttpResponse,request,HttpRequest
from django.template import Template,Context
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from forms import *
from datetime import datetime
from django.db.models import Sum,Avg
from django.utils.safestring import SafeString
import json
import logging

# Create your views here.

logger = logging.getLogger('silence.views')

def global_settings(request):
    try:
        userList = getpage(request, Testuserout.objects.all(), 10)
        callList = getpage(request, Callhistory.objects.filter(imsi=0000), 2)
        actinfo = Activateuserinfo.objects.get(id=1)
    except Exception as e:
        logger.error(e)
        actinfo = Activateuserinfo.objects.filter(id=1)
    return locals()

@login_required(redirect_field_name='',login_url='/login/')
def testuserlist(request):
    return render(request, 'testuserlist.html', locals())

# login
def do_login(request):
    try:
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                # 登录
                username = login_form.cleaned_data["username"]
                password = login_form.cleaned_data["password"]
                user = authenticate(username=username, password=password)
                if user is not None:
                    user.backend = 'django.contrib.auth.backends.ModelBackend' # 指定默认的登录验证方式
                    login(request, user)
                else:
                    return render(request, 'failure.html', {'reason': '登录验证失败'})
                return redirect(testuserlist)
            else:
                return render(request, 'failure.html', {'reason': login_form.errors})
        else:
            login_form = LoginForm()
    except Exception as e:
        logger.error(e)
    return render(request, 'login.html', locals())

@login_required(redirect_field_name='',login_url='/login/')
def searchresult(request):

    username = request.GET.get("username")
    provnm = request.GET.get("provnm")
    countrynm = request.GET.get("countrynm")
    isActivate = request.GET.get("isActivate")

    if (username and provnm and countrynm and isActivate):
        testuserlist = Testuserout.objects.filter(imsi=int(username), provnm=provnm, country_list__contains=countrynm,
                                                  issilence=int(isActivate))
    elif (username and provnm and countrynm):
        testuserlist = Testuserout.objects.filter(imsi=int(username), provnm=provnm,
                                                  country_list__contains=countrynm)
    elif (username and provnm and isActivate):
        testuserlist = Testuserout.objects.filter(imsi=int(username), provnm=provnm,
                                                  issilence=int(isActivate))
    elif (username and countrynm and isActivate):
        testuserlist = Testuserout.objects.filter(imsi=int(username),
                                                  country_list__contains=countrynm,
                                                  issilence=int(isActivate))
    elif (provnm and countrynm and isActivate):
        testuserlist = Testuserout.objects.filter(provnm=provnm,
                                                  country_list__contains=countrynm,
                                                  issilence=int(isActivate))
    elif (username and provnm):
        testuserlist = Testuserout.objects.filter(imsi=int(username), provnm=provnm)
    elif (username and countrynm):
        testuserlist = Testuserout.objects.filter(imsi=int(username), country_list__contains=countrynm)
    elif (username and isActivate):
        testuserlist = Testuserout.objects.filter(imsi=int(username), issilence=isActivate)
    elif (provnm and countrynm):
        testuserlist = Testuserout.objects.filter(provnm=provnm, country_list__contains=countrynm)
    elif (provnm and isActivate):
        testuserlist = Testuserout.objects.filter(issilence=int(isActivate), provnm=provnm)
    elif (countrynm and isActivate):
        testuserlist = Testuserout.objects.filter(issilence=int(isActivate), country_list__contains=countrynm)
    elif (username):
        testuserlist = Testuserout.objects.filter(imsi=int(username))
    elif (provnm):
        testuserlist = Testuserout.objects.filter(provnm=provnm)
    elif (countrynm):
        testuserlist = Testuserout.objects.filter(country_list__contains=countrynm)
    elif (isActivate):
        testuserlist = Testuserout.objects.filter(issilence=int(isActivate))
    else:
        testuserlist = Testuserout.objects.all()

    userList = getpage(request, testuserlist, 10)

    # call result search
    if (username):
        try:
            username = int(request.GET.get("username"))
        except Exception as e:
            logger.error(e)
        callList = getpage(request, Callhistory.objects.filter(imsi=username), 2)

    return render(request, 'testuserlist.html', locals())

@login_required(redirect_field_name='',login_url='/login/')
def callsearchresult(request):
    try:
        username = int(request.GET.get("username"))
    except Exception as e:
        logger.error(e)

    callList = getpage(request, Callhistory.objects.filter(imsi=username), 2)
    return render(request, 'testuserlist.html', locals())

@login_required(redirect_field_name='',login_url='/login/')
def savecall(request):

    try:
        callperson = request.GET.get('callperson')
        memo = request.GET.get('memo')
        imsi = int(request.GET.get('callimsi2'))
        newcall = Callhistory(username=callperson, calldate=datetime.now(), memo=memo, imsi=imsi)
        newcall.save()
    except Exception as e:
        logger.error(e)

    return redirect(request.META['HTTP_REFERER'])

@login_required(redirect_field_name='',login_url='/login/')
def calldetail(request):

    try:
        username = int(request.GET.get("username"))
    except Exception as e:
        logger.error(e)

    callList = getpage(request, Callhistory.objects.filter(imsi=username), 2)
    return render(request, 'testuserlist.html', locals())

@login_required(redirect_field_name='',login_url='/login/')
def dashboard(request):
    return render(request, 'dashboard.html', locals())

@login_required(redirect_field_name='',login_url='/login/')
def promotion(request):
    return render(request, 'promotion.html', locals())

def getpage(request, userList, k):
    paginator = Paginator(userList, k)
    page = request.GET.get('page')
    try:
        userList = paginator.page(page)
    except PageNotAnInteger:
        userList = paginator.page(1)
    except EmptyPage:
        userList = paginator.page(paginator.num_pages)
    return userList