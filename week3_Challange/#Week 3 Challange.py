#Week 3 Challange
 
DRS = 1
DRB = 0
PSS = 1
PSB = 1

IGN = 1

ALM = 1

if IGN == 1:
    if DRS == 1 & DRB == 0 or PSS == 1 & PSB == 0:
        ALM = 0
else:
    ALM = 1
    
if ALM == 0:
    print(f"Alarm!! Seat belt not buckled")
else:
    print(f"Thank you for being safe")