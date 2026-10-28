Mobile Phone Data Scraper

A Python web scraping project that extracts mobile phone information from "Technolife" (https://www.technolife.com/) and stores the collected data in an SQLite database.

The project uses BeautifulSoup to parse HTML content, Requests to retrieve webpage data, and a custom database management class to store extracted records.

✨ Features

- Web Scraping: Retrieves mobile phone listings from Technolife.
- HTML Parsing: Uses BeautifulSoup to extract product information from HTML elements.
- Brand Extraction: Identifies the brand from the product description.
- Memory Information: Extracts available memory information from product listings.
- RAM Extraction: Identifies RAM capacity from product descriptions.
- Rating Extraction: Collects product ratings.
- SQLite Integration: Stores extracted information in a local SQLite database.
- Database Management: Uses a custom "Database_control" class for database initialization and record insertion.
- Error Handling: Handles database operation errors and reports failures.

🛠️ Technologies

- Python
- Requests
- BeautifulSoup4
- SQLite3

⚙️ Installation

Make sure Python is installed on your system.

Install the required third-party libraries:

pip install requests beautifulsoup4

SQLite3 is included with standard Python installations, so no separate Python package is required for "sqlite3".

📁 Project Structure

mobile-phone-scraper/
├── main.py
├── db_management.py
├── Mobile.db
└── README.md

- "main.py": Retrieves and parses mobile phone listings, extracts product information, and saves records to the database.
- "db_management.py": Defines the "Database_control" class for SQLite database operations.
- "Mobile.db": Created automatically when the database is initialized. It does not need to exist before the first run.

▶️ Usage

1. Install the required dependencies.
2. Place "main.py" and "db_management.py" in the same directory.
3. Run the scraper:

python main.py

The program retrieves the mobile phone listing page, extracts information from the matching product cards, and attempts to insert the collected records into "Mobile.db".

The database contains a "mobile" table with the following columns:

Column| Type| Description
"id"| INTEGER| Product record ID
"description"| TEXT| Product description
"brand"| TEXT| Extracted brand
"memory"| TEXT| Memory information
"ram"| TEXT| RAM capacity
"rating"| REAL| Product rating

🧠 How It Works

1. Retrieve the Webpage

The Requests library sends an HTTP GET request to the mobile phone category page, using a browser-like "User-Agent" header.

2. Parse the HTML

BeautifulSoup parses the returned HTML using Python's built-in HTML parser.

CSS selectors identify product cards and retrieve relevant information from their elements.

3. Extract Product Information

For each matching product card, the scraper attempts to extract:

- Product description
- Brand
- Memory information
- RAM capacity
- Rating

The description is split into individual words to identify the brand and RAM capacity. Products that do not match the expected RAM description format are skipped.

4. Store Records in SQLite

The "Database_control" class initializes the database table and inserts extracted records using parameterized SQL queries.

The database operations are separated from the scraping logic, making the code easier to organize and extend.

⚠️ Limitations

- The scraper relies on the current HTML structure and CSS selectors of Technolife's webpage.
- Changes to the website may cause some fields to be missing or extracted incorrectly.
- Product information is extracted using text positions and formatting assumptions, which may not work for every listing.
- The current implementation does not check whether a product has already been stored before inserting it.
- The scraper does not implement pagination or automatic retries.
- Network failures and HTTP error responses are not explicitly handled in the scraping section.
- The database retrieval method currently executes a query but does not return the retrieved record.

🚀 Possible Improvements

- Add HTTP status-code checks and request timeouts.
- Handle missing HTML elements safely.
- Improve brand, RAM, and memory extraction using more robust parsing logic.
- Add duplicate detection and update existing product records.
- Implement pagination to collect products from multiple pages.
- Add database methods for retrieving, updating, and deleting product records.
- Export collected information to CSV or JSON.
- Add logging instead of relying on printed error messages.

📄 License

No license has been specified yet. Add a license file if you intend to define the terms under which others may use, modify, or distribute this project.
