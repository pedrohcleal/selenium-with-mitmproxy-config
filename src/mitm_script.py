import json
from datetime import datetime
from mitmproxy import http
from time import sleep


def response(flow: http.HTTPFlow):
    if "servicespub.prod.api.aws" in flow.request.url:
        response_info = {
            "Host": flow.request.host,  # Não precisa de json.loads
            "Path": flow.request.path,  # Não precisa de json.loads
            "URL": flow.request.url,  # Não precisa de json.loads
            "Status": flow.response.status_code,  # Não precisa de json.loads
            "Headers": dict(
                flow.response.headers
            ),  # Converta para dict, pois headers podem ser um objeto especial
            "Body": json.loads(flow.response.text),  # Mantenha como texto puro
        }

        date_now = datetime.now().strftime("%Y%m%d-%H%M%S")
        with open(f"products/{date_now}.json", "w", encoding="utf-8") as f:
            json.dump(response_info, f, indent=4, ensure_ascii=False)
            print("JSON saved successfully.")
        sleep(1)
