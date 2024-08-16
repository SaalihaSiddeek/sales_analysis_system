# Sales Data Analysis System

This command-line interface-based sales data analysis system has been developed for a large supermarket network. The system is designed to automate and enhance the monthly sales data analysis process, addressing inefficiencies and errors that existed in the previous manual system. It is built using Python and implements a strategy-based approach to perform various types of sales analyses efficiently.

## Key Features:
The system provides the following key functionalities:

### 1. Monthly Sales Analysis by Branch:
- Allows users to analyze the sales of each branch for a selected month.
- The analysis shows the total sales (in terms of product quantities) of all branches during the month.
- Displays the analysis results both in tabular form and as a bar chart.

### 2. Price Analysis of Products:
- Enables users to track the price of a specific product over a selected period.
- Shows daily price changes and trends for the selected product.
- Displays the analysis results using a line graph.

### 3. Weekly Sales Analysis of the Supermarket Network:
- Analyzes the weekly sales data for a specific week of a given month.
- Provides a summary of sales for each branch during the week.
- Displays results in tabular form and a bar chart.

### 4. Product Preference Analysis:
- Analyzes the total quantity sold of each product across all branches.
- Highlights the most preferred and popular products among customers.
- Displays results in tabular form and as a bar chart.

### 5. Distribution of Sales Amount by Branch:
- Provides a distribution analysis of the total sales amount for each branch.
- Displays the analysis results as a pie chart representing the proportion of sales per branch.

## System Overview:

The system is built on an object-oriented design, using Python's `ABC` module to implement an abstract base class for different analysis types. The system includes five analysis classes: `BranchAnalysis`, `PriceAnalysis`, `WeeklyAnalysis`, `PreferenceAnalysis`, and `DistributionAnalysis`. 

The `StrategySelector` class provides a menu-driven interface for users to select and execute the desired analysis. The system is highly extensible and can easily be modified to include new types of analyses in the future.

## Usage:
1. Upon starting the system, the user is prompted to log in with a predefined username and password.
2. Once authenticated, the system provides a menu with options for different types of sales analysis.
3. The user selects the type of analysis and inputs the required parameters (e.g., year, month, product name, starting day of the week).
4. The system performs the selected analysis, displaying the results in both tabular and graphical forms.
5. The user can return to the main menu to perform another analysis or exit the system.

## Sample Data:
The system uses sales data stored in a CSV file (`Food_City.csv`). Each record in the CSV file represents a transaction, with fields such as:
- Year
- Month
- Day
- Branch
- Product
- Quantity
- Price

The analysis operations are performed using the `pandas` library for data manipulation and `matplotlib` for visualizing the results.

## Technology Stack:
- **Programming Language**: Python
- **Libraries**: pandas, matplotlib
- **Data Source**: CSV files

## How to Run:
1. Clone the repository.
2. Ensure you have the required Python libraries installed:
   ```bash
   pip install pandas matplotlib
