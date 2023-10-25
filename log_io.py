def log_io(func):
    # print("firing decorator")

    def wrapper(*args, **kwargs):
        # print("firing decorator")
        print(f"Input: {args}")
        result = func(*args, **kwargs)
        print(f"Output: {result}")
        return result
    return wrapper


@log_io
def run_ai_model_sum(data):
    # Simulate a simple AI model's prediction function.
    prediction = sum(data) * 2
    return prediction


@log_io
def run_ai_model_minus(data):
    # Simulate a simple AI model's prediction function.
    prediction = min(data)
    return prediction


# Simulate sending data to the AI model for prediction.
data = [1, 2, 3, 4, 5]
prediction_result = run_ai_model_sum(data)
prediction_result_min = run_ai_model_minus(data)
