#! /usr/bin/env nix-shell
#! nix-shell -i python3 -p python3Packages.requests

import datetime
import json
import time
from typing import Literal, Union

import requests

LAST = 4154
SLEEP = 0.1 # 0.1 = 1s, limite legerement en dessous de 1s

def main(
    querying: Union[Literal["cpu"], Literal["gpu"]],
    filename: str,
    last_id: int,
    sleep_time: float = 1,
):
    """Make an API call every `sleep_time` (in seconds) and save the aggregated JSON to `{filename}_{current_time}.json`."""

    credentials = {
        "api_key": "1_oZWfpb7IQ05lF9iKPMExhQHxz4BoVrucc74NPiBJYZIBOu1ZhHbwJApZeQq1x7SBWutYSFEbwvXW5xiR0BJwwdzIYHmXGPGY1a82U0CQWs6hCzQ92lvqIUXjJjumXrF3"
    }
    result = []

    print(f"querying {querying}")

    try:
        for id in range(1, last_id + 1):
            r = requests.get(
                f"https://fr.gamesplanet.com/api/v1/techs/{querying}_details/{id}",
                params=credentials,
            )

            response = r.json()
            if response["status"] == "success":
                print(f"id {id}: success")
                result.append(response["result"])

            time.sleep(sleep_time)
    finally:
        print("writing")
        now = "2025-09-24"
        with open(f"{filename}_{now}.json", "w") as file:
            json.dump(result, file)

if __name__ == "__main__":
#   main("gpu", filename="metaboli_gpu", last_id=LAST, sleep_time=SLEEP)
    main("cpu", filename="metaboli_cpu", last_id=LAST, sleep_time=SLEEP)