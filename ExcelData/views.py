from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import xlrd
import xlwt
import openpyxl
import urllib.request as urllib2
import json
import os
# Create your views here.
KEY = 'R3NMzr4vh39Viz8KgvvT3OdFEtzCHrTz'

def checkLOngLat(address):
	address = address.replace(' ', '+')
	url_loc = 'http://www.mapquestapi.com/geocoding/v1/address?key='+KEY+'&location='+address
	json_obj_loc = urllib2.urlopen(url_loc)
	data = json.load(json_obj_loc)
	# print (data)
	lati = str(data["results"][0]["locations"][0]["latLng"]["lat"])
	longi = str(data["results"][0]["locations"][0]["latLng"]["lng"])
	# print (lati)
	# print (longi)
	return lati, longi


def ExcelDataInput(request):
	if request.method == 'POST':
		excelfile = request.FILES["excel_file"]

		wb = openpyxl.load_workbook(excelfile)
		worksheet = wb["Sheet1"]
		print (worksheet)
		for idx, row in enumerate(worksheet.iter_rows()):
			# for cell in row:
			# print (row[1][0].value)
			lati, longi = checkLOngLat(row[0].value)
			worksheet["B"+str(idx+1)] = lati
			worksheet["C"+str(idx+1)] = longi

				# print (lati, longi)
		wb.save("Data.xlsx")
		with open("Data.xlsx", 'rb') as fh:
			response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename("Data.xlsx")
			return response
		# return HttpResponse("hello")
	else:
		return render(request, 'ExcelInput.html', {'message': "Thank you for Using"})
