# Fuel Cell Performance Analysis

This repository contains the implementation of predictive modeling on the `Fuel_cell_performance_data-Full.csv` dataset. The objective is to predict specific target variables based on the roll number of the user.

## Dataset Description
The dataset contains performance data of fuel cells along with multiple target variables. Depending on the roll number, a specific target column is chosen for prediction:

- **Target1**: Roll numbers ending with 0 or 5
- **Target2**: Roll numbers ending with 1 or 6
- **Target3**: Roll numbers ending with 2 or 7
- **Target4**: Roll numbers ending with 3 or 8
- **Target5**: Roll numbers ending with 4 or 9

For this project, the roll number used is **102203973**, which selects **Target4**.

## Methodology

### Steps Performed:
1. **Dataset Preprocessing**:
   - Load and clean the dataset (remove missing values).
   - Select the appropriate target column based on the roll number.
   - Standardize the feature values for scaling.
2. **Train-Test Split**:
   - Split the dataset into training (70%) and testing (30%) sets.
3. **Model Selection**:
   - Implemented the following models:
     - Linear Regression
     - Decision Tree Regressor
     - K-Neighbors Regressor
4. **Evaluation**:
   - Evaluate the models using:
     - Mean Squared Error (MSE)
     - R2 Score

## Results
![Results](model%20results/model_results.png)


## How to Run the Code

### Prerequisites:
- Python 3.8+
- Required libraries:
  ```bash
  pip install pandas scikit-learn
  ```

### Steps:
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Fuel-Cell-Performance.git
   cd Fuel-Cell-Performance
   ```
2. Place the `Fuel_cell_performance_data-Full.csv` file in the repository directory.
3. Run the Python script:
   ```bash
   python fuel_cell_analysis.py
   ```
4. View the results printed in the console.

## Repository Structure
```
Fuel-Cell-Performance/
├── fuel_cell_analysis.py   # Main analysis script
├── Fuel_cell_performance_data-Full.csv # Dataset (not included, user-provided)
├── README.md               # Project documentation
```

## Contributing
Feel free to fork this repository and submit pull requests for improvements or additional features.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
