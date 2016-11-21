from django.shortcuts import render
from django.http import HttpResponse
import os, filecmp
import shlex, subprocess
from collections import Counter
from django.http import JsonResponse
from wsgiref.util import FileWrapper
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def history(request):
	return render(request, 'history.html')

def roadmap(request):
	return render(request, 'roadmap.html')

def checkfont(request):
	return render(request, 'check_font.html')

def assamese(request):
	if request.method == 'POST':
		if request.is_ajax():
			module_dir = os.path.dirname(__file__)
			file_path = os.path.join(module_dir, 'static/lang/as_IN/font/data/master_as.txt')
			img_path = os.path.join(module_dir, 'static/lang/as_IN/font/')
			font_path = os.path.join(module_dir, 'static/fonts/lohit-assamese/Lohit-Assamese.ttf')
			file = open(file_path)
			data = file.read()
			length = data.count('\n')
			file.close()
			file = open(file_path)
			data_code = []
			os.chdir(img_path)
			for i in range(length):
				line = file.readline()
				st = line.strip('\n')
				sp = st.split(',')
				name = sp[1].strip('image/').strip(".svg")
				os.system('hb-view %s %s --output-format=svg --output-file=%s.svg' % (font_path, sp[2], name))
				img1 = os.path.join(module_dir, 'static/lang/as_IN/font/%s' % sp[1])
				img2 = os.path.join(module_dir, 'static/lang/as_IN/font/%s.svg' % name)
				if filecmp.cmp(img1,img2)==True:
					sp.append('Matched')
				else:
					sp.append('Not Matched')
				data_code.append(sp)
				os.remove('%s.svg' % name)
			name = 'Tenstormavi'
			return JsonResponse({'data_code': data_code, 'name': name})
		return render(request, 'test.html')
	else:
		module_dir = os.path.dirname(__file__)
		file_path = os.path.join(module_dir, 'static/lang/as_IN/font/data/master_as.txt')
		file = open(file_path)
		data = file.read()
		length = data.count('\n')
		file.close()
		file = open(file_path)
		data_code = []
		for i in range(length):
			line = file.readline()
			st = line.strip('\n')
			sp = st.split(',')
			data_code.append(sp)
		return render(request, 'test.html', {'data_code': data_code})
        

"""def assamese(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/as_IN/font/data/master_as.txt')
	img_path = os.path.join(module_dir, 'static/lang/as_IN/font/')
	font_path = os.path.join(module_dir, 'static/fonts/lohit-assamese/Lohit-Assamese.ttf')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	os.chdir(img_path)
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		name = sp[1].strip('image/').strip(".svg")
		os.system('hb-view %s %s --output-format=svg --output-file=%s.svg' % (font_path, sp[2], name))
		img1 = os.path.join(module_dir, 'static/lang/as_IN/font/%s' % sp[1])
		img2 = os.path.join(module_dir, 'static/lang/as_IN/font/%s.svg' % name)
		if filecmp.cmp(img1,img2)==True:
			sp.append('Matched')
		else:
			sp.append('Not Matched')
		data_code.append(sp)
		os.remove('%s.svg' % name)
	return render(request, 'assamese.html', {'data_code': data_code})"""

def assamese_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/as_IN/font/data/codepoint/master_as_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'as_codepoint.html', {'data_code': data_code[1:]})

