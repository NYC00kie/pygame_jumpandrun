import requests
import platform
import subprocess
import sys


def isnotcurrvernewest(currversion: str):
    """get the newest version number and compare it to the current one"""
    response = requests.get(
        "https://api.github.com/repos/NYC00kie/pygame_jumpandrun/releases/latest")
    version = response.json()["name"].replace("v", "")
    splitversion = version.split(".")
    currsplitversion = currversion.split(".")
    print(splitversion, currsplitversion)

    print(f"{splitversion[0]}.{splitversion[1]}",
          f"{currsplitversion[0]}.{currsplitversion[1]}")

    if float(f"{splitversion[0]}.{splitversion[1]}") > float(f"{currsplitversion[0]}.{currsplitversion[1]}"):
        return True

    else:
        return False


def downloadnewestversion():
    print("initing download")
    response = requests.get(
        "https://api.github.com/repos/NYC00kie/pygame_jumpandrun/releases/latest")
    assets = response.json()["assets"]
    for asset in assets:
        if asset["name"] == "main.exe" and platform.system() == "Windows":
            print("Downloading")
            file = requests.get(asset["browser_download_url"])
            with open(f"new_{asset['name']}", "wb") as f:
                f.write(file.content)

            subprocess.Popen(
                # , stdout=sys.stdout
                f"timeout 5 & del {asset['name']} & timeout 5 & move new_{asset['name']} {asset['name']}", shell=True
            )
            sys.exit()

        elif asset["name"] == "linux" and platform.system() == "Linux":
            print("Downloading")
            file = requests.get(asset["browser_download_url"])
            with open(f"new_{asset['name']}", "wb") as f:
                f.write(file.content)

            subprocess.Popen(
                # , stdout=sys.stdout
                f"timeout 5 & del {asset['name']} & timeout 5 & move new_{asset['name']} {asset['name']}", shell=True
            )
            sys.exit()
