# Crypto Data Analytics

## Note: This is an assessment given to ALTSCHOOL DATA ENGINEERING STUDENTS.

## Introduction:
Welcome to my Crypto Data Analysis project! As a dedicated data engineer, you've been entrusted with the crucial task of delving into the world of cryptocurrencies to extract valuable insights for an esteemed company executives. This README will guide you through the process of loading and analyzing the provided CSV files, and helping you to address important business questions and informed decision-making.

## Project Overview:

In this project, we aim to leverage the power of data to gain a deeper understanding of various cryptocurrencies. You have been provided you with CSV files containing essential information that holds the key to unlocking insights. By following the instructions outlined below, it will help in navigating through the data, perform necessary analyses, and ultimately provide valuable answers to the questions anticipated by our executives.

### Instructions:

    Dataset Overview:

Data Source: 
Shared CSV files that contain information on different cryptocurrencies.
- members table 
- transaction table
- prices table




    
    
    
    
      Setup:

To get started, ensure that you have the necessary tools and libraries installed. i recommend using Postgres, DBeaver and VScode. You may use popular libraries such as Pandas, Python, Numpy. 
Ensure to use your local system terminal to create the USER and PASSWORD which is highly recommended, DATABASE and SCHEMA respectively.

     CREATEROLE 'user_name' WITH LOGIN PASSWORD 'password' ;
     CREATE DATABASE 'new_database_name' OWNER 'user_name' ;
     CREATE SCHEMA 'schema_name';


Then test your connecting on DBeaver before importing data

    Loading the Data:
Use your preferred method to import the CSV files into a DBeaver. Make sure to inspect the data structure and familiarize yourself with the available columns.

    Display basic information about the DataFrame:
    SELECT  * 
    FROM raw.transactions;

Noting that, the transaction file, contains more required information for this analysis, using the above query.




    Data Cleaning:

Clean the data to handle any missing values and duplicates, if available or outliers that may affect the accuracy of your analysis.

## Analysis:
Analysis phase. Answer the specific business questions provided by the executives using the insights gained from the data.

    Visualization:

Enhance your findings by creating visualizations that make complex trends and patterns more accessible to the executives.

## Reporting:
Document your findings and insights in your report.present your analyses, visualizations if required, and recommendations to provide a holistic understanding of the cryptocurrency landscape.

## Conclusion:
By following these instructions, you'll be well-equipped to embark on a meaningful journey into the realm of cryptocurrency data analysis. Your efforts are crucial in shaping informed decisions for the company future.




MIT License:

Copyright (c) [2023] [Idiyeli Sunday]

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

