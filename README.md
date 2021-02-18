# DATA-690-WANG

### Assignment 1
- Prompts a user to enter 10 integers. If the user enters anything other than integers, remind her that only integers are allowed and let her retry. Don't allow the user to enter more than 10 or less than 10 integers. Display the 10 integers back to the user at the end. Calculate the following statistics from the 10 integers entered

### Assignment 2
-

### Assignment 3
- generate 100 random numbers 0-9 and format into different grids

### Assignment 4
- Write code to open the text file census_cost.txt and read all lines into a list named "line_list". Print line_list.
- Extract the first two lines and put them in a different list named "top2_list". You will need to use them later. Print the top2_list.
- Put the rest of the lines (containing useful data elements) in a new list named "data_list". Print data_list.
- Extract the column "Census Year" from data_list and assign them to a list named year_list. Remove the "" from the last element "2010". Print the cleansed year_list.
- Extract the "Total Population" column from the data_list and assign them to a list named "pop_list". Remove the "," from the numbers since Python doesn't recognize them. Print the cleansed "pop_list".
- Extract the "Census Cost" column from the data_list and assign them to a list named "cost_list". Remove the ",", and "$", and "Billion". Make sure to add the "0"s to the numbers from which you removed "Billion". Print the cleansed cost_list.
- Extract the "Census Cost" column from the data_list and assign them to a list named "cost_list". Remove the ",", and "$", and "Billion". Make sure to add the "0"s to the numbers from which you removed "Billion". Print the cleansed cost_list.
- Coalesce the cleansed data and save them to a text file named "census_cost.csv". The new file should look similar to the original source file except that it is in comma-delimited format and the numbers have been cleansed. The top two lines from the original file should be retained in the new file.
- Open the newly-created file "census_cost.csv", read all lines and display them. How does it look?

### Assignment 5
- Upload the 2017-2018 school year file "MERGED2017_18_PP.csv" to Colab and create a Jupyter notebook to explore the dataset:
  - how many colleges or rows?
  - how many variables or columns?
  - Look at the first 5 colleges
  - look at the last 5 colleges
  - Look at a random sample of 5 colleges
- Since there are too many variables to explore, many of which are not interesting. Create a smaller data frame with the following 9 variables:
  - UNITID
  - INSTNM
  - CITY
  - STABBR
  - ZIP
  - ADM_RATE
  - UGDS
  - TUITIONFEE_IN
  - MN_EARN_WNE_P10
- Download and read the data dictionary file - https://collegescorecard.ed.gov/assets/CollegeScorecardDataDictionary.xlsx
- Find out the definition of the above 9 variables and document the definitions in the Jupyter Notebook in a Markdown cell so that the readers of your notebook will know the meaning of these variables.

### Assignment 6
- Use Pandas read_html() function to retrive the HTML tables as dataframes from the web page: https://www.genealogybranches.com/censuscosts.html
- Find out how many HTML tables Pandas retrieves from the web page. Find out which dataframe contain the data and use it for further processing.
- Display and explore the data (rows, columns, etc.) and determine the data quality (bad rows, bad columns, bad elements, null values, etc.)
- Document the data quality issues using a Markdown cell so the reader understands what the problems are.
- Write a function named cleanse_year() that takes a string as input and removes any asterisks in the string and return the cleansed string. Test the function by using test strings (for example, "1989", "2010")
- Cleanse the column "Census Year" using the function cleanse_year() and Pandas's apply() function.
- After all columns are cleansed, save the clenased dataframe to a file named "census_cost_cleansed.csv" using CSV format.
- Use Pandas to read the saved cleansed file and explore to make sure it is clean.

### Assignment 7
- https://ed-public-download.app.cloud.gov/downloads/CollegeScorecard_Raw_Data.zip
- After unzipping, You will have all files in one folder named "CollegeScorecard_Raw_Data"
- write code to remove the unwanted files from the list variable 
  - Note: don't remove/delete these files from the folder in your drive
- Now that you have a clean list of the yearly files, you want to loop through them
- and read them into a dataframe one at a time. You only load six columns: 
- ["UNITID", "INSTNM", "STABBR", "REGION", "ADM_RATE", "TUITIONFEE_IN"].
- You should use "usecols" option of Pandas to avoid reading unwanted columns.
- You also want to add a new column call "YEAR" to differentiate the data frames from each other.
- look at just UMBC but assign to new df
- sort table by YEAR column
- Plot UMBC's in-state tution overtime from 1996 to 2019 using Bar Chart 
- Plot UMBC's in-state tution overtime from 1996 to 2019 using Line Chart
- Now let's look at the tuition growth rate year over year
- We need to calculate UMBC tuition change percentage each year
- First convert the TUITIONFEE_IN column to a Python List
- Loop through the list and calculate the % change each year over the prior year
- Round up the percentage to two decimal points
- Add the list of the percentages to the dataframe as a new column ("PCT_CHANGE")
- Finaly, we can make the plot tuition growth rate year over year - bar first, then line chart
- Let's create a function which can be reused for any college.
- Plot JHU's in-state tuition overtime from 1996 to 2019. 
- etc

### Assignment 8
-

### Assignment 9
-

### Assignment 10
- 
