# Computer Science Capstone - ML Fantasy Football
## - Isaiah Bullock

---
## About Project 
Project using a linear regression model to predict fantasy football scores based off data of the previous year. Uses data collected from pro football reference as training data.
The following for this project is the written portion of the project
(noted in parts A and B). Analysis of the models accuracy will also take place and will use the data set of 1970-2024 seasons as its reference.

---

## Letter of Transmittal and Project Proposal

To: [Recipient Name] \
From: Isaiah Bullock\
Date: 1/24/25\
Subject: Fantasy Football Machine Learning Model Project Proposal\

Dear [Recipient Name],

I am pleased to present the proposal for the Fantasy Football Machine Learning Model project.
This project aims to streamline the fantasy football drafting process using statistical analysis
to predict player performance. With the help of machine learning algorithms, this tool will
assist both novice and expert fantasy football players in making more informed decisions
when selecting players for their teams.

### Project Overview

Drafting and ranking players for fantasy football is a long and arduous process that must be repeated each year. Our goal is to make statistical analysis more accessible by providing quick and accurate player predictions, empowering fantasy managers regardless of how much time they have to devote to the research. This model uses historical performance data and predictive analytics to generate rankings, allowing users to optimize their fantasy football teams.

### Target Audience

This tool is designed for a broad audience. Primarily, it serves fantasy football enthusiasts who are looking to enhance their draft strategy by leveraging data-driven insights. However, general NFL fans interested in player statistics and performance projections will also find the model valuable.

### Data and Model

The model uses data from Pro Football Reference, which is a reputable, non-biased source for NFL statistics. A linear regression model is employed to predict fantasy football points based on a player’s past performance metrics. The model is trained on data from 1970 to 2024.

### Key Features
- Player Rankings: Players are ranked based on predicted fantasy points.
- Model Evaluation: The model’s performance is evaluated using Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE).
- Simple User Experience: The model is designed to be user-friendly through a simple console interface.

### Areas for Improvement

While the current model provides useful insights, there are several areas for future enhancement:
- Rookies: Currently, the model struggles to predict the performance of rookies.
- Team and Depth Chart Consideration: Player transfers, team strength, and depth chart position are not accounted for in the current version.
- Injury Impact: The model does not account for players coming off injuries or injury predictions.
- Career Trajectory: Future improvements could include using a player’s entire career data to enhance predictions.

### Funding Requirements

While the project is currently a self-contained local tool, if it were to be scaled or used by others in a broader context (e.g., offering an online service), the following considerations should be included:

To fully implement the project at scale, the following funding is required:
- Cloud Hosting Costs: To support a large number of users, the project would need cloud-based servers to host the model and data. Estimated monthly costs for hosting on a platform like AWS or Google Cloud would be approximately $200-$500, depending on traffic.
- Database Hosting: Storing and managing player statistics and rankings for a wider user base would require a database, either relational or NoSQL. Cloud database hosting costs are expected to range from $50-$200/month depending on data size and storage frequency.
- Software and Tools: Some tools and frameworks used for machine learning and model evaluation may require licenses. However, the majority of the tools (e.g., scikit-learn, pandas, matplotlib) are open-source.

### Ethical and Legal Considerations

While working with and communicating about sensitive data, we will adhere to the following ethical and legal precautions:
- Data Privacy: We will ensure that no personally identifiable information (PII) is used in our model. The data comes from publicly available player statistics on Pro Football Reference, which adheres to the platform’s terms of use.
- Data Ownership and Use: The project will adhere to fair use and attribution guidelines when referencing and using public data. This ensures that no proprietary or confidential information is being used improperly.
- Transparency: The model and its outputs will be fully transparent to users. They will have access to the methodologies and data used to generate predictions, ensuring trust in the model’s decision-making process.
- Bias Consideration: The model will aim to avoid biases, especially regarding player injuries, which are not always available in historical data. Future iterations of the model will strive to incorporate additional data to minimize any bias.

### My Expertise

I have experience in software development, data analysis, and machine learning, which are key to the successful completion of this project. Over the years, I have developed a strong understanding of Python, data cleaning, and building predictive models using scikit-learn and other machine learning libraries. Additionally, my experience in sports analytics, particularly in fantasy football, has allowed me to approach this project with both technical and user-centric perspectives. My aim is to create a data-driven solution that can be used by enthusiasts and professionals alike.

### Conclusion

This project offers a powerful tool for both fantasy football players and general NFL enthusiasts. I look forward to your feedback and potential collaboration as we continue to refine the model and expand its features.

Sincerely,\
Isaiah Bullock

---

## Executive Summary

### Project Title: Fantasy Football Machine Learning Model

