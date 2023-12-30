import sys
import os

from package import get_package_disassembled, save_disassembled
from upgradeCap import get_package_history

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <upgradeCap>")
        exit(1)

    upgradeCap = sys.argv[1]
    os.mkdir(upgradeCap)

    package_history = get_package_history(upgradeCap)
    print(package_history)
    version = len(package_history)

    for package in package_history:
        dis = get_package_disassembled(package)
        save_disassembled(dis, f"{upgradeCap}/{version}_{package}")
        version -= 1


if __name__ == "__main__":
    main()