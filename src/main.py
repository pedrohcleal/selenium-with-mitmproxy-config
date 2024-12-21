from chrome_config import get_driver
from time import sleep
import os, json
from pprint import pprint


if __name__ == "__main__":
    with get_driver() as driver:
        driver.get("https://www.kabum.com.br/computadores")
        sleep(5)
        last_file = sorted(os.listdir("products"))[-1]
        arq_json = json.loads(open(f"products/{last_file}").read())
        pprint(arq_json)
