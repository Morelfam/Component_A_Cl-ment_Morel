# Component A: Price Moving-Average Analysis

This project reads daily closing prices from a CSV file, calculates a 20-trading-day simple moving average, and saves a chart showing the closing price with the moving average overlay.

## Requirements

- Python 3
- The packages listed in `requirements.txt`

## Setup

From the project root, create and activate a virtual environment, then install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run

Run the analysis from the project root:

```bash
python src/analysis.py
```

The chart is saved to `outputs/plot.png`. The output directory is created automatically if it does not exist.

## Input Data

The script reads `data/prices.csv`. It must contain these columns:

| Column | Description |
| --- | --- |
| `date` | Date for each observation, parseable as a date |
| `close` | Numeric closing price |

Rows are sorted by date before the moving average is calculated. The first 19 rows have no 20-day average because there are not yet enough observations.

## Configuration

Change the `WINDOW` value near the top of `src/analysis.py` to use a different moving-average period. The plot title and legend use that configured value.

## Project Layout

```text
data/prices.csv       Input price data
outputs/plot.png      Generated chart
src/analysis.py       Analysis and plotting script
requirements.txt      Python dependencies
```