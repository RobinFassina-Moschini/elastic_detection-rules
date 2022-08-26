# Copyright Elasticsearch B.V. and/or licensed to Elasticsearch B.V. under one
# or more contributor license agreements. Licensed under the Elastic License
# 2.0; you may not use this file except in compliance with the Elastic License
# 2.0.

from . import common

PLATFORMS = ["macos"]
TRIGGERED_RULES = {
    "SIEM": [
        {
            "rule_name": "SystemKey Access via Command Line",
            "rule_id": "d75991f2-b989-419d-b797-ac1e54ec2d61",
        }
    ],
    "ENDPOINT": [
        {
            "rule_name": "Suspicious SystemKey Access via Command Line",
            "rule_id": "7d3f98bf-2111-4e5f-9787-9edef8d94dd0",
        }
    ],
}
TACTICS = ["TA0006"]
RTA_ID = "d950ef5f-8277-4ed8-a8dd-d2433e791cef"


@common.requires_os(PLATFORMS)
def main():

    masquerade = "/tmp/bash"
    common.create_macos_masquerade(masquerade)

    # Execute command
    common.log("Launching fake commands to aquire keychain credentials")
    common.execute([masquerade, "/private/var/db/SystemKey"], timeout=10, kill=True)

    # cleanup
    common.remove_file(masquerade)


if __name__ == "__main__":
    exit(main())
