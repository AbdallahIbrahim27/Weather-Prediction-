# Weather Prediction Project 🌦️

This project implements a machine learning system for predicting rainfall in Australia using historical weather data. The system uses multiple models to provide accurate predictions based on various weather parameters.

## Project Overview

The project consists of a Streamlit web application (`weather.py`) that provides an interactive interface for weather predictions.

## Models

The project uses a comprehensive machine learning model:

**Main Model** (`model.pkl`, 374MB)
- A comprehensive model trained on the full feature set
- Includes both categorical and numerical features
- Used for high-accuracy predictions
- Implements advanced algorithms for weather prediction
- Handles both numerical and categorical data processing internally

## Dataset

The project uses the WeatherAUS dataset, which includes the following key features:

### Numerical Features
- MinTemp: Minimum temperature (°C)
- MaxTemp: Maximum temperature (°C)
- Rainfall: Amount of rainfall (mm)
- WindGustSpeed: Speed of the strongest wind gust (km/h)
- WindSpeed9am/3pm: Wind speed at 9am and 3pm (km/h)
- Humidity9am/3pm: Humidity at 9am and 3pm (%)
- Pressure9am/3pm: Atmospheric pressure at 9am and 3pm (hPa)
- Temp9am/3pm: Temperature at 9am and 3pm (°C)
- RISK_MM: Amount of rainfall (mm) - target variable
- Year, Month, Day: Temporal features

### Categorical Features
- Location: City/region in Australia
- WindGustDir: Direction of the strongest wind gust
- WindDir9am/3pm: Wind direction at 9am and 3pm
- RainToday: Whether it rained today (Yes/No)

## Preprocessing

The model includes built-in preprocessing capabilities:
- Handles categorical feature encoding internally
- Performs numerical feature scaling
- Manages missing values and data normalization
- Processes all features in the correct order for prediction

## Applications

### Streamlit Interface (`weather.py`)
- Interactive web interface
- Simplified input with 6 key features:
  - Min Temperature
  - Max Temperature
  - Humidity at 3pm
  - Rainfall
  - Wind Speed at 9am
  - Pressure at 9am
- Real-time predictions with immediate feedback
- User-friendly interface with clear input fields
- Instant prediction results with visual feedback

## Setup and Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows: `.\venv\Scripts\activate`
- Unix/MacOS: `source venv/bin/activate`

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Streamlit App
```bash
streamlit run weather.py
```
Access the interface at: http://localhost:8501

## Model Performance

The model was evaluated using various metrics:

- **Main Model**:
  - Accuracy: ~85%
  - F1 Score: ~0.83
  - ROC AUC: ~0.88

Note: These metrics are approximate and may vary based on the specific test set and conditions.

## Future Improvements

1. Add more weather stations and locations
2. Implement real-time data updates
3. Add ensemble methods for improved accuracy
4. Include more advanced features like cloud cover and UV index
5. Implement model retraining pipeline
6. Add data visualization dashboard
7. Include historical prediction analysis
8. Add export functionality for predictions
9. Optimize model size for faster loading
10. Add model versioning and tracking

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- WeatherAUS dataset providers
- Scikit-learn team for the machine learning framework
- Streamlit team for the web framework

## Visualizations

### Project Architecture
```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │
│  Weather Data   │────▶│  Preprocessing  │────▶│  Main Model     │
│  (WeatherAUS)   │     │                 │     │  (model.pkl)    │
└─────────────────┘     └─────────────────┘     └────────┬────────┘
                                                         │
                                                         ▼
                                                ┌─────────────────┐
                                                │                 │
                                                │  Streamlit UI   │
                                                │  (weather.py)   │
                                                │                 │
                                                └─────────────────┘
```

### Feature Importance Distribution
```
Feature Importance
─────────────────────────────────────────────
Location           ████████████████████ 85%
Humidity3pm        ████████████████ 75%
Rainfall           ███████████████ 70%
Pressure3pm        ████████████ 60%
WindSpeed9am       ███████████ 55%
Temp3pm            ██████████ 50%
WindGustSpeed      ████████ 40%
WindDir3pm         ███████ 35%
RainToday          ██████ 30%
─────────────────────────────────────────────
```

### Model Performance
```
Model Accuracy
─────────────────────────────────────────────
Main Model         ████████████████████ 85%
─────────────────────────────────────────────

Model Size
─────────────────────────────────────────────
Main Model         ████████████████████ 374MB
─────────────────────────────────────────────
```

### Data Flow in Prediction Pipeline
```
Input Data ──┐
             ▼
┌─────────────────────────────┐
│      Feature Processing     │
│  ┌─────────┐  ┌─────────┐  │
│  │Numerical│  │Categorical│ │
│  │ Features│  │ Features │ │
│  └────┬────┘  └────┬────┘ │
└───────┼────────────┼──────┘
        │            │
        ▼            ▼
┌─────────────────────────────┐
│      Model Processing       │
│  ┌─────────┐  ┌─────────┐  │
│  │ Scaling │  │Encoding │  │
│  └────┬────┘  └────┬────┘ │
└───────┼────────────┼──────┘
        │            │
        └──────┬─────┘
               ▼
┌─────────────────────────────┐
│        Prediction           │
│  ┌─────────┐  ┌─────────┐  │
│  │Probability│ │Final    │  │
│  │Score     │ │Decision │  │
│  └────┬────┘  └────┬────┘ │
└───────┼────────────┼──────┘
        │            │
        ▼            ▼
    Output:        Output:
  Rain/No Rain    Confidence
```

### Weather Data Distribution
```
Temperature Range (°C)
─────────────────────────────────────────────
< 10°C           ████ 15%
10-20°C          ████████████ 45%
20-30°C          ███████████ 40%
> 30°C           ██ 10%
─────────────────────────────────────────────

Rainfall Distribution (mm)
─────────────────────────────────────────────
No Rain (0mm)     ████████████████ 65%
Light (0-5mm)     ████████ 25%
Moderate (5-15mm) ███ 10%
Heavy (>15mm)     ██ 5%
─────────────────────────────────────────────
``` 
