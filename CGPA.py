def calculate_cgpa(grades, prev_cgpa = None, prev_credits = None):
    ''' has a parameter that takes in the grades as argument'''
   
    total_weighted = 0.0
    total_credits = 0.0

    for course in grades:
        total_score = course['test'] + course['exam']
            # calculates the total score in a course'''
        if total_score >= 70.0:
            gp = 5.0
        elif total_score >= 60.0:
            gp = 4.5
        elif total_score >= 50.0:
            gp = 4.0
        elif total_score >= 45.0:
            gp = 3.5
        elif total_score >= 40.0:
            gp = 3.0
        elif total_score >= 35.0:
            gp = 2.5
        elif total_score >= 30.0:           
            gp = 2.0
        elif total_score >= 20.0:
            gp = 1.0
        else:
            gp = 0.0
            
            '''the conditions above determines the 
            gp after analising the total score'''
            
        weighted = gp * course['credit']
        total_weighted += weighted
        total_credits += course['credit']
        
    return round(total_weighted,2)