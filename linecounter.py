import time
import os
import re
import locale

wlk = os.walk(".")

num_all_files = 0
num_all_lines = 0
for root, dirs, files in wlk:
    for file in files:
        if file.endswith(".py"):
            f = open(os.path.join(root, file))
            numlines = len(f.readlines())
            num_all_files += 1
            num_all_lines += numlines
            f.close()
            
            
self_file = open("linecounter.py", "r", encoding="utf-8")            
last_line = self_file.readlines()[-1]
prev_lines = num_all_lines
try:
    prev_lines = int(re.search(r"Linii: ([0-9]*)[.\s]", last_line).group(1))
except:
    pass
lines_delta = num_all_lines - prev_lines
self_file.close()

self_file = open("linecounter.py", "a", encoding="utf-8")

locale.setlocale(locale.LC_TIME, "pl_PL")

str_date = time.strftime("%A %d %B %Y %H:%M").title()
str_numfiles = "Plików: " + str(num_all_files)
delta_string = f" (^{lines_delta})" if lines_delta > 0 else f" (v{lines_delta})"
str_numlines = "Linii: " + str(num_all_lines) + delta_string

self_file.write(f"#  {str_date}: \t {str_numfiles} \t {str_numlines} \n")
self_file.close()

#  Wtorek 29 Październik 2024 17:09: 	 Plików: 15 	 Linii: 586 (v0) 
#  Wtorek 29 Październik 2024 17:09: 	 Plików: 15 	 Linii: 587 (^1) 
#  Wtorek 29 Październik 2024 17:09: 	 Plików: 15 	 Linii: 588 (^1) 
#  Wtorek 29 Październik 2024 17:09: 	 Plików: 15 	 Linii: 589 (^1) 
#  Wtorek 29 Październik 2024 17:09: 	 Plików: 15 	 Linii: 590 (^1) 
#  Wtorek 29 Październik 2024 17:09: 	 Plików: 15 	 Linii: 591 (^1) 
#  Wtorek 29 Październik 2024 17:09: 	 Plików: 15 	 Linii: 592 (^1) 
#  Wtorek 29 Październik 2024 19:25: 	 Plików: 15 	 Linii: 595 (^3) 
