

#===================================================================
                    #MODULES — Real-World Mini Project
#===================================================================

import motivation_module
import datetime

print("================= DAILY MOTIVATION =================")

now = datetime.datetime.now()
print(now.strftime("Date: %d %B, %Y"))

print("Today's Motivation:\n",motivation_module.get_motivation())