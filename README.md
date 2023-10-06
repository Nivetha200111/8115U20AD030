URL Number Extractor
URL Number Extractor is a Flask web application that retrieves data from a list of URLs, extracts numbers from JSON responses, and returns a sorted list of unique numbers in JSON format.

Features
Extract Numbers: The app extracts numbers from JSON responses obtained from a list of URLs.

Error Handling: The app gracefully handles errors such as invalid URLs, network issues, and timeouts when fetching data from URLs.

Sorting: The extracted numbers are sorted in ascending order.

Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/url-number-extractor.git
Navigate to the project directory:

bash
Copy code
cd url-number-extractor
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
Activate the virtual environment (optional):

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS and Linux:

bash
Copy code
source venv/bin/activate
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Start the Flask application:

bash
Copy code
python app.py
Open a web browser and access the application at http://localhost:5000/numbers.

Enter a list of URLs as query parameters in the following format:

php
Copy code
http://localhost:5000/numbers?url=<url1>&url=<url2>&url=<url3>
Replace <url1>, <url2>, and <url3> with the URLs you want to process.

The app will retrieve data from the specified URLs, extract numbers from the JSON responses, and return a sorted list of unique numbers in JSON format.

Example