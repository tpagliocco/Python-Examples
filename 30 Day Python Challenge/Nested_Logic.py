return_date = list(map(str, input().split(" ")))
due_date  = list(map(str, input().split(" ")))
#date actually returned
rday = int(return_date[0])
rmonth = int(return_date[1])
ryear = int(return_date[2])
#date due
dday = int(due_date[0])
dmonth = int(due_date[1])
dyear = int(due_date[2])

fine = 0return_date = list(map(str, input().split(" ")))
due_date  = list(map(str, input().split(" ")))
#date actually returned
rday = int(return_date[0])
rmonth = int(return_date[1])
ryear = int(return_date[2])
#date due
dday = int(due_date[0])
dmonth = int(due_date[1])
dyear = int(due_date[2])

fine = 0

#if returned ontime , fine is 0
if rday == dday and rmonth == dmonth and ryear == dyear:
    fine = 0

#if after return month but same year
if ryear == dyear and rmonth != dmonth:
    #calculate # of months late
    months_late = rmonth - dmonth
    fine = months_late * 500

#if same month and same year
if rday != dday and rmonth == dmonth and ryear == dyear:
    #calculate # of days late
    days_late = rday - dday
    fine = days_late * 15

print(fine)




#print(rday, rmonth, ryear, "and", dday, dmonth, dyear)




if rday == dday and rmonth == dmonth and ryear == dyear:
    fine = 0
    print(fine)

#if after return month but same year
if ryear == dyear and rmonth != dmonth:
    #calculate # of months late
    months_late = rmonth - dmonth
    fine = months_late * 500

if rday != dday and rmonth == dmonth and ryear == dyear:
    days_late = rday - dday
    fine = days_late * 15

print(fine)




print(rday, rmonth, ryear, "and", dday, dmonth, dyear)


