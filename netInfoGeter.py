import pandas as pd
import re

# Load Excel file
df = pd.read_excel("your_file.xlsx", header=None)

# Parse each column (device config)
for col in df.columns:
    config_lines = df[col].dropna().astype(str).tolist()
    config_text = "\n".join(config_lines)

    hostname = re.search(r'^hostname (\S+)', config_text, re.M)
    ospf = re.search(r'router ospf (\d+)', config_text)
    bgp = re.search(r'router bgp (\d+)', config_text)
    nat = re.search(r'ip nat inside source list \d+ interface \S+ overload', config_text)

    print(f"Hostname: {hostname.group(1) if hostname else 'Unknown'}")
    print(f"OSPF: {ospf.group(1) if ospf else 'None'}")
    print(f"BGP: {bgp.group(1) if bgp else 'None'}")
    print(f"NAT Overload: {'Yes' if nat else 'No'}")
    print("="*40)
