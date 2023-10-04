from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
import pandas as pd
from django.db.models import Q


def Booklistview(request):
    book_list = BarCodeModel.objects.all()
    context = {'book_list': book_list}
    return render(request, 'catlog/book_dtail.html', context)


def BooklistviewTest(request):
    if 'q' in request.GET:
        q = request.GET['q']
        book_list = BarCodeModel.objects.filter(isbn__icontains=q)
    else:
        book_list = BarCodeModel.objects.all()
    context = {'book_list': book_list}
    return render(request, 'catlog/grid_test.html', context)


@api_view(['GET'])
def addData(request):
    data = pd.read_excel('f:/test.xlsx')
    print(len(data))
    for i in range(0, len(data)):
        s = BarCodeModel()
        s.title = data.iloc[i][0]
        s.isbn = data.iloc[i][1]
        print(s)
        s.save()
    return Response('request.data')
