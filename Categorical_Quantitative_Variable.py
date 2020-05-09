""" Categorical 
count plots  ---->>> catplot(x=, data=, kind='count', order=[], )
bar plots --->>> display the mean of quantative variable per category, and 95% confidence intervals 
          --->>> catplot(x, y, data, kind='bar', ci=None)
comparison between groups
"""
# Example 1
# Create column subplots based on age category
sns.catplot(y="Internet usage", data=survey_data,
            kind="count", col='Age Category')
# Show plot
plt.show()


# Example 2
# Create a bar plot of interest in math, separated by gender
sns.catplot(x='Gender', y='Interested in Math', data=survey_data, kind='bar')
# Show plot
plt.show()


# Example 3
# Turn off the confidence intervals
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=["<2 hours", 
                   "2 to 5 hours", 
                   "5 to 10 hours", 
                   ">10 hours"], ci=None)

# Show plot
plt.show()



""" Box
Comparison of distrubutions of quantiative variables among groups
catplot(x=categorical, y=quantitative, data=, kind='box', order=, sym='')
whiskers, whis=1.5 by defauly, whis=[5, 95]
"""

# Example 1
# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours", 
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(x='study_time', y='G3', data=student_data, kind='box', order=study_time_order)

# Show plot
plt.show()


# Example 2
# Create a box plot with subgroups and omit the outliers
# you can omit outliers in box plots by setting the sym parameter equal to an empty string ("").
sns.catplot(x='internet', y='G3', data=student_data, kind='box', sym='', hue='location')

# Show plot
plt.show()


# Example 3
# Set the whiskers at the min and max values
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[0, 100])      # whis=0.5, whis=[5, 95]

# Show plot
plt.show()



""" point plot """

# Example 1
# Remove the lines joining the points
sns.catplot(x="famrel", y="absences",
			      data=student_data,
            kind="point",
            capsize=0.2, join=False)            
# Show plot
plt.show()



# Example 2
# Import median function from numpy
from numpy import median

# Plot the median number of absences instead of the mean
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None, estimator=median)

# Show plot
plt.show()
