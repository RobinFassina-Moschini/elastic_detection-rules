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
        }
    ],
}
TACTICS = ["TA0005"]
RTA_ID = "b12372b8-0e76-4b3d-9dfc-880664893eb9"
EXE_FILE = common.get_path("bin", "renamed_posh.exe")


@common.requires_os(PLATFORMS)
def main():
    posh = "C:\\Users\\Public\\posh.exe"
    tiworker = "C:\\Users\\Public\\TiWorker.exe"
    common.copy_file(EXE_FILE, posh)
    common.copy_file(EXE_FILE, tiworker)

    # Execute command
    common.execute([posh, "/c", tiworker], timeout=3, kill=True)
    common.remove_files(posh, tiworker)


if __name__ == "__main__":
    exit(main())
