import requests
import platform


def isnotcurrvernewest(currversion: str):
    """get the newest version number and compare it to the current one"""
    response = requests.get(
        "https://api.github.com/repos/NYC00kie/pygame_jumpandrun/releases/latest")
    version = response.json()["name"].replace("v", "")
    splitversion = version.split(".")
    currsplitversion = currversion.split(".")
    print(splitversion, currsplitversion)
    if splitversion[0] >= currsplitversion[0] or splitversion[1] >= currsplitversion[1]:
        # no new release
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
            with open(asset["name"], "wb") as f:
                f.write(file.content)

        elif asset["name"] == "linux" and platform.system() == "Linux":
            print("Downloading")
            file = requests.get(asset["browser_download_url"])
            with open(asset["name"], "wb") as f:
                f.write(file.content)
