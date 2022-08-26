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
            "rule_name": "Credential Access via Known Utilities",
            "rule_id": "3c44fc50-2672-48b3-af77-ff43b895ac70",
        }
    ],
}
TACTICS = ["TA0006"]
RTA_ID = "374718be-d841-4381-a75f-ef54f0d5eb18"
EXE_FILE = common.get_path("bin", "renamed.exe")


@common.requires_os(PLATFORMS)
def main():
    binary = "ProcessDump.exe"
    common.copy_file(EXE_FILE, binary)

    # Execute command
    common.execute([binary], timeout=5, kill=True)

    common.remove_files(binary)


if __name__ == "__main__":
    exit(main())
