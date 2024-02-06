#!/usr/bin/env python3

import sys
import whois

def usage():
    script_name = "whois.py"
    print(f"Usage: {script_name} <target>\n")
    print(f"Example: {script_name} 192.168.0.1")
    print(f"Example: {script_name} duckduckgo.com")

def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    target = sys.argv[1]
   
    res = whois.query(target)
    print(res)

main()