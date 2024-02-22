import subprocess

import qrcode

data = (
    subprocess.check_output(["netsh", "wlan", "show", "profiles"])
    .decode("utf-8")
    .split("\n")
)
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
wifi = (
    subprocess.check_output(["netsh", "WLAN", "show", "interfaces"])
    .decode("utf-8")
    .split("n")
)
details = subprocess.check_output(["netsh", "WLAN", "show", "interfaces"]).decode(
    "utf-8"
)
profile = [i.split(":")[1][1:-1] for i in wifi if "SSID" in i]
for i in profile:
    Name = i.split("\r")[0]

for i in profiles:
    results = (
        subprocess.check_output(["netsh", "wlan", "show", "profile", Name, "key=clear"])
        .decode("utf-8")
        .split("\n")
    )
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    password = "{:<}".format(results[0])


print(details)
input_data = "WIFI:S:" + Name + ";T:" + "WPA" + ";P:" + password + ";;"

# generating qr code to share quickly
print("SCAN QR Code To Quickly Connect To The AccessPoint")
qr = qrcode.QRCode()
qr.add_data(input_data)
qr.print_ascii()
