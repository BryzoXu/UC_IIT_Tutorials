Step 1


--- 
Step 2

| Type   | NAMe   | Values | example                   | Meaning |
| ------ | ------ | ------ | ------------------------- | ------- |
| Input  | DRS    | Bool   | In seat = `High` = on     |         |
| Input  | PSS    | Bool   | In seat = `High` = on     |         |
| Input  | DRB    | Bool   | No connected  =`Low` = on |         |
| Input  | PSB    | Bool   | No connected  =`Low `= on |         |
| Input  | Ign    | Bool   | Ign on = `High` = on      |         |
| Output | Altert | Bool   | Alert = `Low` = on        |         |

--- 
**Step 3** 

*3.1*
Start
If engine is running
Check
Does DRS equal High and DRB equal Low or  Does PSS  equal High and PSB equal Low
If Yes Turn on alarm
Otherwise 
Dont turn on alarm
If engine not running do nothing
End

--- 
**3.2**

| DRS | PSS | DRB | PSB | IGN | Output |
| --- | --- | --- | --- | --- | ------ |
| 0   | 0   | 0   | 0   | 0   |        |
| 0   | 0   | 0   | 0   | 1   |        |
| 0   | 0   | 0   | 1   | 0   |        |
| 0   | 0   | 0   | 1   | 1   |        |
| 0   | 0   | 1   | 0   | 0   |        |
| 0   | 0   | 1   | 0   | 1   |        |
| 0   | 0   | 1   | 1   | 0   |        |
| 0   | 0   | 1   | 1   | 1   |        |
| 0   | 1   | 0   | 0   | 0   |        |
| 0   | 1   | 0   | 0   | 1   |        |
| 0   | 1   | 0   | 1   | 0   |        |
| 0   | 1   | 0   | 1   | 1   |        |
| 0   | 1   | 1   | 0   | 0   |        |
| 0   | 1   | 1   | 0   | 1   |        |
| 0   | 1   | 1   | 1   | 0   |        |
| 0   | 1   | 1   | 1   | 1   |        |
| 1   | 0   | 0   | 0   | 0   |        |
| 1   | 0   | 0   | 0   | 1   |        |
| 1   | 0   | 0   | 1   | 0   |        |
| 1   | 0   | 0   | 1   | 1   |        |
| 1   | 0   | 1   | 0   | 0   |        |
| 1   | 0   | 1   | 0   | 1   |        |
| 1   | 0   | 1   | 1   | 0   |        |
| 1   | 0   | 1   | 1   | 1   |        |
| 1   | 1   | 0   | 0   | 0   |        |
| 1   | 1   | 0   | 0   | 1   |        |
| 1   | 1   | 0   | 1   | 0   |        |
| 1   | 1   | 0   | 1   | 1   |        |
| 1   | 1   | 1   | 0   | 0   |        |
| 1   | 1   | 1   | 0   | 1   |        |
| 1   | 1   | 1   | 1   | 0   |        |
| 1   | 1   | 1   | 1   | 1   |        |

Removed all row were IGN is 0 to simplify logic table as IGN 0 will always be no alert

| DRS | PSS | DRB | PSB | IGN | Output | Alarm |
| --- | --- | --- | --- | --- | ------ | ----- |
| 0   | 0   | 0   | 0   | 1   | 1      | Off   |
| 0   | 0   | 1   | 0   | 1   | 1      | Off   |
| 0   | 0   | 1   | 1   | 1   | 1      | Off   |
| 0   | 1   | 0   | 0   | 1   | 0      | ON    |
| 0   | 1   | 0   | 1   | 1   | 1      | Off   |
| 0   | 1   | 1   | 0   | 1   | 0      | ON    |
| 0   | 1   | 1   | 1   | 1   | 1      | Off   |
| 1   | 0   | 0   | 0   | 1   | 0      | ON    |
| 1   | 0   | 0   | 1   | 1   | 0      | ON    |
| 1   | 0   | 1   | 0   | 1   | 1      | Off   |
| 1   | 0   | 1   | 1   | 1   | 1      | Off   |
| 1   | 1   | 0   | 0   | 1   | 0      | ON    |
| 1   | 1   | 0   | 1   | 1   | 0      | ON    |
| 1   | 1   | 1   | 0   | 1   | 0      | ON    |
| 1   | 1   | 1   | 1   | 1   | 1      | Off   |

--- 
**3.3**

LaTaX Math

$Out = \overline{ IGN \cdot ( DRS \cdot \overline{DRB} + PSS \cdot \overline{PSB} ) }$



~Out = IGN * (DRS AND ~DRB + PSS AND ~PSB)

--- 

**3.4**
*PseudoCode* 

Read Sensors
If IGN is ON(HIGH)
Check:
	If DRS is ON(HIGH) & DRB is ON(LOW)
		Then Alarm = on(LOW)
	If PSS is ON(HIGH) & PSB is ON(LOW)
		Then Alarm = on(LOW)
If not 
	The Alarm = off (HIGH)

---
3.4 
Flow Chart 
*See FlowChart.png*

--- 

4.1 
Logic Circit
 *See *LogicCircit.png*

--- 

4.2
Python  My Python
```
	#Week 3 Challange

DRS = 1
DRB = 0
PSS = 1
PSB = 1
IGN = 1

ALM = 1
 

if IGN == 1:
	if DRS == 1 and DRB == 0 or PSS == 1 and PSB == 0:
	ALM = 0
else:
	ALM = 1

if ALM == 0:
	print(f"Alarm!! Seat belt not buckled")
else:
	print(f"Thank you for being safe")
```

4.3 AI Python

```
def check_seatbelt_alarm(DRS, DRB, PSS, PSB, IGN):
    """
    Checks if the seatbelt alarm should be triggered.

    Parameters:
    - DRS: Driver seat occupied (1 = yes, 0 = no)
    - DRB: Driver seatbelt status (0 = unfastened, 1 = fastened)
    - PSS: Passenger seat occupied (1 = yes, 0 = no)
    - PSB: Passenger seatbelt status (0 = unfastened, 1 = fastened)
    - IGN: Ignition status (1 = on, 0 = off)

    Returns:
    - ALM: Alarm status (0 = ON, 1 = OFF)
    """

    if IGN == 1 and ((DRS == 1 and DRB == 0) or (PSS == 1 and PSB == 0)):
        return 0  # Alarm ON
    else:
        return 1  # Alarm OFF


# Example usage:
ALM = check_seatbelt_alarm(DRS=1, DRB=0, PSS=1, PSB=0, IGN=1)

if ALM == 0:
    print("Alarm!! Seat belt not buckled")
else:
    print("Thank you for being safe")

```
