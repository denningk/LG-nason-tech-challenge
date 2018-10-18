# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader

from .models import Customer, Package

# Create your views here.

def landing(request):
    """landing page that lists all of the packages"""
    customerList = Customer.objects.values()
    packageList = Package.objects.values()
    context = {
        'customerList': customerList,
        'packageList': packageList,
    }
    return render(request, 'html/landing.html', context)
    

def order(request):
    """order page that displays a form to order a package"""
    context = {}
    return render(request, 'html/order.html', context)

def handle(request):
    """handles saving data from form into database"""
    if request.method == 'POST':
        customerName = request.POST.get('namefield').lower()
        order = request.POST.get('orderfield').lower()
        
        if customerName != '' and order != '':

            try:
                existingCustomer = Customer.objects.get(name=customerName)
                #if customer in database already
                o = Package(name=order, customer_id=existingCustomer.id)
                o.save()

            except Customer.DoesNotExist:
                #if customer not yet in database
                n = Customer(name=customerName)
                n.save()
                o = Package(name=order, customer_id=n.id)
                o.save()
                
    #redirects to landing page to show the updated customer in database       
    return HttpResponseRedirect('/main/landing/')
