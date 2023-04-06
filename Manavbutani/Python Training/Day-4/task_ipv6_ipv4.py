"""Write a python program to check valid IPV4 and IPV6 ip address (Regex)
"""
import re
ip = input("Enter the ip address: ")
check_ipv4 = re.match(
    r"^((25[0-5]|2[0-4][\d]|[01]?[\d][\d]?)\\.){3}(25[0-5]|2[0-4][\d]|[\d]?[\d][\d]?)$",
    ip,
)
check_ipv6 = re.match(
    r"([0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}|(\d{1,3}\.){3}\d{1,3}",
    ip,
)
if check_ipv4:
    print("IP Address is IPV4")
elif check_ipv6:
    print("IP Address is IPV6")
else:
    print("Address is not IPV4 and not IPV6")
    