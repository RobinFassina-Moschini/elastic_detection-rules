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
            "rule_name": "Microsoft Office File Execution via Script Interpreter",
            "rule_id": "54aabea0-3687-4ef1-b70c-015ca588e563",
        }
    ],
}
TACTICS = ["TA0001"]
RTA_ID = "3206f2b2-c731-479f-a258-d486dac8a055"
EXE_FILE = common.get_path("bin", "renamed.exe")


@common.requires_os(PLATFORMS)
def main():
    binary = "winword.exe"
    common.copy_file(EXE_FILE, binary)

    # Execute command
    common.log("Dropping executable using fake winword")
    common.execute([binary, "/c", "copy C:\\Windows\\System32\\cmd.exe cmd.exe"])

    common.log("Executing it using scripting program")
    common.execute(
        [
            "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
            "-C",
            ".\\cmd.exe /c exit",
        ]
    )

    common.remove_files(binary, "cmd.exe")


if __name__ == "__main__":
    exit(main())
