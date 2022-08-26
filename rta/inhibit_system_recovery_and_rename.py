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
            "rule_name": "Inhibit System Recovery Followed by a Suspicious File Rename",
            "rule_id": "92f114fb-7113-4e82-b021-6c2c4ca0a507",
        }
    ],
}
TACTICS = ["TA0040"]
RTA_ID = "43331e29-57ba-438f-8d61-99f5d6471aaa"


@common.requires_os(PLATFORMS)
def main():
    vssadmin = "C:\\Windows\\System32\\vssadmin.exe"
    powershell = "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"
    png = "C:\\Windows\\System32\\SecurityAndMaintenance.png"
    tmppng = "C:\\Users\\Public\\SecurityAndMaintenance.png"
    renamed = "C:\\Users\\Public\\renamed.encrypted"
    common.copy_file(png, tmppng)

    # Execute command
    common.log("Deleting Shadow Copies using Vssadmin spawned by cmd")
    common.execute(
        [powershell, "/c", vssadmin, "delete", "shadows", "/For=C:"], timeout=10
    )

    common.log("Renaming image to unknown extension")
    common.execute([powershell, "/c", f"Rename-Item {tmppng} {renamed}"], timeout=10)

    common.remove_file(renamed)


if __name__ == "__main__":
    exit(main())
