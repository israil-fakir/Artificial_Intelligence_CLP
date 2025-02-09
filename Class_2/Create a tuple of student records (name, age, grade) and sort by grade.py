print("student info (name, age, grade):")
student = (
            ("a", 15, "C"),
            ("b", 14, "A-"),
            ("c", 17, "B+"),
            ("d", 19, "A+"),
           )

sort_grade = sorted(student, key=lambda grade:grade[2])

for i in sort_grade:
    print(i) 