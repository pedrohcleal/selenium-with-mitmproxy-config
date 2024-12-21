# Selenium with MITM Proxy

This project demonstrates how to integrate [Selenium](https://www.selenium.dev/) with [MITM Proxy](https://mitmproxy.org/) for intercepting and saving HTTP responses. The application fetches product data from the Kabum website and logs it into JSON files for further analysis.

## Project Structure

```
.
├── src
│   ├── main.py            # Entry point of the application
│   ├── chrome_config.py   # Selenium Chrome driver configuration with proxy
│   ├── mitm_script.py     # MITM Proxy script for intercepting HTTP responses
├── products               # Directory where JSON files are saved
```

## Prerequisites

- Python 3.9+
- Google Chrome installed
- [MITM Proxy](https://mitmproxy.org/) installed
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager) for managing ChromeDriver

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

1. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

1. Install MITM Proxy:

   ```bash
   pip install mitmproxy
   ```

## Usage

1. Start the application:

   ```bash
   python src/main.py
   ```

   This will:

   - Launch MITM Proxy on port 8090.
   - Open the Kabum website using a headless Chrome browser.
   - Save intercepted HTTP response data as JSON files in the `products` directory.

1. View the generated JSON files:

   - Navigate to the `products` directory to find the intercepted data.

## Code Overview

### `src/main.py`

This script initializes the Selenium driver, navigates to the Kabum website, and processes the latest JSON file.

### `src/chrome_config.py`

Sets up a Selenium Chrome driver with the MITM Proxy configuration. Key features include:

- Headless browser mode.
- Custom proxy settings for MITM Proxy.

### `src/mitm_script.py`

A MITM Proxy script to intercept HTTP responses, parse the data, and save it to JSON files. Key features:

- Filters requests to specific URLs.
- Logs HTTP status, headers, and response body.

## Example Output

The output JSON files in the `products` directory will look like this:

```json
{
    "Host": "servicespub.prod.api.aws",
    "Path": "/api/path",
    "URL": "https://servicespub.prod.api.aws/api/path",
    "Status": 200,
    "Headers": {
        "Content-Type": "application/json"
    },
    "Body": {
        "key": "value"
    }
}
```

## Notes

- Ensure MITM Proxy is properly installed and accessible in your system's PATH.
- Modify the `response` function in `src/mitm_script.py` to handle additional response formats as needed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
