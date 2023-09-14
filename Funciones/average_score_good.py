def get_average_score(spanish_score, science_score, history_score):
    return (spanish_score + science_score + history_score) / 3

def is_student_exempted(spanish_score, science_score, history_score):
    average_score = get_average_score(spanish_score, science_score, history_score)
    return average_score > 70

# Scores
juan_spanish_score = 75
juan_science_score = 95
juan_history_score = 54

sofia_spanish_score = 64
sofia_science_score = 56
sofia_history_score = 98

paul_spanish_score = 72
paul_science_score = 75
paul_history_score = 79

# Results
juan_is_exempted = is_student_exempted(juan_spanish_score, juan_science_score, juan_history_score)
sofia_is_exempted = is_student_exempted(sofia_spanish_score, sofia_science_score, sofia_history_score)
paul_is_exempted = is_student_exempted(paul_spanish_score, paul_science_score, paul_history_score)