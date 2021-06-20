# Importing the matplotlb.pyplot
import matplotlib.pyplot as plt

# Add export function to PDF
# Import basic data re: Activities & Times (Name, Start, Length, Variance)
# Print this data to the PDF @ top
# Add pie chart to calculate % of total time for each task 

# Declaring a figure "gnt"
fig, gnt = plt.subplots()

# Declaring axis limits
Y_MIN = 0 
Y_MAX = 0
X_MIN = 0 
X_MAX = 0 

# Setting Y-axis limits
gnt.set_ylim(Y_MIN, Y_MAX)

# Setting X-axis limits
gnt.set_xlim(X_MIN, X_MAX)

# Setting labels for x-axis and y-axis
gnt.set_xlabel('Date')
gnt.set_ylabel('Activity')

# Setting ticks on y-axis
gnt.set_yticks([15, 25, 35])
# Labelling tickes of y-axis
gnt.set_yticklabels(['1', '2', '3'])

# Setting graph attribute
gnt.grid(True)

# Declaring a bar in schedule
gnt.broken_barh([(40, 50)], (30, 9), facecolors =('tab:orange'))

# Declaring multiple bars in at same level and same width
gnt.broken_barh([(110, 10), (150, 10)], (10, 9),
						facecolors ='tab:blue')

gnt.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
								facecolors =('tab:red'))

plt.savefig("gantt1.png")
