##install mod
# import pip
import subprocess
import sys
import argparse

# use python type hints to make code more readable
from typing import List, Optional


def pip_install(proxy: Optional[str], args: List[str]) -> None:
    if proxy is None:
        # pip.main(["install", f"--proxy={proxy}", *args])
        subprocess.run(
            [sys.executable, "-m", "pip", "install", *args],
            capture_output=False,
            check=True,
        )
    else:
        subprocess.run(
            [
                sys.executable, "-m", "pip", "install", f"--proxy={proxy}",
                *args
            ],
            capture_output=False,
            check=True,
        )


def main():
    parser = argparse.ArgumentParser(description="install requirements")
    parser.add_argument("--cuda", default=None, type=str)
    parser.add_argument(
        "--proxy",
        default=None,
        type=str,
        help="specify http proxy, [http://127.0.0.1:1080]",
    )
    args = parser.parse_args()

    pkgs = f"""
    moviepy
    """

    for line in pkgs.split("\n"):
        # handle multiple space in an empty line
        line = line.strip()

        if len(line) > 0:
            # use pip's internal APIs in this way is deprecated. This will fail in a future version of pip.
            # The most reliable approach, and the one that is fully supported, is to run pip in a subprocess.
            # ref: https://pip.pypa.io/en/latest/user_guide/#using-pip-from-your-program
            # pip.main(['install', *line.split()])

            pip_install(args.proxy, line.split())

    print("\n successfully installed requirements!")


if __name__ == "__main__":
    main()

##正文
from moviepy.editor import *


def changesku(inputpath):
    listdir = os.listdir(inputpath)
    mp4namelist = [name for name in listdir if name.endswith(".mp4")]#格式筛选
    for file in mp4namelist:
        filepath = os.path.join(inputpath, file)
        video = VideoFileClip(filepath)
        list_filepath = list(filepath)
        list_filepath[-1] = '3'
        #判断MP3是否存在
        if list_filepath in listdir:
            continue
        filepath = ''.join(list_filepath)
        print(filepath)
        audio = video.audio
        audio.write_audiofile(filepath)


if __name__ == '__main__':
    vediopath = ""  #视频路径
    changesku(vediopath)