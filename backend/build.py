# -*- coding: utf-8 -*-
# @Author: Bi Ying
# @Date:   2023-05-15 13:34:28
# @Last Modified by:   Bi Ying
# @Last Modified time: 2023-05-17 18:39:13
import shlex
import shutil
import argparse
import subprocess
from pathlib import Path


def run_cmd(cmd: str, split=False):
    """
    Run command in shell
    """
    if split:
        cmd = shlex.split(cmd)
    return subprocess.run(cmd, shell=True)


def build_production(version):
    run_cmd("pyinstaller main.spec --noconfirm", split=True)
    # Create a version file in ./dist/vector-vein/
    with open("./dist/vector-vein/version.txt", "w") as f:
        f.write(version)


def build_development(version):
    pass


def build_frontend():
    run_cmd("cd '../frontend' && pnpm run build", split=True)
    web_path = Path("./web")
    if web_path.exists():
        shutil.rmtree(web_path)
    web_path.mkdir()
    # 遍历../frontend/dist并将所有文件按路径复制到./web
    for file_path in Path("../frontend/dist").rglob("*"):
        if file_path.is_file():
            target_file_path = Path("./web") / file_path.relative_to("../frontend/dist")
            if not target_file_path.parent.exists():
                target_file_path.parent.mkdir(parents=True)
            shutil.copy(file_path, target_file_path)
    # 遍历../frontend/src/assets/并将所有文件按路径复制到./web/assets/
    for file_path in Path("../frontend/src/assets/").rglob("*"):
        if file_path.is_file():
            target_file_path = Path("./web/assets/") / file_path.relative_to("../frontend/src/assets/")
            if not target_file_path.parent.exists():
                target_file_path.parent.mkdir(parents=True)
            shutil.copy(file_path, target_file_path)


parser = argparse.ArgumentParser(description="Build software.")
parser.add_argument("-v", "--version", default="0.0.1", help="version number, default: 0.0.1")
parser.add_argument(
    "-t", "--type", default="production", help="build type: development(d) or production(p) or frontend(f)"
)
args = parser.parse_args()
if args.type == "p" or args.type == "production":
    build_production(args.version)
elif args.type == "d" or args.type == "development":
    build_development(args.version)
elif args.type == "f" or args.type == "frontend":
    build_frontend()
