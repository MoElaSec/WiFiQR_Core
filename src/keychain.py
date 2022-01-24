import re
import os


def getpassword(account, service="AirPort"):

    def decode_hex(s):
        s = eval('"' + re.sub(r"(..)", r"\x\1", s) + '"')
        if "" in s:
            s = s[:s.index("")]
        return s

    cmd = ' '.join([
        "/usr/bin/security",
        " find-generic-password",
        "-g -s '%s' -a '%s'" % (service, account),
        "2>&1 >/dev/null"
    ])
    p = os.popen(cmd)
    s = p.read()
    p.close()
    m = re.match(r"password: (?:0x([0-9A-F]+)\s*)?\"(.*)\"$", s)
    if m:
        hexform, stringform = m.groups()
        if hexform:
            return decode_hex(hexform)
        else:
            return stringform
