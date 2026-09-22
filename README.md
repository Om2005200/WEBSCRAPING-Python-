# 📊 NIFTY 50 Historical Data Scraper

A Python-based web scraping and data-processing project that retrieves **historical NIFTY 50 index data from the NSE India website**, stores the raw API response as JSON, and converts the data into a structured CSV dataset using Pandas.

The project is designed as a simple data pipeline:

**NSE India → API Response → JSON → Pandas → Clean CSV Dataset**

---

## 🚀 Features

* Fetches historical **NIFTY 50 index data** from NSE India.
* Uses `requests.Session()` to maintain a persistent HTTP session.
* Sends browser-like HTTP headers with the request.
* Retrieves data directly from the NSE historical index API.
* Stores the raw API response in JSON format.
* Uses Pandas to normalize nested JSON data.
* Renames NSE API fields into simpler column names.
* Extracts important OHLC and trading-volume information.
* Converts timestamps into Pandas datetime format.
* Sorts records chronologically.
* Preserves previously collected CSV data.
* Combines newly scraped data with existing data.
* Removes duplicate records based on the date.
* Produces a clean CSV dataset suitable for further analysis.

---

## 🛠️ Technologies Used

* **Python**
* **Requests** — API requests and HTTP sessions
* **Pandas** — data processing and CSV generation
* **JSON** — raw API response storage
* **CSV** — structured dataset storage

---

## 📁 Project Flow

```text
                    NSE India
                        │
                        ▼
              Historical Index API
                        │
                        ▼
                 requests.Session()
                        │
                        ▼
                 JSON API Response
                        │
                        ▼
              Raw JSON Data File
                        │
                        ▼
               pandas.json_normalize()
                        │
                        ▼
                Column Renaming
                        │
                        ▼
                  Data Cleaning
                        │
                        ▼
              Duplicate Removal
                        │
                        ▼
                 Sorted CSV File
```

---

## 🔗 NSE Endpoints

The project uses two NSE URLs.

### NSE Historical Index Data Page

```text
https://www.nseindia.com/reports-indices-historical-index-data
```

### Historical Index API

```text
https://www.nseindia.com/api/historicalOR/indicesHistory
```

The API request contains parameters such as:

```text
indexType=NIFTY 50
from=11-02-2026
to=12-02-2026
```

This allows the scraper to request historical NIFTY 50 data for a specified date range.

---

## 📦 Raw JSON Data

The API response is first received as JSON:

```python
json_data = response2.json()
```

The raw response can then be stored in:

```text
nifty_50_raw_data.json
```

This keeps the original API response available before further processing.

---

## 🧹 Data Processing

The JSON response contains the actual records inside the `data` field.

Pandas is used to normalize this nested structure:

```python
result = pd.json_normalize(data['data'])
```

This converts the list of dictionaries into a Pandas DataFrame.

---

## 🔄 Column Transformation

The original NSE API column names are converted into simpler names:

| NSE API Column        | Dataset Column |
| --------------------- | -------------- |
| `EOD_TIMESTAMP`       | `DATE`         |
| `EOD_INDEX_NAME`      | `INDEX`        |
| `EOD_OPEN_INDEX_VAL`  | `OPEN`         |
| `EOD_HIGH_INDEX_VAL`  | `HIGH`         |
| `EOD_LOW_INDEX_VAL`   | `LOW`          |
| `EOD_CLOSE_INDEX_VAL` | `CLOSE`        |
| `HIT_TURN_OVER`       | `TURNOVER`     |
| `HIT_TRADED_QTY`      | `VOLUME`       |
| `HI_TIMESTAMP`        | `RAW_TIME`     |

The final dataset contains:

```text
DATE
INDEX
OPEN
HIGH
LOW
CLOSE
TURNOVER
VOLUME
RAW_TIME
```

---

## 📈 Example Dataset

The resulting CSV will have a structure similar to:

```text
DATE,INDEX,OPEN,HIGH,LOW,CLOSE,TURNOVER,VOLUME,RAW_TIME
2026-02-11,NIFTY 50,....,....,....,....,....,....,....
2026-02-12,NIFTY 50,....,....,....,....,....,....,....
```

The actual values are obtained directly from the NSE API.

---

## 🔁 Updating Existing Data

The scraper can also work with an existing CSV file.

If the CSV already exists:

1. Existing CSV data is loaded.
2. Newly scraped data is generated.
3. Both datasets are combined.
4. Duplicate dates are removed.
5. The complete dataset is sorted chronologically.
6. The updated dataset is written back to the CSV.

Conceptually:

```text
Existing CSV
     │
     ├──────────────┐
     │              │
     ▼              ▼
Old Data        New Data
     │              │
     └──────┬───────┘
            ▼
       Concatenate
            │
            ▼
     Remove duplicates
            │
            ▼
      Sort by DATE
            │
            ▼
       Updated CSV
```

---

## 📂 Output Files

The project is designed to generate:

```text
nifty_50_raw_data.json
nifty_50.csv
```

### `nifty_50_raw_data.json`

Contains the raw response received from the NSE API.

### `nifty_50.csv`

Contains the cleaned and structured historical NIFTY 50 dataset.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

### 2. Install dependencies

```bash
pip install requests pandas
```

### 3. Run the Python script

```bash
python scraper.py
```

The script will request the data from NSE and process the response into the output files.

---

## ⚙️ Changing the Date Range

The historical period can be changed through the API URL:

```python
url2 = 'https://www.nseindia.com/api/historicalOR/indicesHistory?indexType=NIFTY%2050&from=11-02-2026&to=12-02-2026'
```

For example:

```text
from=01-01-2026
to=31-01-2026
```

This allows the scraper to collect a different historical period.

---

## 🧠 What I Learned From This Project

This project demonstrates several important concepts:

* Working with REST APIs
* Using HTTP sessions
* Understanding HTTP response status codes
* Working with JSON responses
* Converting nested JSON into tabular data
* Pandas DataFrame manipulation
* Data cleaning
* Date/time conversion
* Sorting datasets
* Combining old and new datasets
* Removing duplicate records
* Building a simple data-ingestion pipeline

---

## ⚠️ Disclaimer

This project is intended for **educational and research purposes**.

The data is retrieved from NSE India endpoints and should be used in accordance with the applicable NSE terms, policies, and access requirements.

This project is **not affiliated with or endorsed by NSE India**.

---

## 📌 Future Improvements

Possible improvements include:

* Automatic date-range generation
* Automated historical data backfilling
* Better error handling
* Retry logic for failed requests
* Request throttling
* Logging
* Data validation
* Configurable index selection
* Automated scheduled data collection
* Database storage instead of CSV
* Support for additional NSE indices

---
