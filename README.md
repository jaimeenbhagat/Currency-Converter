# Real-Time Currency Converter

## Introduction

Welcome to the Real-Time Currency Converter! This is a simple Python-based GUI application that allows you to convert amounts from one currency to another using real-time exchange rates. The application is built using the `tkinter` library for the graphical user interface and fetches exchange rates using the ExchangeRate-API.

## Features

- Convert amounts between multiple currencies in real-time.
- User-friendly graphical interface.
- Easy-to-use dropdown menus for selecting currencies.
- Clear button to reset the input fields.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- `requests` library (to install, use: `pip install requests`)

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/real-time-currency-converter.git
   cd real-time-currency-converter
   ```

2. **Install required dependencies:**
   ```sh
   pip install requests
   ```

## Usage

1. **Run the application:**
   ```sh
   python currency_converter.py
   ```

2. **Using the application:**
   - Enter the amount you want to convert in the "Amount" field.
   - Select the currency you are converting from using the "From Currency" dropdown menu.
   - Select the currency you are converting to using the "To Currency" dropdown menu.
   - Click the "Convert" button to perform the conversion.
   - The converted amount will be displayed in the "Converted Amount" field.
   - Use the "Clear" button to reset the input fields.

## Code Overview

The application consists of a single Python file `currency_converter.py`. The main components of the code are:

- **GUI Setup:** Setting up the main window and layout using `tkinter`.
- **Currency Conversion Function:** Fetching real-time exchange rates and performing the conversion.
- **Clear Function:** Clearing the input and output fields.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. **Fork the repository:**
   - Click the "Fork" button at the top right of this page.

2. **Clone the forked repository:**
   ```sh
   git clone https://github.com/your-username/real-time-currency-converter.git
   cd real-time-currency-converter
   ```

3. **Create a new branch:**
   ```sh
   git checkout -b feature-branch-name
   ```

4. **Make your changes and commit:**
   ```sh
   git add .
   git commit -m "Add a descriptive commit message"
   ```

5. **Push to the branch:**
   ```sh
   git push origin feature-branch-name
   ```

6. **Submit a pull request:**
   - Open a pull request on the original repository with a description of your changes.


---

Feel free to reach out if you have any questions or need further assistance. Happy coding!

---

By including this README file in your GitHub repository, you provide clear instructions and information for users and contributors, making your project more accessible and easier to use.
