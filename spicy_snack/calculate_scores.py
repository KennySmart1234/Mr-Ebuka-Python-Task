


def calculate_average(score):

    if score >= 90 and score <= 100:
        return "A"
    if score >= 80 and score < 90:
        return "B"
    if score >= 70 and score < 80:
        return "C"
    if score >= 60 and score < 70:
        return "D"
    if score < 60:
        return "F"




print(calculate_average(95))
print(calculate_average(73))
print(calculate_average(30))





