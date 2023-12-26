import statistics

# number = input("How many students are there?: ")
# print("Enter score")
# students = []
# for i in range(int(number)):
#     students.append(int(input()))
# students = sorted(students)
# print(students)
# print(f"{statistics.median(students)} is the average of the students' marks")
# print(max(students))
# print(students[len(students) - 1])
num_sum = 0
for num in range(1, 101, 2):
    num_sum += num

print(num_sum)
