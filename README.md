------------------------------------------------------------------------------------------------------------------

![Screenshot 2025-05-16 084050](https://github.com/user-attachments/assets/12bb82c3-f61e-4898-a862-50ad6af9e91b)

------------------------------------------------------------------------------------------------------------------

![Screenshot 2025-04-24 135125](https://github.com/user-attachments/assets/01989c83-2ea5-4820-a473-db7ec5870e16)

Created based on Upwork job posting, used Python to create my own data based on tables listed https://www.upwork.com/jobs/~021915454583394520149

------------------------------------------------------------------------------------------------------------------

![Screenshot 2025-03-24 145707](https://github.com/user-attachments/assets/5c9f34c1-6cae-4e7a-9133-dcc41b120260)
![Screenshot 2025-03-24 145721](https://github.com/user-attachments/assets/b1d405b5-5139-4e8f-9476-2168150f7ec9)
![Screenshot 2025-03-24 145737](https://github.com/user-attachments/assets/8de533df-ddad-4cab-8299-52122cd54c4a)
![Screenshot 2025-03-24 145748](https://github.com/user-attachments/assets/f1ff0e80-ebf1-44be-a64e-cb779606c870)
![Screenshot 2025-03-24 145628](https://github.com/user-attachments/assets/41f64241-af29-4f79-9458-07981c40d201)

DAX & Measures:

Primary Buyer = AND(Customer[Cars Owned] = 0, Customer[Home Owner] = "No")

Secondary Buyer = OR(Customer[Cars Owned] = 0, Customer[Home Owner] = "No")

Full Name = Customer[First Name] & " " & Customer[Last Name]

Order Date Year = Format('Order Date'[Order Date], "YYYY")

Order Date Month = Format('Order Date'[Order Date], "MMM")

Order Date = CALENDAR(Min(Sales[Order Date]), Max(Sales [Order Date]))

Color Category = IF('Product'[Color] IN {"Black", "Blue", "Red"}, "Darker", "Lighter")

Count of ALL Sales Orders Line Items = COUNTROWS(ALL (Sales))

Count of Sales Orders = DISTINCTCOUNT (Sales[Sales Order Number])

Count of Sales Orders Line Items = COUNTROWS (Sales)

Count of Sales Orders Line Items GT 50 = COUNTROWS(FILTER (Sales, Sales[Line Total Sales] > 50 ) )

Line Margin = Sales[Line Total Sales] - Sales[Line Product Cost]

Line Margin % = DIVIDE(Sales[Line Margin], Sales[Line Total Sales], 0)

Line Product Cost = Sales[Order Quantity] * RELATED('Product'[Standard Cost])

PCT Sales Orders Line Items All Time = DIVIDE([Count of Sales Orders Line Items], [Count of ALL Sales Orders Line Items], 0)

PY Total Sales = CALCULATE([TOtal Sales], SAMEPERIODLASTYEAR('Order Date'[Order Date]))

QTD Sales = TOTALQTD([Total Sales], 'Order Date'[Order Date])

Target = 7000000

Total Margin = SUM(Sales[Line Margin])

Total Margin % = DIVIDE([Total Margin], [Total Sales], 0)

Total Sales = SUM (Sales [Line Total Sales])

Total Sales SUMX = SUMX(Sales, (Sales [Unit Price] * Sales[Order Quantity]))

YTD Sales = TOTALYTD([Total Sales], 'Order Date' [Order Date])

Total Sales YoY% = 
VAR __PREV_YEAR =
    CALCULATE ( [Total Sales], DATEADD ( 'Order Date'[Order Date], -1, YEAR ) )
RETURN
    DIVIDE ( [Total Sales] - __PREV_YEAR, __PREV_YEAR )



------------------------------------------------------------------------------------------------------------------

![Screenshot 2025-03-21 150348](https://github.com/user-attachments/assets/18513ef4-dd36-4d20-bc17-421ea9535eb8)

------------------------------------------------------------------------------------------------------------------

Maven Spotify Streaming History: https://mavenanalytics.io/data-playground 

![Screenshot 2025-02-27 130125](https://github.com/user-attachments/assets/78c91ecc-8327-4f72-9178-ba2bea7cb3a6)

------------------------------------------------------------------------------------------------------------------

Maven Market Challenge: https://mavenanalytics.io/challenges/maven-market-challenge/c50a4f9e-1bde-433d-99bd-6436d8ed98e6

![Screenshot 2024-12-30 134749](https://github.com/user-attachments/assets/b33fad7a-f6d1-432d-8725-8ff67aed6b1c)

![Screenshot 2024-12-30 134800](https://github.com/user-attachments/assets/1769c4ab-071d-4aa1-898d-ac1658f87146)

![Screenshot 2024-12-30 134812](https://github.com/user-attachments/assets/054b8cb5-305a-44a6-9e54-6d47b8e514c3)

------------------------------------------------------------------------------------------------------------------

Maven Rail Challenge: https://mavenanalytics.io/challenges/maven-rail-challenge/08941141-d23f-4cc9-93a3-4c25ed06e1c3

This dashboard was created entirely in Python using Visual Studio Code. 

Libraries:

import pandas as pd

from datetime import datetime

import dash

from dash import dcc, html, Input, Output

import plotly.express as px

![Screenshot 2024-11-17 131348](https://github.com/user-attachments/assets/a7295877-3f70-43ac-8778-68296480a62d)

------------------------------------------------------------------------------------------------------------------

Maven Hospital Challenge - https://mavenanalytics.io/challenges/maven-hospital-challenge/facee4d2-8369-4c87-a55e-e6c7ed2a42d8

![Screenshot 2024-11-13 122502](https://github.com/user-attachments/assets/5ec823f8-7d8a-43e0-a0a8-f646960ee973)

![Screenshot 2024-11-13 131434](https://github.com/user-attachments/assets/8c1d0712-74be-4a5d-b597-1cb65bc197fa)

![Screenshot 2024-11-13 123038](https://github.com/user-attachments/assets/c2f80b81-0688-4046-8c0c-819e1aee676d)

![Screenshot 2024-11-13 123055](https://github.com/user-attachments/assets/1bd10224-9ce9-4927-83f4-f72e5cacfa5d)

![Screenshot 2024-11-13 123038](https://github.com/user-attachments/assets/c2f80b81-0688-4046-8c0c-819e1aee676d)

![Screenshot 2024-11-13 123055](https://github.com/user-attachments/assets/1bd10224-9ce9-4927-83f4-f72e5cacfa5d)
------------------------------------------------------------------------------------------------------------------

Pre & Post-Pandemic Ridership for New York City 

Maven Analytics Community Challenge - Maven Commuter Challenge: https://mavenanalytics.io/challenges/maven-commuter-challenge/2300490c-532e-4f34-87a3-a47c83351164

![Screenshot 2024-11-12 143801](https://github.com/user-attachments/assets/a3999e32-70d3-4c0e-9ee1-fc8b3aea6741)

![Screenshot 2024-11-12 143820](https://github.com/user-attachments/assets/8c6bc5ee-cae9-4eaf-865d-51b0861e7837)

![Screenshot 2024-11-12 145305](https://github.com/user-attachments/assets/ca60a657-6178-4ace-b7f4-96a8e2eef4c5)

![Screenshot 2024-11-12 162754](https://github.com/user-attachments/assets/b0c0b5a4-5f18-4143-b818-1496b106e548)

![Screenshot 2024-11-12 162815](https://github.com/user-attachments/assets/7be205b6-1949-4dc5-8213-b9a21b3b2b8e)

![Screenshot 2024-11-12 154421](https://github.com/user-attachments/assets/9d7617ba-a6fa-4f90-b89e-71170b5007bc)

![Screenshot 2024-11-12 154445](https://github.com/user-attachments/assets/e8622a07-dd83-41b8-9cf5-a7f6abaed94c)

![Screenshot 2024-11-12 154502](https://github.com/user-attachments/assets/8eb54ee7-4233-4a5f-b7df-c89803354059)

![Screenshot 2024-11-12 154516](https://github.com/user-attachments/assets/811ee531-0f45-4e11-8980-25c4523892b4)
