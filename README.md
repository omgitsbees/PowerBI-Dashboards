Pre & Post-Pandemic Ridership for New York City 

Maven Analytics Community Challenge - Maven Commuter Challenge: https://mavenanalytics.io/challenges/maven-commuter-challenge/2300490c-532e-4f34-87a3-a47c83351164

![Screenshot 2024-11-12 143801](https://github.com/user-attachments/assets/a3999e32-70d3-4c0e-9ee1-fc8b3aea6741)

![Screenshot 2024-11-12 143820](https://github.com/user-attachments/assets/8c6bc5ee-cae9-4eaf-865d-51b0861e7837)

![Screenshot 2024-11-12 145305](https://github.com/user-attachments/assets/ca60a657-6178-4ace-b7f4-96a8e2eef4c5)

1. Trend Analysis Over Time

    Track the ridership and traffic data to see how various transportation modes have recovered over time relative to pre-pandemic levels.

SELECT 
    Date,
    AVG(`Subways: % of Comparable Pre-Pandemic Day`) AS avg_subways_percentage,
    AVG(`Buses: % of Comparable Pre-Pandemic Day`) AS avg_buses_percentage,
    AVG(`Bridges and Tunnels: % of Comparable Pre-Pandemic Day`) AS avg_bridges_tunnels_percentage
FROM 
    omgitsbeesdata.DailyRidership.Ridership
GROUP BY 
    Date
ORDER BY 
    Date;

2. Identify Peak Usage Days

    Find the days with the highest estimated ridership for each transportation mode. This can be useful to understand peak days and periods.

SELECT 
    Date,
    MAX(`Subways: Total Estimated Ridership`) AS max_subways_ridership,
    MAX(`Buses: Total Estimated Ridership`) AS max_buses_ridership,
    MAX(`Bridges and Tunnels: Total Traffic`) AS max_bridges_traffic
FROM 
    omgitsbeesdata.DailyRidership.Ridership
GROUP BY 
    Date
ORDER BY 
    max_subways_ridership DESC
LIMIT 10;
------------------------------------------------------------------------------------------------------------------
