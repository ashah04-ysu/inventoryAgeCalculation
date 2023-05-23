# Inventory Age Calculation

This Python module calculates the age of inventory items based on event dates and types. It takes a sample dataset from Table 1, performs calculations, and generates a summary table.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Sample Data](#sample-data)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Inventory management is crucial for businesses to maintain optimal stock levels and understand the age distribution of their inventory. This module provides a solution to calculate the age of inventory items based on event dates and types, allowing businesses to gain insights into inventory aging.

## Installation

1. Make sure you have Python 3 installed on your system.
2. Clone this repository or download the `inventory_age_calculation.py` file.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where `inventory_age_calculation.py` is located.
3. Run the following command to execute the module:
    ```bash
    python inventory_age_calculation.py
    ```
4. The module will calculate the age of the inventory items and display a summary table with counts for different age ranges.

## Sample Data

The module uses a sample dataset from Table 1 to perform calculations. The data is represented as a list of dictionaries, where each dictionary represents an inventory entry with the following fields:
- ID: Identifier for the inventory item.
- OnHandQuantity: The current quantity on hand for the item.
- OnHandQuantityDelta: The change in quantity for the item due to an event.
- event_type: The type of event (InBound or OutBound).
- event_datetime: The date and time of the event.

Feel free to modify the sample data in the `inventory_age_calculation.py` file to analyze different datasets.

## Contributing

Contributions are welcome! If you have any ideas, improvements, or bug fixes, please open an issue or submit a pull request. Please make sure to follow the existing code style and provide clear commit messages.

## License

This project is licensed under the [MIT License](LICENSE).

