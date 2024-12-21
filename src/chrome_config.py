from typing import Any

from collections.abc import Generator
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from contextlib import contextmanager
from typing import Any
import subprocess


@contextmanager
def get_driver() -> Generator[WebDriver, Any, None]:
    proxy_host = "127.0.0.1"
    proxy_port = "8090"

    mitmproxy_command = [
        "mitmproxy",
        "--listen-port",
        proxy_port,
        "-s",
        "src/mitm_script.py",
        "--quiet",  # Adiciona o parâmetro --quiet
    ]
    mitmproxy_process = subprocess.Popen(mitmproxy_command)

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-animations")
    chrome_options.add_argument("--disable-cache")
    chrome_options.add_argument("--disable-prefetch")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument(f"--proxy-server={proxy_host}:{proxy_port}")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        yield driver
    finally:
        mitmproxy_process.kill()
        mitmproxy_process.wait()
        driver.quit()
        print("mitmproxy and driver closed")
