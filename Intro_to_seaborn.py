import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create scatter plot with GDP on the x-axis and number of phones on the y-axis
sns.scatterplot(x=gdp, y=phones)

# Create count plot with region on the y-axis
sns.countplot(y=region)


""" Pandas with seaborn ----->>>> ONLY if the db is tidy!!!!    """
# add another argument to: sns.***plot(xxx, yyy, data = your_df)

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Create a count plot with "Spiders" on the x-axis
sns.countplot(x = 'Spiders', data = df)

# Display the plot
plt.show()


""" Adding a third variable by coloring ---->>> hue =    """
# Example 1
# Change the legend order in the scatter plot
sns.scatterplot(x="absences", y="G3", 
                data=student_data, 
                hue="location", hue_order = ['Rural', 'Urban'])            

# Show plot
plt.show()


# Example 2
# Create a dictionary mapping subgroup values to colors
palette_colors = {'Rural': "green", 'Urban': "blue"}

# Create a count plot of school with location subgroups
sns.countplot(x = 'school', data = student_data, hue = 'location', palette = palette_colors)

# Display plot
plt.show()

