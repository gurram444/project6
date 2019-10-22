from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas
import csv
# Create your views here.
data="""<table><tr><th>eid</th><th>ename</th><th>esal</th></tr>
<tr><td>1001</td><td>scott</td><td>2000</td></tr>
<tr><td>1002</td><td>blake</td><td>4000</td></tr>
<tr><td>1003</td><td>miller</td><td>1500</td></tr></table>"""

def CSVview(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;\'filename="myfile.csv"'
    writer=csv.writer(response)
    writer.writerow(['firstrow','foo','bar','baz'])
    writer.writerow(['secondrow','A','B','C','Testing','here is a quote'])
    return response

def pdfview(request):
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='fvattachment; filename="myfile.pdf"'
    p=canvas.Canvas(response)
    p.drawString(100,100,'hello world')
    p.showPage()
    p.save()
    return response
def htmlview(request):
    return HttpResponse(data,content_type='text/html')
def xmlview(request):
    return HttpResponse(data,content_type="appalication/pdf")