from collections import Counter
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool
import re


def getFileData(filename):


	# Store contents of resume in variable. Make all letters lowercase
	with open(filename, "r") as file:
		data = file.read().upper()

	# Remove all non-letter elements 
	data = re.sub("[^A-Z]","",data)
	# Summarize the data by letter and sort it alphabetically
	data = Counter(data)
	data = (sorted(data.items()))

	return data


def main():

	print("this is a test")
	filename ="resume_formatted.txt"
	output_file("resume_letter_count.html")


	data = getFileData(filename)
	x_axis = []
	y_axis = []

	for letter, frequency in data:
		x_axis.append(letter)
		y_axis.append(frequency)

	# print (x_axis)
	hover = HoverTool(tooltips=[
		("Frequency:", "@top")])
	p = figure(title="Letter frequency found in resume", x_range=x_axis, plot_width=1100, tools=[hover,"pan,wheel_zoom,box_zoom,reset"])
	p.vbar(x=x_axis, top=y_axis, width=0.5)
	show(p)



if __name__ == "__main__":
	main()