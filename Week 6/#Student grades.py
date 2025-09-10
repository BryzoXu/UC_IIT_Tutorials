#--
#Function 
#--

def get_grades():
    midterm = float(input(f"Enter Midterm Mark: "))
    final = float(input(f'Enter Final Exam Mark: '))
    return midterm, final

def cal_grades(midterm, final):
    ave_grade = ((final*2 + midterm) / 2)
    print(ave_grade)
    if ave_grade >= 90:
        grade = "A"
    elif ave_grade >= 89:
        grade = "B"
    elif ave_grade >= 75:
        grade = "C"
    elif ave_grade >= 50:
        grade = "D"
    else:
        grade = "F"
        
    return grade

def main():
    midterm, final = get_grades()
    grade = cal_grades(midterm, final)
    print(grade)

    
    
main()