from datetime import datetime

def days_to_birthday(date):
    '''
    Calculates the number of days that have passed since the 1st of January 
    to the given date.

    :param date: A date string in the format of yyyy-mm-dd
    :return: The number of days to the date from 1st of January 
             (eg: date->2021-01-01, return->1)
    '''

    # Convert the date string to a datetime object
    datetime_object = datetime.strptime(date, "%Y-%m-%d")

    # Extract only the date and remove the timestamp
    date = datetime_object.date()

    # Find the number of days since the begining of the year
    num_days = date.timetuple().tm_yday

    return num_days


# Please do not edit anything above this line.
################################################################################



# Your code should be included here. 
# You may use the days_to_birthday(date) function in your solution.

input_file = open("input.txt", "r")
output_file = open("output.txt", "w")

# To store count per year
year_count = {}

for line in input_file:
    line = line.strip()
    
    if line == "":
        continue

    name, dob, gender = line.split()

    # Get year from date
    year = dob[:4]

    # 🔴 IMPORTANT: Use given function
    day_number = days_to_birthday(dob)

    # Add 500 if female
    if gender == "F":
        day_number += 500

    # Serial number per year
    if year not in year_count:
        year_count[year] = 1
    else:
        year_count[year] += 1

    serial = year_count[year]

    # Format NIC
    nic = year + f"{day_number:03d}" + f"{serial:03d}"

    output_file.write(name + " " + nic + "\n")

input_file.close()
output_file.close()


################################################################################
# Please do not edit anything below this line.

##################### End of the programme #####################################