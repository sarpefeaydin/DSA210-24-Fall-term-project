# DSA210-24-Fall-term-project

**##INTRODUCTION**
Until I started to study for the university entrance exam, I used to spend a lot of time with my Playstation 4. But especially after I started university my hours in front of the TV started to drop. At least it feels like it. So the aim of this project is to analyze the data which I collected from Sony and Apple Health and to investigate if they have any correlation with each other. The hypothesis is that whenever I acquired new content to play with on my PS4 it would affect my steps taken and decrease it for 4 days after the purchase.


**##DATA SOURCES AND CONTENTS**
Both the data from Sony and the data from Apple Health were easy to access. I downloaded the data from Apple Health directly. The data consist of "Date" and "Step Counts". I requested the data from Sony via account settings, which was pretty easy as well. After some cleaning these data only consist of "Transaction Date" and "Content Type". Transaction dates are the dates that those "contents" ("New Game", "In-game Content", "Subscriptions" and "Apps") were acquired either for free or with money. By examining these data, I am trying to find if there is a correlation between acquiring new contents for my PS4 and the change in my step counts after acquiring new contents related to my average step count. 


**##DATA PROCESSING**
Since I did not have a phone until high school, I have health data starting from 06-12-2017. That's why I only use the data from Sony starting from that date. Fortunately before that date there are not many data to begin with. There is also a time period starting from 14-02-2022 to 18-06-2022 which I did not use my phone at all while studying for the university entrance exam. The data during that time can be misleading because steps taken during that period are either 0 or completely blank. In order to aviod confusion I excluded that data. The tricky part is that Apple Health app exports the data in a messy .xml format so it needs cleaning and organizing. In order to get the simple and clean data I needed, I used an app called "Health Export" from the app store which basically converts the data into the format I can use. I combined the two datasets in one .xlsx file. After the operations data were ready to be analyzed.

After the necessary operations, I used Python libraries pandas, matplotlib and seaborn to calculate the average steps taken overall and for a window of 4 days after a day of any purchase and visualize the differences between those averages. To get rid of the unnecessary and extra date points I merged the purchases on the same days.


**##FINDINGS AND VISUALIZATION**
There are 77 different days with any type of purchase. Overall average steps taken is 4520.45, overall post-purchase steps taken is 4149.75. Down below 3 different types of visualized data can be seen.

A scatter plot with axes of "Change in Step Count" and "Transaction Date" regarding the types of transactions:
![scatter_plot](https://github.com/user-attachments/assets/1cb9d630-650b-4cc4-b1fc-fa2351a3cc5d)

A histogram of distribution of step count changes with axes of "Frequency" and "Change in Step Count":
![histogram](https://github.com/user-attachments/assets/232ad451-bfd4-442b-83d0-17ef4ae7e594)

A bar plot with axes of "Steps" and "Transaction Date", showing the overall average steps taken and post-transaction average of 4 days after the transaction.
![bar_plot_with_average_line](https://github.com/user-attachments/assets/d0b31c69-a65e-4806-8aaf-c6ca6056f358)

After the plotting and visualization, I applied t-test and calculated the p-value using scipy library in order to see if I am able to reject the null hypothesis, which states that acquiring new content for PS4 has no effect on daily steps taken.
<img width="723" alt="Screenshot 2025-01-03 at 18 35 11" src="https://github.com/user-attachments/assets/c840de00-0634-4a60-be62-21aeb0f5d1f7" />


**##RESULTS**
Regarding the test outcomes, I am not able to reject the null hypothesis. This tells us that acquiring new content for PS4 does not have a significant effect on the steps that I take.
