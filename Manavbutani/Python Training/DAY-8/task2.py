import json
import os
from logging import *

if __name__ == "__main__":
    dic = """{
    "f1":["manav.txt","butani.txt","family.txt","friend.txt"],
    "f2":["manav.txt","butani.txt","family.txt","friend.txt"],
    "f3":["manav.txt","butani.txt","family.txt","friend.txt"],
    "f4":["manav.txt","butani.txt","family.txt","friend.txt"]}
    """

    j = json.loads(dic)
    # print(j["f1"]) # ['manav.txt', 'butani.txt', 'family.txt', 'friend.txt']
    # print(j["f1"][1]) # butani.txt
    k = os.listdir("task2/")
    # print(k) # ['f1', 'f2', 'f3']

    basicConfig(
        filename="task2.log", style="{", format="{message}", filemode="w", level=INFO
    )
    for r in k:
        s = os.listdir("task2/" + r)

        # print(s)
        """
        ['butani.txt', 'manav.txt', 'desktop.ini']
        ['butani.txt', 'manav.txt', 'friend.txt', 'desktop.ini']
        ['manav.txt', 'butani.txt', 'family.txt', 'desktop.ini']
        """

        for q in s:
            if q not in j[r]:
                critical(f"Critical: {q} is not present in json key:{r}")
            else:
                info(f"Info: {q} is present in json key:{r}")