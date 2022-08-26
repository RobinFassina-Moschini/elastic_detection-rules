# Copyright Elasticsearch B.V. and/or licensed to Elasticsearch B.V. under one
# or more contributor license agreements. Licensed under the Elastic License
# 2.0; you may not use this file except in compliance with the Elastic License
# 2.0.

import time

from . import common

PLATFORMS = ["windows"]
TRIGGERED_RULES = {
    "SIEM": [],
    "ENDPOINT": [
        {
            "rule_name": "Scriptlet Execution via Rundll32",
            "rule_id": "93438ae3-becd-43fa-81de-645ce17afa8e",
        },
        {
            "rule_name": "Binary Proxy Execution via Rundll32",
            "rule_id": "f60455df-5054-49ff-9ff7-1dc4e37b6ea7",
        },
    ],
}
TACTICS = ["TA0002", "TA0005"]
RTA_ID = "7d139669-2b4c-4fc3-9a7c-bd1b643696dc"
INF_FILE = common.get_path("bin", "notepad_launch.inf")


def main():
    # http server will terminate on main thread exit
    # if daemon is True
    common.log("RunDLL32 with Script Object and Network Callback")
    server, ip, port = common.serve_web()
    callback = "http://%s:%d" % (ip, port)
    common.clear_web_cache()

    common.patch_regex(INF_FILE, common.CALLBACK_REGEX, callback)

    rundll32 = "rundll32.exe"
    common.execute(
        [
            rundll32,
            "advpack.dll," + "LaunchINFSection",
            INF_FILE + ",DefaultInstall_SingleUser,1,",
        ],
        shell=False,
    )

    time.sleep(1)
    common.log("Cleanup", log_type="-")
    common.execute(["taskkill", "/f", "/im", "notepad.exe"])
    server.shutdown()


if __name__ == "__main__":
    exit(main())
