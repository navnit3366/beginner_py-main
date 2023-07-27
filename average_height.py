# 31.07.2021
# A program which calculates the average of values in a list.

student_heights = [156, 178, 165, 171, 187]

heights = 0
for i in student_heights:
    heights += i
    
string_sum = 0
for a in student_heights:
    string_sum += 1

average_height = round(heights / string_sum)

print(average_height)
