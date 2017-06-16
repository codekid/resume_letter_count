# ================================================================================================
# Script Name 	: letter_count.py
# Purpose		: Summarize the frequency of each letter and output the results in bar chart form
# 				  Using the bokeh charting library.
# Author		: Kadeem
# ================================================================================================
from collections import Counter
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool
import re

# Get the resume data from a file, change all letters to uppercase and remove all characters that are not letters
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

	filename ="resume_formatted.txt"
	output_file("resume_letter_count.html")

	data = getFileData(filename)

	x_axis = []
	y_axis = []

	# Populate the x and y axis with data
	for letter, frequency in data:
		x_axis.append(letter)
		y_axis.append(frequency)


	# hover allows the value to be shown on mouse over of each element in the chart  
	hover = HoverTool(tooltips=[
		("Frequency:", "@top")])
	
	# Prepare the chart
	p = figure(title="Letter frequency found in resume", x_range=x_axis, plot_width=1100, tools=[hover,"pan,wheel_zoom,box_zoom,reset"])
	p.vbar(x=x_axis, top=y_axis, width=0.5)
	
	show(p)



if __name__ == "__main__":
	main()