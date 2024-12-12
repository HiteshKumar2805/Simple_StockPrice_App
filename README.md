# Simple Stock Price App

This is a simple web application built using **Streamlit** and **yfinance**. The app displays the closing prices and trading volume of Google's stock (GOOGL) over a specified time period.

---

## Features
- **Fetch Stock Data**: Automatically retrieves historical stock data for Google (GOOGL) using the `yfinance` library.
- **Interactive Charts**:
  - **Closing Price Chart**: A line chart displaying daily closing prices.
  - **Volume Chart**: A line chart showing the daily trading volume.
- **Streamlit Interface**: Provides a clean and interactive user interface.

---

## Installation

Follow the steps below to set up and run the application:

### Prerequisites
- Python 3.7 or above installed on your system.
- Libraries:
  - `streamlit`
  - `yfinance`
  - `pandas`

### Steps
1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Install required libraries:
   ```bash
   pip install streamlit yfinance pandas
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

4. Open the URL displayed in the terminal (usually `http://localhost:8501`) in your web browser to view the app.

---

## Code Overview

### 1. **Dependencies**
The application uses the following Python libraries:
- **yfinance**: Fetches stock market data programmatically.
- **streamlit**: Creates an interactive web app interface.
- **pandas**: Handles stock data in tabular format.

### 2. **Fetching Stock Data**
The stock data for Google is fetched using:
```python
import yfinance as yf

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDF = tickerData.history(period='1d', start='2010-5-31', end='2024-5-31')
```
This retrieves daily historical data, including **open**, **high**, **low**, **close**, and **volume**.

### 3. **Visualization**
The app displays two charts:
- **Closing Price Chart**:
  ```python
  st.line_chart(tickerDF.Close)
  ```
- **Volume Chart**:
  ```python
  st.line_chart(tickerDF.Volume)
  ```

---

## Example Output

### Closing Price Chart
This chart shows Google's daily closing prices from 2010 to 2024.

### Volume Chart
This chart shows the daily trading volume over the same period.

---

## How to Extend the Application
Here are some ways you can enhance the app:
1. **User Input**: Allow users to enter a stock ticker symbol and select a custom date range.
2. **Additional Metrics**: Include charts for other financial metrics like **Open**, **High**, and **Low**.
3. **Download Data**: Provide an option to download the fetched data as a CSV file.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contributing
If you'd like to contribute to this project, feel free to open a pull request or report issues.

---

## Author
Created by [Your Name].

