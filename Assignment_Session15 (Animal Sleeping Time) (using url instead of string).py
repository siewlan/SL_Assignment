#Data set from <https://raw.githubusercontent.com/genomicsclass/dagdata/master/inst/extdata/msleep_ggplot2.csv>

##2nd method

#Input
import requests
rowsurl="https://raw.githubusercontent.com/genomicsclass/dagdata/master/inst/extdata/msleep_ggplot2.csv"
r=requests.get(rowsurl)
rows=r.text
rows=rows.split("\n")

#Computation

#Output - not using if condition
#title row cannot convert to float so print first, then delete title row --> rows.pop(0)
print("""%s\t%s"""%(rows[0].split(",")[0],rows[0].split(",")[5]))
rows.pop(0)

#there was an empty string at the end so delete
rows.pop()

for eachrow in rows:
        print("""%s\t%s"""%(eachrow.split(",")[0],float(eachrow.split(",")[5])))

