import json
import glob
import os
jsonpath = os.path.dirname(__file__)+"\\"
files = glob.glob(jsonpath + r"**\*.json", recursive= True)
ans = "  "
for i in files:
    print(os.path.basename(i))
if len(files) < 3:
    print("Error: No Team or Individual Files")
else:
    while ans[0] != "i" and ans[0] != "t":
        ans = input("Input your ID to continue\n-").lower()
        if ans[0] != "i" and ans[0] != "t":
            print("Error: Invalid ID")


        elif ans[0] == "t":
            for i in files:
                if os.path.basename(i).find(str(ans[1])) != -1 and os.path.basename(i).find("team") != -1:
                    print(os.path.basename(i))
                    break

        elif ans[0] == "i":
            for i in files:
                if os.path.basename(i).find(str(ans[1])) != -1 and os.path.basename(i).find("indiv") != -1:
                    print(os.path.basename(i))
                    break
