import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
file_path = "data/Fuel_cell_performance_data-Full.csv"
df = pd.read_csv(file_path)

# Define roll number and determine the target column
roll_number = "102203973"
last_digit = int(roll_number[-1])

# Map roll number's last digit to the corresponding target
target_map = {
    0: "Target1", 5: "Target1",
    1: "Target2", 6: "Target2",
    2: "Target3", 7: "Target3",
    3: "Target4", 8: "Target4",
    4: "Target5", 9: "Target5"
}
target_column = target_map.get(last_digit, None)

# Ensure the target column exists
if target_column is None or target_column not in df.columns:
    raise ValueError(f"Target column '{target_column}' not found in the dataset.")

# Preprocess data
df = df.dropna()  # Remove rows with missing values
X = df.drop(columns=[col for col in df.columns if col.startswith("Target")])
y = df[target_column]

# Split data into training and testing sets (70/30 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize models
models = {
    "LinearRegression": LinearRegression(),
    "DecisionTree": DecisionTreeRegressor(random_state=42),
    "KNeighbors": KNeighborsRegressor(n_neighbors=5)
}

# Train and evaluate each model
performance = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    performance[name] = {"MSE": mse, "R2": r2}

# Display results
print("Model Evaluation Results:")
for model_name, metrics in performance.items():
    print(f"\n{model_name}")
    print(f"Mean Squared Error: {metrics['MSE']:.2f}")
    print(f"R² Score: {metrics['R2']:.4f}")
