import json
import glob
import os
jsonpath = os.path.dirname(__file__)+"\\"
files = glob.glob(jsonpath + r"**\*.json", recursive= True)
ans = "  "
while ans[0] != "i" and ans[0] != "t":
    ans = input("Input your ID to continue\n-").lower()
    if ans[0] != "i" and ans[0] != "t":
        print("Error: Invalid ID")
    if ans[0] == "t":
        for i in files:
            if os.path.basename(i).find("team") != -1:
                if os.path.basename(i).find(str(ans[1])) != -1:
                    print(os.path.basename(i))
                else:
                    print("Team ID not valid")
                    quit()