<strong>Objective:</strong>
The Fantasy Football Machine Learning Model aims to predict the fantasy football points of NFL players, providing rankings based on performance data. The model uses a linear regression algorithm to make predictions, and the goal is to improve the accuracy of player rankings for fantasy football managers.

<strong>Key Features:</strong>
- Predictive Analytics: The model ranks players based on predicted fantasy points, using past performance data.
- Evaluation Metrics: The model’s performance is assessed through MAE, MSE, and RMSE metrics.
- User-Friendly Interface: The model is designed to be simple and easy to use, providing a seamless experience for the user.

<strong>Target Audience:</strong>
- Fantasy football enthusiasts who are looking for an edge in their drafts.
- General NFL fans who are interested in player statistics and performance projections.

<strong>Data Source:</strong>
The model uses data from Pro Football Reference, which provides detailed and accurate statistics for all NFL players.

<strong>Current Model and Limitations:</strong>
- Linear Regression: The current version of the model uses linear regression, which works well for many players, but has limitations in predicting breakouts and underperformance.
- Areas for Improvement: The model does not account for rookie status, injury history, player transfers, depth chart positions, or team strength. These are areas for future expansion, which could significantly improve the accuracy of predictions.

#### <strong>Model Evaluation (Sample Results):</strong> 

<strong>Total Data Analysis:</strong>
- MAE: 43.34
- MSE: 3470.86
- RMSE: 58.91

<strong>RB Analysis:</strong>
- MAE: 47.10
- MSE: 3987.96
- RMSE: 63.15

<strong>WR Analysis:</strong>
- MAE: 43.43
- MSE: 3258.00
- RMSE: 57.08

<strong>Projected Timeline, Including Milestones</strong>

To give a clear understanding of the development process, here’s a simple timeline for the next stages:
- Phase 1: Data Collection and Cleaning (2 weeks)
  - Collect player statistics from Pro Football Reference (completed).
  - Clean and preprocess the data (handling missing values, normalization).
- Phase 2: Model Development and Testing (3 weeks)
  - Develop and test the linear regression model (completed).
  - Evaluate the model’s accuracy using MAE, MSE, RMSE.
- Phase 3: Visualization and Interface Development (2 weeks)
  - Develop visualizations (scatterplots, pairplots, probplots).
  - Create a simple user interface (CLI).
- Phase 4: Final Testing and Documentation (2 weeks)
  - Test the final version of the model.
  - Create documentation (GitHub repository, user guide).
- Phase 5: Deployment (2 weeks)
  - Host the project on a platform like GitHub or consider cloud deployment for wider use.

<strong>Conclusion:</strong>
This machine learning model has the potential to transform the way fantasy football players make draft decisions by providing data-driven insights into player performance. While there are areas for improvement, the foundation has been set, and the model can be further refined to produce even more accurate rankings and predictions.

---
## Areas of part C... 
#### that seemed better for writing as it is not a live service that collects user data
### Industry-Appropriate Security Features

For security, especially if transitioning to a cloud-hosted environment, these are things that could be done once the service is live:
- Data Encryption: When hosting player data on cloud platforms, we will ensure that data is encrypted at rest and in transit using industry-standard protocols (e.g., AES-256 encryption).
- Access Control: Role-based access control will be implemented, ensuring that only authorized users (e.g., admins, users with special permissions) can access sensitive data.
- Compliance with GDPR: If any personal data is collected in the future (e.g., user-generated rankings or feedback), we will ensure compliance with GDPR (General Data Protection Regulation) for European users.
- Secure Authentication: Any future user-facing features (e.g., account creation, access to personalized predictions) will utilize OAuth 2.0 or similar secure authentication mechanisms.

### Tools to Monitor and Maintain the Product

Monitoring and maintaining the product once it’s live is key for ensuring smooth operation.
- Application Monitoring: Tools like New Relic or Datadog will be used to monitor the model’s performance and ensure that it scales effectively with increasing traffic.
- Model Monitoring: Regular checks will be performed on model predictions, ensuring that the model’s accuracy is consistent. If the accuracy decreases, retraining or algorithm adjustments will be necessary.
- Error Reporting: Tools like Sentry can be implemented to monitor errors in real-time and alert the development team to address issues quickly.
- Maintenance Schedule: Regular updates to player data, model training, and system performance will be scheduled at regular intervals (e.g., quarterly).

---
## Quick-Start Guide

1. Installation:
   - Ensure that Python (version 3.x) is installed.
   - Install necessary libraries: pip install -r requirements.txt.
2. Running the Model:
   - Launch the script with the following command:
   python fantasy_football_predictor.py.
   - Provide instructions for selecting a position and viewing player rankings.
3. Viewing Visualizations:
   - Upon running all plots will be shown within ide (plots for the evaluation in README are in the plots folder)
