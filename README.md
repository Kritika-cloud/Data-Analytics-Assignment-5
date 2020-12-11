# Data Analytics Assignment#5

## Explaining Python Code
Main Aim:To make a function to find out distribution of top 1000 youtube channels<br/>

![Youtube](https://user-images.githubusercontent.com/75749963/101848986-c5e65480-3b24-11eb-9a13-6df5d583cbca.jpeg)


Step1:
Data was loaded into dataframe named raw_df using pandas<br/>
Step2:
A code to extract top 1000 rows was written using iloc<br/>
Step3:
value_counts() function was used to count the distribution of channels<br/>
Step4:
A function named first_1000 was defined by generalising the above two lines of code<br/>
Step 5:
The function was called by passing name of dataframe and number of rows as the arguments
Step 6:
Extracting top 1000 records and importing them in a separate csv file using .to_csv