def assamese_gsub(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/as_IN/font/data/gsub/master_gsub_as_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gsub = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gsub.append(sp)
	return render(request, 'as_gsub.html', {'data_gsub': data_gsub[1:]})

def assamese_gpos(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/as_IN/font/data/gpos/master_gpos_as_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gpos = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gpos.append(sp)
	return render(request, 'as_gpos.html', {'data_gpos': data_gpos[1:]})

def bengali(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/bn_IN/font/data/master_bn.txt')
	img_path = os.path.join(module_dir, 'static/lang/bn_IN/font/')
	font_path = os.path.join(module_dir, 'static/fonts/lohit-bengali/Lohit-Bengali.ttf')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	os.chdir(img_path)
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		name = sp[1].strip('image/').strip(".svg")
		os.system('hb-view %s %s --output-format=svg --output-file=%s.svg' % (font_path, sp[2], name))
		img1 = os.path.join(module_dir, 'static/lang/bn_IN/font/%s' % sp[1])
		img2 = os.path.join(module_dir, 'static/lang/bn_IN/font/%s.svg' % name)
		if filecmp.cmp(img1,img2)==True:
			sp.append('Matched')
		else:
			sp.append('Not Matched')
		data_code.append(sp)
		os.remove('%s.svg' % name)
	return render(request, 'bengali.html', {'data_code': data_code})

def bengali_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/bn_IN/font/data/codepoint/master_bn_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'bn_codepoint.html', {'data_code': data_code[1:]})

def bengali_gsub(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/bn_IN/font/data/gsub/master_gsub_bn_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gsub = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gsub.append(sp)
	return render(request, 'bn_gsub.html', {'data_gsub': data_gsub[1:]})

def bengali_gpos(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/bn_IN/font/data/gpos/master_gpos_bn_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gpos = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gpos.append(sp)
	return render(request, 'bn_gpos.html', {'data_gpos': data_gpos[1:]})

def german(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/de_DE/font/data/codepoint/master_de_DE.txt')
	img_path = os.path.join(module_dir, 'static/lang/de_DE/font/')
	font_path = os.path.join(module_dir, 'static/fonts/dejavu/DejaVuSans.ttf')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	pdf_data = [['<b>Codepoint</b>','<b>Character</b>','<b>Description</b>','<b>Result</b>']]
	os.chdir(img_path)
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		name = sp[1].strip('image/').strip(".svg")
		os.system('hb-view %s %s --output-format=svg --output-file=%s.svg' % (font_path, sp[2], name))
		img1 = os.path.join(module_dir, 'static/lang/de_DE/font/%s' % sp[1])
		img2 = os.path.join(module_dir, 'static/lang/de_DE/font/%s.svg' % name)
		if filecmp.cmp(img1,img2)==True:
			sp.append('Matched')
		else:
			sp.append('Not Matched')
		pd = sp[:]
		pd.pop(1)
		#pd.insert(0, i)
		pdf_data.append(pd)
		data_code.append(sp)
		os.remove('%s.svg' % name)
	doc = SimpleDocTemplate("german-report.pdf", pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
	doc.pagesize = landscape(A4)
	elements = []
	style = TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
                       ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
                       ('VALIGN',(0,0),(0,-1),'TOP'),
                       ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                       ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                       ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
                       ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ])
	s = getSampleStyleSheet()
	s = s["BodyText"]
	s.wordWrap = 'CJK'
	data2 = [[Paragraph(cell, s) for cell in row] for row in pdf_data]
	t = Table(data2)
	t.setStyle(style)
	styles = getSampleStyleSheet()
	p = Paragraph("<u>Report</u>", styles["title"])
	elements.append(p)
	elements.append(t)
	doc.build(elements)
	return render(request, 'german.html', {'data_code': data_code})

def german_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/de_DE/font/data/codepoint/master_de_DE.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'de_codepoint.html', {'data_code': data_code})

def german_gsub(request):
	return render(request, 'de_gsub.html')

def german_gpos(request):
	return render(request, 'de_gpos.html')

def german_pdf(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/de_DE/font/german-report.pdf')
	file = open(file_path, "r")
	response = HttpResponse(FileWrapper(file), content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=german-report.pdf'
	file.close()
	return response

def gujarati(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/gu_IN/font/data/master_gu.txt')
	img_path = os.path.join(module_dir, 'static/lang/gu_IN/font/')
	font_path = os.path.join(module_dir, 'static/fonts/lohit-gujarati/Lohit-Gujarati.ttf')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	os.chdir(img_path)
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		name = sp[1].strip('image/').strip(".svg")
		os.system('hb-view %s %s --output-format=svg --output-file=%s.svg' % (font_path, sp[2], name))
		img1 = os.path.join(module_dir, 'static/lang/gu_IN/font/%s' % sp[1])
		img2 = os.path.join(module_dir, 'static/lang/gu_IN/font/%s.svg' % name)
		if filecmp.cmp(img1,img2)==True:
			sp.append('Matched')
		else:
			sp.append('Not Matched')
		data_code.append(sp)
		os.remove('%s.svg' % name)
	return render(request, 'gujarati.html', {'data_code': data_code})

def gujarati_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/gu_IN/font/data/codepoint/master_gu_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'gu_codepoint.html', {'data_code': data_code[1:]})

def gujarati_gsub(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/gu_IN/font/data/gsub/master_gsub_gu_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gsub = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gsub.append(sp)
	return render(request, 'gu_gsub.html', {'data_gsub': data_gsub[1:]})

def gujarati_gpos(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/gu_IN/font/data/gpos/master_gpos_gu_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gpos = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gpos.append(sp)
	return render(request, 'gu_gpos.html', {'data_gpos': data_gpos[1:]})

def hindi(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/hi_IN/font/data/master_hi.txt')
	img_path = os.path.join(module_dir, 'static/lang/hi_IN/font/')
	font_path = os.path.join(module_dir, 'static/fonts/lohit-devanagari/Lohit-Devanagari.ttf')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	os.chdir(img_path)
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		name = sp[1].strip('image/').strip(".svg")
		os.system('hb-view %s %s --output-format=svg --output-file=%s.svg' % (font_path, sp[2], name))
		img1 = os.path.join(module_dir, 'static/lang/hi_IN/font/%s' % sp[1])
		img2 = os.path.join(module_dir, 'static/lang/hi_IN/font/%s.svg' % name)
		if filecmp.cmp(img1,img2)==True:
			sp.append('Matched')
		else:
			sp.append('Not Matched')
		data_code.append(sp)
		os.remove('%s.svg' % name)
	return render(request, 'hindi.html', {'data_code': data_code})

def hindi_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/hi_IN/font/data/codepoint/master_hi_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'hi_codepoint.html', {'data_code': data_code[1:]})

def hindi_gsub(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/hi_IN/font/data/gsub/master_gsub_hi_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gsub = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gsub.append(sp)
	return render(request, 'hi_gsub.html', {'data_gsub': data_gsub[1:]})

def hindi_gpos(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/hi_IN/font/data/gpos/master_gpos_hi_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gpos = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gpos.append(sp)
	return render(request, 'hi_gpos.html', {'data_gpos': data_gpos[1:]})

def kannada(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/kn_IN/font/data/master_kn.txt')
	img_path = os.path.join(module_dir, 'static/lang/kn_IN/font/')
	font_path = os.path.join(module_dir, 'static/fonts/lohit-kannada/Lohit-Kannada.ttf')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	os.chdir(img_path)
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		name = sp[1].strip('image/').strip(".svg")
		os.system('hb-view %s %s --output-format=svg --output-file=%s.svg' % (font_path, sp[2], name))
		img1 = os.path.join(module_dir, 'static/lang/kn_IN/font/%s' % sp[1])
		img2 = os.path.join(module_dir, 'static/lang/kn_IN/font/%s.svg' % name)
		if filecmp.cmp(img1,img2)==True:
			sp.append('Matched')
		else:
			sp.append('Not Matched')
		data_code.append(sp)
		os.remove('%s.svg' % name)
	return render(request, 'kannada.html', {'data_code': data_code})

def kannada_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/kn_IN/font/data/codepoint/master_kn_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'kn_codepoint.html', {'data_code': data_code[1:]})

def kannada_gsub(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/kn_IN/font/data/gsub/master_gsub_kn_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gsub = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gsub.append(sp)
	return render(request, 'kn_gsub.html', {'data_gsub': data_gsub[1:]})

def kannada_gpos(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/kn_IN/font/data/gpos/master_gpos_kn_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gpos = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gpos.append(sp)
	return render(request, 'kn_gpos.html', {'data_gpos': data_gpos[1:]})

def maithili(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/mai_IN/font/data/master_mai.txt')
	img_path = os.path.join(module_dir, 'static/lang/mai_IN/font/')
	font_path = os.path.join(module_dir, 'static/fonts/lohit-devanagari/Lohit-Devanagari.ttf')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	os.chdir(img_path)
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		name = sp[1].strip('image/').strip(".svg")
		os.system('hb-view %s %s --output-format=svg --output-file=%s.svg' % (font_path, sp[2], name))
		img1 = os.path.join(module_dir, 'static/lang/mai_IN/font/%s' % sp[1])
		img2 = os.path.join(module_dir, 'static/lang/mai_IN/font/%s.svg' % name)
		if filecmp.cmp(img1,img2)==True:
			sp.append('Matched')
		else:
			sp.append('Not Matched')
		data_code.append(sp)
		os.remove('%s.svg' % name)
	return render(request, 'maithili.html', {'data_code': data_code})

def maithili_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/mai_IN/font/data/codepoint/master_mai_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'mai_codepoint.html', {'data_code': data_code[1:]})

def maithili_gsub(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/mai_IN/font/data/gsub/master_gsub_mai_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gsub = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gsub.append(sp)
	return render(request, 'mai_gsub.html', {'data_gsub': data_gsub[1:]})

def maithili_gpos(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/mai_IN/font/data/gpos/master_gpos_mai_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gpos = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gpos.append(sp)
	return render(request, 'mai_gpos.html', {'data_gpos': data_gpos[1:]})

def malayalam(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ml_IN/font/data/master_ml.txt')
	img_path = os.path.join(module_dir, 'static/lang/ml_IN/font/')
	font_path = os.path.join(module_dir, 'static/fonts/smc/Meera.ttf')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	os.chdir(img_path)
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		name = sp[1].strip('image/').strip(".svg")
		os.system('hb-view %s %s --output-format=svg --output-file=%s.svg' % (font_path, sp[2], name))
		img1 = os.path.join(module_dir, 'static/lang/ml_IN/font/%s' % sp[1])
		img2 = os.path.join(module_dir, 'static/lang/ml_IN/font/%s.svg' % name)
		if filecmp.cmp(img1,img2)==True:
			sp.append('Matched')
		else:
			sp.append('Not Matched')
		data_code.append(sp)
		os.remove('%s.svg' % name)
	return render(request, 'malayalam.html', {'data_code': data_code})

def malayalam_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ml_IN/font/data/codepoint/master_ml_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'ml_codepoint.html', {'data_code': data_code[1:]})

def malayalam_gsub(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ml_IN/font/data/gsub/master_gsub_ml_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gsub = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gsub.append(sp)
	return render(request, 'ml_gsub.html', {'data_gsub': data_gsub[1:]})

def malayalam_gpos(request):
	return render(request, 'ml_gpos.html')

def marathi(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/mr_IN/font/data/master_mr.txt')
	img_path = os.path.join(module_dir, 'static/lang/mr_IN/font/')
	font_path = os.path.join(module_dir, 'static/fonts/lohit-devanagari/Lohit-Devanagari.ttf')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	os.chdir(img_path)
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		name = sp[1].strip('image/').strip(".svg")
		os.system('hb-view %s %s --output-format=svg --output-file=%s.svg' % (font_path, sp[2], name))
		img1 = os.path.join(module_dir, 'static/lang/mr_IN/font/%s' % sp[1])
		img2 = os.path.join(module_dir, 'static/lang/mr_IN/font/%s.svg' % name)
		if filecmp.cmp(img1,img2)==True:
			sp.append('Matched')
		else:
			sp.append('Not Matched')
		data_code.append(sp)
		os.remove('%s.svg' % name)
	return render(request, 'marathi.html', {'data_code': data_code})

def marathi_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/mr_IN/font/data/codepoint/master_mr_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'mr_codepoint.html', {'data_code': data_code[1:]})

def marathi_gsub(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/mr_IN/font/data/gsub/master_gsub_mr_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gsub = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gsub.append(sp)
	return render(request, 'mr_gsub.html', {'data_gsub': data_gsub[1:]})

def marathi_gpos(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/mr_IN/font/data/gpos/master_gpos_mr_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gpos = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gpos.append(sp)
	return render(request, 'mr_gpos.html', {'data_gpos': data_gpos[1:]})

def odia(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/or_IN/font/data/master_or.txt')
	img_path = os.path.join(module_dir, 'static/lang/or_IN/font/')
	font_path = os.path.join(module_dir, 'static/fonts/lohit-odia/Lohit-Odia.ttf')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	os.chdir(img_path)
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		name = sp[1].strip('image/').strip(".svg")
		os.system('hb-view %s %s --output-format=svg --output-file=%s.svg' % (font_path, sp[2], name))
		img1 = os.path.join(module_dir, 'static/lang/or_IN/font/%s' % sp[1])
		img2 = os.path.join(module_dir, 'static/lang/or_IN/font/%s.svg' % name)
		if filecmp.cmp(img1,img2)==True:
			sp.append('Matched')
		else:
			sp.append('Not Matched')
		data_code.append(sp)
		os.remove('%s.svg' % name)
	return render(request, 'odia.html', {'data_code': data_code})

def odia_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/or_IN/font/data/codepoint/master_or_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'or_codepoint.html', {'data_code': data_code[1:]})

def odia_gsub(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/or_IN/font/data/gsub/master_gsub_or_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gsub = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gsub.append(sp)
	return render(request, 'or_gsub.html', {'data_gsub': data_gsub[1:]})

def odia_gpos(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/or_IN/font/data/gpos/master_gpos_or_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gpos = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gpos.append(sp)
	return render(request, 'or_gpos.html', {'data_gpos': data_gpos[1:]})

def punjabi(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/pa_IN/font/data/master_pa.txt')
	img_path = os.path.join(module_dir, 'static/lang/pa_IN/font/')
	font_path = os.path.join(module_dir, 'static/fonts/lohit-gurmukhi/Lohit-Gurmukhi.ttf')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	os.chdir(img_path)
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		name = sp[1].strip('image/').strip(".svg")
		os.system('hb-view %s %s --output-format=svg --output-file=%s.svg' % (font_path, sp[2], name))
		img1 = os.path.join(module_dir, 'static/lang/pa_IN/font/%s' % sp[1])
		img2 = os.path.join(module_dir, 'static/lang/pa_IN/font/%s.svg' % name)
		if filecmp.cmp(img1,img2)==True:
			sp.append('Matched')
		else:
			sp.append('Not Matched')
		data_code.append(sp)
		os.remove('%s.svg' % name)
	return render(request, 'punjabi.html', {'data_code': data_code})

def punjabi_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/pa_IN/font/data/codepoint/master_pa_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'pa_codepoint.html', {'data_code': data_code[1:]})

def punjabi_gsub(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/pa_IN/font/data/gsub/master_gsub_pa_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gsub = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gsub.append(sp)
	return render(request, 'pa_gsub.html', {'data_gsub': data_gsub[1:]})

def punjabi_gpos(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/pa_IN/font/data/gpos/master_gpos_pa_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gpos = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gpos.append(sp)
	return render(request, 'pa_gpos.html', {'data_gpos': data_gpos[1:]})

def tamil(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ta_IN/font/data/master_ta.txt')
	img_path = os.path.join(module_dir, 'static/lang/ta_IN/font/')
	font_path = os.path.join(module_dir, 'static/fonts/lohit-tamil/Lohit-Tamil.ttf')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	os.chdir(img_path)
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		name = sp[1].strip('image/').strip(".svg")
		os.system('hb-view %s %s --output-format=svg --output-file=%s.svg' % (font_path, sp[2], name))
		img1 = os.path.join(module_dir, 'static/lang/ta_IN/font/%s' % sp[1])
		img2 = os.path.join(module_dir, 'static/lang/ta_IN/font/%s.svg' % name)
		if filecmp.cmp(img1,img2)==True:
			sp.append('Matched')
		else:
			sp.append('Not Matched')
		data_code.append(sp)
		os.remove('%s.svg' % name)
	return render(request, 'tamil.html', {'data_code': data_code})

def tamil_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ta_IN/font/data/codepoint/master_ta_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'ta_codepoint.html', {'data_code': data_code[1:]})

def tamil_gsub(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ta_IN/font/data/gsub/master_gsub_ta_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gsub = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gsub.append(sp)
	return render(request, 'ta_gsub.html', {'data_gsub': data_gsub[1:]})

def tamil_gpos(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/ta_IN/font/data/gpos/master_gpos_ta_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gpos = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gpos.append(sp)
	return render(request, 'ta_gpos.html', {'data_gpos': data_gpos[1:]})

def telugu(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/te_IN/font/data/master_te.txt')
	img_path = os.path.join(module_dir, 'static/lang/te_IN/font/')
	font_path = os.path.join(module_dir, 'static/fonts/lohit-telugu/Lohit-Telugu.ttf')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	os.chdir(img_path)
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		name = sp[1].strip('image/').strip(".svg")
		os.system('hb-view %s %s --output-format=svg --output-file=%s.svg' % (font_path, sp[2], name))
		img1 = os.path.join(module_dir, 'static/lang/te_IN/font/%s' % sp[1])
		img2 = os.path.join(module_dir, 'static/lang/te_IN/font/%s.svg' % name)
		if filecmp.cmp(img1,img2)==True:
			sp.append('Matched')
		else:
			sp.append('Not Matched')
		data_code.append(sp)
		os.remove('%s.svg' % name)
	return render(request, 'telugu.html', {'data_code': data_code})

def telugu_codepoint(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/te_IN/font/data/codepoint/master_te_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_code = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_code.append(sp)
	return render(request, 'te_codepoint.html', {'data_code': data_code[1:]})

def telugu_gsub(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/te_IN/font/data/gsub/master_gsub_te_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gsub = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gsub.append(sp)
	return render(request, 'te_gsub.html', {'data_gsub': data_gsub[1:]})

def telugu_gpos(request):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'static/lang/te_IN/font/data/gpos/master_gpos_te_IN.txt')
	file = open(file_path)
	data = file.read()
	length = data.count('\n')
	file.close()
	file = open(file_path)
	data_gpos = []
	for i in range(length):
		line = file.readline()
		st = line.strip('\n')
		sp = st.split(',')
		data_gpos.append(sp)
	return render(request, 'te_gpos.html', {'data_gpos': data_gpos[1:]})

