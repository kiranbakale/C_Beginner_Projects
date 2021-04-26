import os
if os.path.exists("trial.txt"):
    os.remove("trial.txt")
else:
    print("file not present")
