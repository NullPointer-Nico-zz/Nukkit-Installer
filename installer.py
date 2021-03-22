import requests
import platform
import os

res = requests.get('https://ci.opencollab.dev//job/NukkitX/job/Nukkit/job/master/lastSuccessfulBuild/artifact/target/nukkit-1.0-SNAPSHOT.jar',
                   allow_redirects=True)

open("nukkit.jar", "wb").write(res.content)

if platform.system() in ["Linux", "darwin"]:
    with open("start.sh", "w") as file:
        file.write("java -Xms512M -Xmx512M -jar nukkit.jar\n")
    os.system("chmod +x start.sh")
else:
    with open("start.bat", "w") as file:
        file.write("java -Xms512M -Xmx512M -jar nukkit.jar\n")

print("Nukkit Server Installed\n")

if platform.system() in ["Linux", "darwin"]:
    print("To start the server use the start.sh file.")
else:
    print("To start the server use the start.bat file.")
