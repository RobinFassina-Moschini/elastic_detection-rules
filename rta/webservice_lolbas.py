# Copyright Elasticsearch B.V. and/or licensed to Elasticsearch B.V. under one
# or more contributor license agreements. Licensed under the Elastic License
# 2.0; you may not use this file except in compliance with the Elastic License
# 2.0.

from . import common

PLATFORMS = ["windows"]
TRIGGERED_RULES = {
    "SIEM": [],
    "ENDPOINT": [
        {
            "rule_name": "External IP Address Discovery via a Trusted Program",
            "rule_id": "51894221-7657-4b56-9406-e080e19ad159",
        },
        {
            "rule_name": "Connection to WebService by a Signed Binary Proxy",
            "rule_id": "c567240c-445b-4000-9612-b5531e21e050",
        },
    ],
}
TACTICS = ["TA0005", "TA0007", "TA0011"]
RTA_ID = "b7a7d246-b1ef-4d08-85ce-92e1cfc18520"


@common.requires_os(PLATFORMS)
def main():
    powershell = "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"

    # Execute command
    common.log("Retrieving the public IP Address using ipify")
    common.execute(
        [powershell, "/c", "iwr", "http://api.ipify.org/", "-UseBasicParsing"],
        timeout=10,
    )


if __name__ == "__main__":
    exit(main())
