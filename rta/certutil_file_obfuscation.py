# Copyright Elasticsearch B.V. and/or licensed to Elasticsearch B.V. under one
# or more contributor license agreements. Licensed under the Elastic License
# 2.0; you may not use this file except in compliance with the Elastic License
# 2.0.

# Name: Certutil Encode / Decode
# RTA: certutil_file_obfuscation.py
# ATT&CK: T1140
# signal.rule.name: Encoding or Decoding Files via CertUtil
# Description: Uses certutil to create an encoded copy of cmd.exe. Then uses certutil to decode that copy.

import os

from . import common

PLATFORMS = [common.WINDOWS]
TRIGGERED_RULES = {
    "SIEM": ["Suspicious CertUtil Commands"],
    "ENDPOINT": []
}

@common.requires_os(PLATFORMS)
def main():
    common.log("Encoding target")
    encoded_file = os.path.abspath('encoded.txt')
    decoded_file = os.path.abspath('decoded.exe')
    common.execute(["c:\\Windows\\System32\\certutil.exe", "-encode", "c:\\windows\\system32\\cmd.exe", encoded_file])

    common.log("Decoding target")
    common.execute(["c:\\Windows\\System32\\certutil.exe", "-decode", encoded_file, decoded_file])

    common.log("Cleaning up")
    common.remove_file(encoded_file)
    common.remove_file(decoded_file)


if __name__ == "__main__":
    exit(main())
