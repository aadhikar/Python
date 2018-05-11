# -*- coding: utf-8 -*-

#import statements
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import Image
import csv

data_file = 'attendees.csv'

def import_dataset(file):
	attendee_data = csv.reader(open(file, 'rb'))
	for row in attendee_data:
		first_name = row[2]
		middle_name = row[3]
		last_name = row[4]
		percentile = row[26][:-1]
		pdf_file_name = first_name+'_'+middle_name+'_'+last_name+'_'+percentile+'.pdf'
		print pdf_file_name
		generate_certificate(first_name, middle_name, last_name, percentile, pdf_file_name)

def generate_certificate(first_name, middle_name, last_name, percentile, pdf_file_name):
	attendee_name = first_name+' '+middle_name+' '+last_name
	doc = canvas.Canvas(pdf_file_name, pagesize=landscape(letter))
	
	# Header text
	doc.drawCentredString(415, 500, 'Certification Of Completion')
	
	doc.drawCentredString(415, 450, 'This certificate is presented to')
	
	# Attendee name
	doc.drawCentredString(415, 400, attendee_name)
	
	# Attendee percentile
	doc.drawCentredString(415, 350, 'For scoring '+percentile+'% in finals')
	
	# Seal for certificate
	seal = 'seal.jpg'
	doc.drawImage(seal, 350, 50, width=100, height=100)
	
	doc.showPage()
	
	doc.save()

def main():
	import_dataset(data_file)


if __name__ == '__main__':
	main();