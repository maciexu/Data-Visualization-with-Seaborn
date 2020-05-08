# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter", 
            row="study_time")

# Show plot
plt.show()






# add subplots based on school&family support
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter", 
            col="schoolsup",
            col_order=["yes", "no"], 
            row='famsup',
            row_order = ['yes', 'no'])

# Show plot
plt.show()


"""
Subplots ------>>> col =   , row =    .
Subgroups with color ----->>>> hue = 
Customizing ----->>>> point size, style, transparency
"""


# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg", 
            data=mpg, kind="scatter", 
            hue='cylinders',
            size="cylinders")

# Show plot
plt.show()



# Create a scatter plot of acceleration vs. mpg
sns.relplot(x="acceleration", y="mpg", 
            data=mpg, kind="scatter", 
            style="origin", hue="origin")

# Show plot
plt.show()



""" line """

# Create line plot
sns.relplot(x='model_year', y='mpg', data=mpg, kind='line')             # the output will show the confidence internal

# Show plot
plt.show()


# Make the shaded area show the standard deviation
# Use the ci parameter to change what the shaded area represents. By default, it is the confidence internal. 
# ci = 'sd' shows the standard deviation instead of the confidence interval for the mean.
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line", ci='sd')

# Show plot
plt.show()



# Add markers and make each line have the same style
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None, style="origin", 
            hue="origin", markers=True, dashes=False)

# Show plot
plt.show()


