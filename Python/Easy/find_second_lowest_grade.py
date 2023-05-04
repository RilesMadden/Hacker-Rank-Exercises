# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

records = [["danny", 40], ["charlie", 20], ["doug", 50], ["lenny", 40], ["alice", 40]]
scores = []
for record in records:
    scores.append(record[1])
# order that list smallest to biggest
scores.sort()

# iterate through the list starting with the smallest
second_lowest = 0
counter = 0
while second_lowest == 0:
    if scores[counter] != scores[counter+1]:
        second_lowest = scores[counter+1]
    else:
        counter += 1

second_lowest_list = []
for i in range(0, len(records)):
    if records[i][1] == second_lowest:
        second_lowest_list.append(records[i][0])
second_lowest_list.sort()
for name in second_lowest_list:
    print(name)