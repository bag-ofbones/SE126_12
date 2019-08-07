# Brenna Giroux, SE126.12, August 7, 2019, Lab3B
# Rewrite Lab #2A (voter analysis lab) so that all data comes from the csv file voters.csv.  This final solution should
# have NO input() statements and when the console is ran it should print all 7 totals from Lab 2A.  Use your original 2A
# (or the solution file!) as starter code, but edit it to connect to a file and use a for loop to process each voter
# and their data to still find the 7 totals.
import csv

# dir_path = 'C:/NEIT/Users/brenn/Desktop/Lab3A_CSV_Voters/'
dir_path = 'C:/Users/brenn/Desktop/Lab3A_CSV_Voters/'
file = 'vote.csv'

print("\t\t\tWELCOME TO THE VOTER REGISTRATION PROGRAM\n")

total_voters = 0  # records = rows of data ALWAYS have to total records var and value
total_vote = 0

# FIELD HEADER
id_num = "ID NUMBER"
age = "AGE"
gender = "GENDER"
registered = "REGISTERED TO VOTE?"
voted = "VOTED?"

print("{0:20} {1:20} {2:20} {3:20} {4:20}".format(id_num, age, gender, registered, voted))

# create counters
males_not_eligible = 0
females_not_eligible = 0
males_old_enough = 0
females_old_enough = 0
individuals_eligible_did_not_vote = 0
individuals_voted = 0
records_processed = 0

# STEP 3--OPEN FILE
with open(dir_path+file) as csv_file:  # open as csv file
    file = csv.reader(csv_file, skipinitialspace=True)  # skipin = HELLOOOOO GET RID OF THE WHITE SPACES!!!!!
    # now the file we have connected to the program is known as 'file'


    # below is a FOR LOOP-- repeated sequence of code, they continue not based on a condition but on RANGE
    for rec in file:    # repeats until terminated
        id_num = rec[0]
        age = int(rec[1])
        gender = rec[2]
        registered = rec[3]
        voted = rec[4]

        # test output
        print("{0:8} {1:8} {2:8} {3:8} {4:8}".format(id_num, age, gender, registered, voted))

        records_processed += 1

        # check if this is a under-aged male
        if age < 18 and gender == "M":
            males_not_eligible += 1

        # check if this is a under-aged female
        if age < 18 and gender == "F":
            females_not_eligible += 1

        # check males old enough to vote
        if age > 18 and voted == "N":
            males_old_enough += 1

        # check females old enough to vote
        if age > 18 and voted == "N":
            females_old_enough += 1

        # individuals who did not vote
        if registered == "Y" and voted == "N":
            individuals_eligible_did_not_vote += 1

        # individuals voted
        if registered == "Y" and voted == "Y":
            individuals_voted += 1

print("______________________________________________________________")

print("\n Processing Voters Analysis....\n")
print("\n\t\t\t VOTERS ANALYSIS\n")

print(" 1. Number of Males not eligible to register: {0}".format(males_not_eligible))
print(" 2. Number of Females not eligible to register: {0}".format(females_not_eligible))
print(" 3. Number of Males who are old enough to vote but have not registered: {0}".format(males_old_enough))
print(
    " 4. Number of Females who are old enough to vote but have not registered: {0}".format(females_old_enough))
print(" 5. Number of individuals who are eligible to vote but did not vote: {0}".format(
    individuals_eligible_did_not_vote))
print(" 6. Number of individuals who did vote: {0}".format(individuals_voted))
print(" 7. Number of records processed: {0}".format(records_processed))

print("\n\n PROGRAM COMPLETE, GOODBYE.")
