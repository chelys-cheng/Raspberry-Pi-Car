# -*- coding: utf-8 -*-
from django.http import HttpResponse

def homepage(request):
	return HttpResponse("<a href='./control/'>进入小车控制端</a>")
