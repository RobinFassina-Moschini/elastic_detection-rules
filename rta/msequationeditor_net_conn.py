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
            "rule_name": "Suspicious Network Connection from Microsoft Equation Editor",
            "rule_id": "365571bb-2b93-4ae8-8c39-0558f8a6c4cc",
        }
    ],
}
TACTICS = ["TA0002", "TA0001"]
RTA_ID = "75167553-4886-44ba-b5d6-b4c341b33709"
EXE_FILE = common.get_path("bin", "regsvr32.exe")


@common.requires_os(PLATFORMS)
def main():
    eqnedt32 = "C:\\Users\\Public\\eqnedt32.exe"

    common.copy_file(EXE_FILE, eqnedt32)
    common.log("Making connection using fake eqnedt32.exe")
    common.execute([eqnedt32, "-Embedding"], timeout=10, kill=True)


if __name__ == "__main__":
    exit(main())
