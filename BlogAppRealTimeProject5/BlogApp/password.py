import subprocess
output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

data = output.decode('utf-8').split('\n')
profiles = []
for d in data:
    if "All User" in d:
        profiles.append(d.split(":")[1].replace('\r','').strip())

gold = []
for profile in profiles:
    command = ["netsh", "wlan", "show", "profile", profile, "key=clear"]
    output = subprocess.check_output(command)
    data = output.decode('utf-8').split('\n')
    for d in data:
        if "Key Content" in d:
            password = d.split(":")[1].replace('\r','').strip()
            gold.append([profile,password])

for g in gold:
    print("Username: " +g[0] + "\nPassword: " + g[1])
    print("------------------")