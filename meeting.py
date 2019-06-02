# Convert number to a time
def num2time(number):
	time = ""
	if number > 1200:
		number -= 1200

		if number/100 == 0:
			time += "12"
		elif number/100 == 12:
			time += "00"
		else:
			time += str(number/100)

		time += ":"

		if number%100 == 0:
			time += "00"
		else:
			time += str(number%100)

		if number/100 == 12:
			time += "AM"
		else:
			time += "PM"
	else:
		if number/100 == 0:
			time += "00"
		else:
			time += str(number/100)

		time += ":"

		if number%100 == 0:
			time += "00"
		else:
			time += str(number%100)

		if number/100 == 12:
			time += "PM"
		else:
			time += "AM"

	return time

# Convert time to a number
def time2num(times):
	times = times.strip()
	[start, stop] = times.split('-')
	timelist = []
	flag = False

	for i in [start, stop]:

		if 'PM' in i and '12' not in i:
			flag = True
		
		if 'AM' in i or 'PM' in i:
			i = i[:-2]

		if ":" in i:
			[i_hour, i_min] = i.split(':')
		else:
			i_hour = i
			i_min = "00"

		timelist.append(int(i_hour+i_min) + (1200 if flag else 0))

	return timelist

def consolidate(meeting_times):
	
	meeting_times = sorted(meeting_times, key=lambda x: x[0])

	i = 0
	while i < (len(meeting_times)-1):
		if meeting_times[i][1] > meeting_times[i+1][0]:
			meeting_times[i][1] = max(meeting_times[i][1], meeting_times[i+1][1])
			meeting_times.remove(meeting_times[i+1])
		else:
			i = i + 1

	print meeting_times
	return meeting_times


def read_input(filename):
	meeting_times = []
	with open(filename) as fp:
	    for line in fp:
	        meeting_times.append(time2num(line))
    
    	return meeting_times
		        


meeting_times = read_input('input.txt')

meeting_times = consolidate(meeting_times)

for slot in meeting_times:
	
	i = meeting_times.index(slot)

	if i == 0 and 0 != meeting_times[0][0]:
		print "Free: " + num2time(0) + "-" + num2time(meeting_times[i][0])
	else:
		print "Free: " + num2time(meeting_times[i-1][1]) + "-" + num2time(meeting_times[i][0])
	
	print "Busy: " + num2time(slot[0]) + "-" + num2time(slot[1])

if 2400 != meeting_times[-1][1]:
		print "Free: " + num2time(meeting_times[-1][1]) + "-" + num2time(2400)



	# clock = []
	# for i in range(24):
	# 	clock.append(i*100)
	# 	clock.append(i*100+15)
	# 	clock.append(i*100+30)
	# 	clock.append(i*100+45)

	# clock.append(2400)

	# print meeting_times
	# print clock

	# count = 0

	# for time in clock:
	# 	if time < meeting_times[count][0] or 