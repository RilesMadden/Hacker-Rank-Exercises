s = '06:05:45PM'

# get AM or PM
a_or_p = s[-2]

# make time into a list
time_as_list = []
for i in range(0, len(s)-2):
    time_as_list.append(s[i])    

# get hours as int
hours_list = []
hours_list.append(s[0])
hours_list.append(s[1])
hours_string = ''.join(hours_list)
hours = int(hours_string)

if a_or_p == 'A':
    if hours == 12:
        time_as_list[0] = '0'
        time_as_list[1] = '0'
else:
    if hours < 12:
        hours += 12
        hours_string = str(hours)
        time_as_list[0] = hours_string[0]
        time_as_list[1] = hours_string[1]

converted_time = ''.join(time_as_list)
print(converted_time)














# time_as_list = []
# time_converted_list = []
# for letter in s:
#     time_as_list.append(letter)
# hours_list = []
# hours_list.append(s[0])
# hours_list.append(s[1])
# hours = int(''.join(hours_list))
# if time_as_list[-2] == 'A':
#     if hours < 12:
#         for i in range(0, len(s) - 2):
#             time_converted_list.append(time_as_list[i])
#     if hours == 12:
#         time_as_list[0] = 0
#         time_as_list[1] = 0
#         for i in range(0, len(s) - 2):
#             time_converted_list.append(time_as_list[i])

# time_converted_string = ''.join(time_converted_list)
# print(time_converted_string)
        


# if time_as_list[-2] == 'A':
#     if hours_int < 12:
#         for i in range(0, len(time_as_list)-1):
#             time_converted.append(time_as_list[i])



# print(timeConversion(s))