```
Global AQI Risk
A machine learning system that predicts the mortality rates by analyzing real world parameters such as PM2.5, PM10, CO2 Emissions, Renewable Energy Production per country across the world.
```
```
Project Overview

This project pulls real-time air quality data from the OpenAQ API, and uses several datasets secured from Kaggle and then processes and engineers features using NumPy and Pandas, builds a prediction model which predicts mortality rates while using real-time data from WHO as it's target using Random Forest Regression.

The system currently monitors 25 countries over the world, classifying each country by the average of PM2.5, PM10, Co2 Emissions, Renewable energy production per country.

```
```
Tech Stack

Data Collection: Python, Requests, OpenAQ API
Data Processing: Pandas, NumPy
Machine Learning: Scikit-learn (Random Forest Regressor)
Environment: Jupyter Notebook, VS Code

```
```
Project Structure

global-aqi-risk/
├── data/
│   ├── agg_df.csv
│   ├── air_quality_health_dataset.csv
│   ├── base_df.csv
│   ├── co-emissions-per-capita.csv
│   ├── death-rate-ambient-air-pollution.csv
│   ├── final_df.csv
│   ├── polluted_cities.csv
│   └── renewable-share-energy.csv
├── notebooks/
│   └── 01_data_exploration.ipynb
├── .env
├── .gitignore
└── README.md

```
```
How It Works

PM2.5,PM10,CO2 Emissions,Renewable Energy data is procured from various datasets sourced from kaggle
Data is cleaned — outliers removed, missing values dropped, various datasets merged together, clean up of unnecessary columns.
Features engineered: WHO classified normalized pollution scores, WHO-aligned risk categories (Low Risk → Very High Risk).
Combined risk score calculated as weighted average of normalized pm25_avg,pm10_avg,co2_avg,ren_avg scores (0-100 scale)
Random Forest Regressor trained to predict death rates of the countries considering target variable from real-world data.

```
```
Results
Dataset: 25 Countries with complete PM2.5, PM10, CO2 Emission, Renewable Energy production data.
Model MAE: 15.39 (on held-out test set)
Key Finding: Countries with high PM2.5 and PM10 alone scored a very high mortality rate due to the fact that there were no external factors taken into account Ex: Population Density, Source of the particulate matter.
Mortality Prediction: 3 out of 5 countries have high mortality rate. PM2.5 and PM10 account for 75% of the model's predictive power, confirming particulate matter as the primary driver of air pollution mortality.

```
```
Limitations & Future Work
Risk score currently based on PM2.5, PM10, co2 emissions, renewable enegy only
Country level proxy data — CO2 and renewable energy are country level values assigned to all cities in that country. City level data doesn't exist publicly.
Small dataset — only 25 countries after merging all datasets. Not enough for statistically robust conclusions.
3 year gap — AQI features are from 2016, death rate target is from 2019. Assumed acceptable given slow-changing mortality trends.
Natural vs industrial pollution — Kuwait over-predicted because desert dust (natural PM10) is less harmful than industrial PM2.5. The model doesn't distinguish between pollution types.
Single year snapshot — AQI data is mostly from 2016. No true time series for trend prediction.
Risk score formula — the city level risk score is human-defined using WHO thresholds, not learned from data. Weights (40/20/20/20) are expert judgment, not scientifically validated.

```
```

Sources
## Data Sources
- [WHO Most Polluted Cities](https://www.kaggle.com/datasets/rajkumarpandey02/worlds-most-air-polluted-countries-cities)
- [CO2 Emissions Per Capita](https://ourworldindata.org/grapher/co-emissions-per-capita)
- [Renewable Energy Share](https://ourworldindata.org/grapher/share-electricity-renewables)
- [WHO Death Rate from Air Pollution](https://ourworldindata.org/grapher/death-rate-ambient-air-pollution)

```
```
About
Built as part of an AI/ML learning journey focused on using data science for environmental impact. All data sourced from OpenAQ's public API and datasets from Kaggle.

```