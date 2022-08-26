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
            "rule_name": "Suspicious Parent-Child Relationship",
            "rule_id": "18a26e3e-e535-4d23-8ffa-a3cdba56d16e",
        },
        {
            "rule_name": "Binary Masquerading via Untrusted Path",
            "rule_id": "35dedf0c-8db6-4d70-b2dc-a133b808211f",
        },
        {
            "rule_name": "UAC Bypass via ICMLuaUtil Elevated COM Interface",
            "rule_id": "13fab475-06e4-4ac9-87fc-2105c7441244",
        },
    ],
}
TACTICS = ["TA0005", "TA0004"]
RTA_ID = "e0e95f35-173d-4545-a1cc-ee35ee1d89b1"
EXE_FILE = common.get_path("bin", "renamed_posh.exe")


@common.requires_os(PLATFORMS)
def main():
    dllhost = "C:\\Users\\Public\\dllhost.exe"
    common.copy_file(EXE_FILE, dllhost)

    common.execute(
        [dllhost, "/c", "echo 3E5FC7F9-9A51-4367-9063-A120244FBEC7; powershell"],
        timeout=2,
        kill=True,
    )
    common.remove_file(dllhost)


if __name__ == "__main__":
    exit(main())
