#!/usr/bin/env python3
# Author - Graham McMillan
# Date 19/07/2019

import requests
import json
from argparse import ArgumentParser

apiKey = ""
baseUrl = ""
headers = {'Accept': 'application/json',
           'X-Api-Key': apiKey,
           'Content-Type': 'application/json'}

parser = ArgumentParser(description="Name of A record")
parser.add_argument('domain', type=str, help="Enter the name of the A record")
parser.add_argument('ipaddr', type=str,
                    help="Enter the ip of the server")
parser.add_argument('recordType', nargs='?', default="A", type=str,
                    help="Enter the type of record")

args = parser.parse_args()
domain = str(args.domain)
ipaddr = str(args.ipaddr)
recordType = str(args.recordType)


def add_record(domain, ipaddr, recordType):
    record = {'rrset_name': domain,
              'rrset_type': recordType,
              'rrset_ttl': 300,
              'rrset_values': [ipaddr]}

    r = requests.post(baseUrl, data=json.dumps(record), headers=headers)

    if r.ok:
        print(f"New record for {domain} added successfully")
    else:
        print("There was an issue adding the record",
              "\nStatus code:", r.status_code)
        print(r.json())
        return 1


add_record(domain, ipaddr, recordType)
