from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
	if request.method == "GET":
		return render_template("index.html")
	else:
		year = int(request.form.get("year"))
		classes = request.form.get("class")
		week = request.form.get("week")
		day = request.form.get("day")
		if classes.isalpha() == True:#jh class timetable
			classes = ord(classes)#work on this
			if classes<64 or 77<=classes<=96 or classes>=109:
				error = "Invalid input!" #error for invalid jh input
				return render_template("index.html", error=error)
		elif int(classes)<=10 or 13<=int(classes)<=20 or 23<=int(classes)<=30 or 38<=int(classes)<=40 or 49<=int(classes): #error for invalid sh input
			error = "Invalid input!"
			return render_template("index.html", error=error)
		else:
			return redirect(url_for('display', year=year, classes=classes, week=week, day=day))


@app.route('/display', methods=["GET", "POST"])
def display():
	year = int(request.args.get('year', None))
	classes = int(request.args.get('classes', None))
	week = request.args.get('week', None)
	day = request.args.get('day', None)
	data=[]
	headers = "Time", "Subject", "Location"
	if classes*year == 175: #sh 5c35 class timetable
		if week == "o":
			if int(day) == 1:
				fin = open("5C35_O1.txt","r")
				datatable = [line.split() for line in fin.read().splitlines()]
				widths = [max(len(value) for value in col) for col in zip(*(datatable + [headers]))]
				fin.close()
			elif int(day) == 2:
				fin = open("5C35_O+E2.txt","r")
				datatable = [line.split() for line in fin.read().splitlines()]
				widths = [max(len(value) for value in col) for col in zip(*(datatable + [headers]))]
				fin.close()
			elif int(day) == 3:
				fin = open("5C35_O+E3.txt","r")
				datatable = [line.split() for line in fin.read().splitlines()]
				widths = [max(len(value) for value in col) for col in zip(*(datatable + [headers]))]
				fin.close()
			elif int(day) == 4:
				fin = open("5C35_O+E4.txt","r")
				datatable = [line.split() for line in fin.read().splitlines()]
				widths = [max(len(value) for value in col) for col in zip(*(datatable + [headers]))]
				fin.close()
			else:
				fin = open("5C35_O+E5.txt","r")
				datatable = [line.split() for line in fin.read().splitlines()]
				widths = [max(len(value) for value in col) for col in zip(*(datatable + [headers]))]
				fin.close()
		else:
			if int(day) == 1:
				fin = open("5C35_E1.txt", "r")
				datatable = [line.split() for line in fin.read().splitlines()]
				widths = [max(len(value) for value in col) for col in zip(*(datatable + [headers]))]
				fin.close()
			elif int(day) == 2:
				fin = open("5C35_O+E2.txt", "r")
				datatable = [line.split() for line in fin.read().splitlines()]
				widths = [max(len(value) for value in col) for col in zip(*(datatable + [headers]))]
				fin.close()
			elif int(day) == 3:
				fin = open("5C35_O+E3.txt", "r")
				datatable = [line.split() for line in fin.read().splitlines()]
				widths = [max(len(value) for value in col) for col in zip(*(datatable + [headers]))]
				fin.close()
			elif int(day) == 4:
				fin = open("5C35_O+E4.txt", "r")
				datatable = [line.split() for line in fin.read().splitlines()]
				widths = [max(len(value) for value in col) for col in zip(*(datatable + [headers]))]
				fin.close()
			else:
				fin = open("5C35_O+E5.txt", "r")
				datatable = [line.split() for line in fin.read().splitlines()]
				widths = [max(len(value) for value in col) for col in zip(*(datatable + [headers]))]
				fin.close()
	format_spec = '{:{widths[0]}}  {:<{widths[1]}}  {:<{widths[2]}}'
	table = format_spec.format(*headers, widths=widths)
	for fields in datatable:
		lines = format_spec.format(*fields, widths=widths)
		data.append(lines)
	print(data)
	return render_template("display.html", table=table, data=data)



app.run(host='0.0.0.0', port=8080)
