# Solution Code: Basic Sentiment Analysis App

This project showcases a simple Flask-based Sentiment Analysis API leveraging the TextBlob library. Additionally, it demonstrates a simulated AI model with a logging decorator that tracks the input and output during predictions.

## Installation
1. Clone this repository:
   ```shell
   git clone git@github.com:Thinkful-Ed/solution-code-flask-endpoints-project.git
   ```
2. Navigate to the repository directory:
   ```shell
   cd solution-code-flask-endpoints-project
   ```
3. Set up a virtual environment:
   * On macOS and Linux:
     ```shell
     python3 -m venv flask_endpoints_project_env
     ```
   * On Windows:
     ```shell
     python -m venv flask_endpoints_project_env
     ```
4. Activate the virtual environment:
   * On macOS and Linux:
     ```shell
     source flask_endpoints_project_env/bin/activate
     ```
   * On Windows:
     ```shell
     .\flask_endpoints_project_env\Scripts\activate
     ```
5. Install the required packages (Flask should be in the `requirements.txt`):
   ```shell
   pip install -r requirements.txt
   ```
6. To run the Sentiment Analysis API:
   ```shell
   python app.py
   ```

Upon launching the API, navigate to `localhost:5000` to see a welcome message. For sentiment analysis, use the route `localhost:5000/analyze_sentiment/YourTextHere`.

## Description

The Sentiment Analysis API provides sentiment classification (Positive, Negative, Neutral) for any given text. The repository also contains a simple AI model simulation with two functions (`run_ai_model_sum` and `run_ai_model_minus`). These functions are decorated with `log_io`, which prints input and output values to the console.

## Notes

While the Flask API can be accessed via a browser or tools like Postman, the AI model simulation is designed for demonstration purposes. Running the code will execute the AI model functions, and you'll observe the logging in action.

If you face any issues or have suggestions, be sure to reach out for help.