
| Type   | NAMe   | Values | example                   | Meaning |
| ------ | ------ | ------ | ------------------------- | ------- |
| Input  | DRS    | Bool   | In seat = `High` = on     |         |
| Input  | PSS    | Bool   | In seat = `High` = on     |         |
| Input  | DRB    | Bool   | No connected  =`Low` = on |         |
| Input  | PSB    | Bool   | No connected  =`Low `= on |         |
| Input  | Ign    | Bool   | Ign on = `High` = on      |         |
| Output | Altert | Bool   | Alert = `Low` = on        |         |

**Step 3** 

Start
If engine = High
	Does DRS equal High and DRB equal Low
	or 
	Does PSS  equal High and PSB equal Low
	Alarm = Low 
End


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

Removed all row were IGN is 0 to simplify logic as IGN 0 will always be no alert

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

**3.3**

Out = IGN * DRS ~DRB + PSS ~PSB

**Step 4**



If IGN == 1
	If DRS == 1 & DRB == 0
		Alarm = 1
	IF PRS == 1 & PSB == 0 
		Alarm = 1
Else 
	Alarm = 0



	