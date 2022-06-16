from django.shortcuts import render, redirect
from CashBook1.models import *
from CashBook1.forms import *
from django.contrib import messages
import locale
import datetime


# Create your views here.
def blank_page(request):
    return render(request, "BlankPage.html")


def home(request):
    return redirect('/accounts/')

# Accounts
def accounts(request):
    data = Account.objects.all()
    account_cnt = data.count()
    return render(request, "Accounts.html", {'data': data, 'account_cnt': account_cnt})


def create_account(request):
    return render(request, "CreateAccount.html")


def add_account(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            try:
                obj = form.save()
                return redirect('/accounts/')
            except:
                return redirect('/accounts/')
        else:
            return redirect('/accounts/')
    else:
        return redirect('/accounts/')


def delete_account(request, id):
    try:
        a = Account.objects.get(account_id=id)
        a.delete()
        return redirect('/accounts/')
    except:
        return redirect('/accounts/')


def edit_account(request, id):
    try:
        data = Account.objects.get(account_id=id)
        return render(request, "EditAccount.html", {'data': data})
    except:
        return redirect('/accounts/')


def save_account(request):
    if request.method == "POST":
        a = Account.objects.get(account_id=request.POST['account_id'])
        form = AccountForm(request.POST, instance=a)
        if form.is_valid():
            try:
                form.save()
                return redirect('/accounts/')
            except:
                return redirect('/accounts/')
    else:
        return redirect('/accounts/')


def data_tables(request, id):
    try:
        cf_a = []
        cf_n = 0
        data = Data.objects.filter(account_id_id=id).order_by('data_date', 'data_id')
        for i in data:
            if i.cd == 1:
                cf_n = cf_n + i.amount
            else:
                cf_n = cf_n - i.amount
            cf_a.append(round(cf_n, 2))
        account = Account.objects.get(account_id=id)
        data_cnt = data.count()
        data = reversed(data)
        cf_a = reversed(cf_a)
        data = zip(data, cf_a)
        return render(request, "DataTables.html", {'data': data, 'account': account, 'data_cnt': data_cnt})
    except:
        return redirect('/accounts/')


def create_entry(request, id):
    try:
        obj = Account.objects.get(account_id=id)
        return render(request, "CreateEntry.html", {'id': id})
    except:
        return redirect('/accounts/')


def add_entry(request):
    if request.method == "POST":
        form = DataForm(request.POST)
        if form.is_valid():
            try:
                obj = form.save()
                print()
                return redirect('/data-tables/' + str(obj.account_id_id))
            except:
                return redirect('/data-tables/' + str(obj.account_id_id))
        else:
            print(form.errors)
            return redirect('/accounts/')
    else:
        return redirect('/accounts/')


def delete_entry(request, id):
    try:
        d = Data.objects.get(data_id=id)
        acc_id = d.account_id_id
        d.delete()
        return redirect('/data-tables/' + str(acc_id))
    except:
        return redirect('/accounts/')


def edit_entry(request, id):
    try:
        data = Data.objects.get(data_id=id)
        return render(request, "EditEntry.html", {'data': data, 'dat_id': id, 'acc_id': data.account_id_id})
    except:
        return redirect('/accounts/')


def save_entry(request):
    if request.method == "POST":
        d = Data.objects.get(data_id=request.POST['data_id'])
        form = DataForm(request.POST, instance=d)
        if form.is_valid():
            try:
                form.save()
                return redirect('/data-tables/' + str(request.POST['account_id']))
            except:
                return redirect('/accounts/')
    else:
        return redirect('/accounts/')


# Reports
def reports(request):
    return render(request, "Reports.html")


def show_reports(request):
    if request.method == "POST":
        a = Account.objects.all()
        sdate1 = request.POST['start_date']
        edate1 = request.POST['end_date']
        sortby = int(request.POST['sortby'])
        sdate = sdate1.split('-')
        edate = edate1.split('-')
        sdate = datetime.datetime(int(sdate[0]), int(sdate[1]), int(sdate[2]))
        edate = datetime.datetime(int(edate[0]), int(edate[1]), int(edate[2]))
        if sortby == 0:
            data = Data.objects.filter(data_date__range=[sdate1, edate1]).order_by('data_date', 'data_id')
        else:
            data = Data.objects.filter(data_date__range=[sdate1, edate1], account_id_id=sortby).order_by('data_date',
                                                                                                         'data_id')
        data_cnt = data.count()
        return render(request, "Reports.html",
                      {'data': data, 'data_cnt': data_cnt, 'sdate': sdate, 'edate': edate, 'accounts': a, 'sb': sortby})
    else:
        a = Account.objects.all()
        sdate = datetime.date.today().replace(day=1)
        edate = datetime.date.today()
        data = Data.objects.filter(data_date__range=[sdate, edate]).order_by('data_date', 'data_id')
        data_cnt = data.count()
        return render(request, "Reports.html",
                      {'data': data, 'data_cnt': data_cnt, 'sdate': sdate, 'edate': edate, 'accounts': a, 'sb': int(0)})
