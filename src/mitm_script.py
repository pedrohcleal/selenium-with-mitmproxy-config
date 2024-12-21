import json
from datetime import datetime
from mitmproxy import http
from time import sleep


def response(flow: http.HTTPFlow):
    if "servicespub.prod.api.aws" in flow.request.url:
        response_info = {
            "Host": flow.request.host,
            "Path": flow.request.path,
            "URL": flow.request.url,
            "Status": flow.response.status_code,
            "Headers": dict(
                flow.response.headers
            ),
            "Body": json.loads(flow.response.text),
        }

        date_now = datetime.now().strftime("%Y%m%d-%H%M%S")
        with open(f"products/{date_now}.json", "w", encoding="utf-8") as f:
            json.dump(response_info, f, indent=4, ensure_ascii=False)
            print("JSON saved successfully.")
        sleep(1)
