from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.core.files.storage import FileSystemStorage
from .manualcode import Code
from tika import parser
import re
# Create your views here.
def index(request):
	temp1='splitter/sentence.html'
	temp2='splitter/output.html'
	x = Code() 
	if request.method == "POST":
		if request.POST.get('query2'):
			inp = request.POST.get('query2')
			inp2 = request.POST.get('query3')
			out,le=x.sen(inp,inp2)
			print(out)
			return render(request,temp2,context={'out':out , 'len':le})
		elif request.FILES['query1']:
			myfile = request.FILES['query1']
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			url = fs.url(filename)
			print(filename,url)
			url=re.sub("%20",' ',url)

			if ".pdf" in filename:
				raw = parser.from_file(url)
				inp = raw['content']
			else:
				with open(url, 'r') as file:
					inp = file.read()
			print(inp)
			inp2 = request.POST.get('query3')
			out,le=x.sen(inp,inp2)
			print(out)
			return render(request,temp2,context={'out':out , 'len':le})
	return render(request,temp1)

