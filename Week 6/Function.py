def main():
    data()
    calc()
    output()

def calc():
    bal = data()
    new_bal = bal *0.015
    if new_bal < 20:
        min_pay = new_bal
    else:
        min_pay = 20 + ((new_bal-20) * .1)
            
