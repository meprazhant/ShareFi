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
otherdata = subprocess.check_output(["netsh", "WLAN", "show", "interfaces"]).decode(
    "utf-8"
)
profile = [i.split(":")[1][1:-1] for i in wifi if "SSID" in i]
for i in profile:
    Name = i.split("\r")[0]
    # Wifi name = Data

for i in profiles:
    results = (
        subprocess.check_output(["netsh", "wlan", "show", "profile", Name, "key=clear"])
        .decode("utf-8")
        .split("\n")
    )
    # print(results)
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    password = "{:<}".format(results[0])

print("Wifi " + Name + "'s Data has been Collected\n")
val = input("To View Password Input 1\nTo Generate QR Code Input 2\n ==>")
if val == "1":
    print("Wifi SSID: " + Name)
    print("\nWIfi Password: " + password)
    print("\n *** Other WIFI Details*** \n")
    print(otherdata)
elif val == "2":

    input_data = "WIFI:S:" + Name + ";T:" + "WPA" + ";P:" + password + ";;"
    # Creating an instance of qrcode
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(input_data)
    print("SCAN QR Code To Quickly Connect To The AccessPoint")
    qr.print_ascii()

else:
    print("The Input You Provided is not Valid. Try Again")
