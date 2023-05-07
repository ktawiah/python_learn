"""
Sales calculator 
Question
--------
Write a program to calculate the annual monthly sales 
    for shops in High street branch and Mall Branch 
"""
month1_high_street_branch = [42000, 52000, 46000, 50000]
month2_high_street_branch = [48000, 58000, 49000, 51000]
month3_high_street_branch = [50000, 60000, 58000, 61000]
month1_high_street_branch.append(sum(month1_high_street_branch))
month2_high_street_branch.append(sum(month2_high_street_branch))
month3_high_street_branch.append(sum(month3_high_street_branch))
sum_quater1_high_street_branch = (
    month1_high_street_branch[0]
    + month2_high_street_branch[0]
    + month3_high_street_branch[0]
)
sum_quater2_high_street_branch = (
    month1_high_street_branch[1]
    + month2_high_street_branch[1]
    + month3_high_street_branch[1]
)
sum_quater3_high_street_branch = (
    month1_high_street_branch[2]
    + month2_high_street_branch[2]
    + month3_high_street_branch[2]
)
sum_quater4_high_street_branch = (
    month1_high_street_branch[3]
    + month2_high_street_branch[3]
    + month3_high_street_branch[3]
)
Quaterly_Sales = [
    sum_quater1_high_street_branch,
    sum_quater2_high_street_branch,
    sum_quater3_high_street_branch,
    sum_quater4_high_street_branch,
    "",
]
Quaters = ["Quater 1", "Quater 2", "Quater 3", "Quater 4", "Montly Sales"]
print("\t\tHigh Street Branch")
print("\t\tmonth 1\tmonth 2\tmonth 3\tQuarterly Sales")
for value in range(0, 5, 1):
    print(
        str(Quaters[value])
        + "\t"
        + str(month1_high_street_branch[value])
        + "\t"
        + str(month2_high_street_branch[value])
        + "\t"
        + str(month3_high_street_branch[value])
        + "\t"
        + str(Quaterly_Sales[value])
    )
print("\n\tAnnual monthly sales = 625000\n")

month1_mall_branch = [57000, 70000, 67000, 72000]
month2_mall_branch = [63000, 67000, 65000, 69000]
month3_mall_branch = [60000, 73000, 62000, 75000]
month1_mall_branch.append(sum(month1_mall_branch))
month2_mall_branch.append(sum(month2_mall_branch))
month3_mall_branch.append(sum(month3_mall_branch))
sum_quater1_mall_branch = (
    month1_mall_branch[0] + month2_mall_branch[0] + month3_mall_branch[0]
)
sum_quater2_mall_branch = (
    month1_mall_branch[1] + month2_mall_branch[1] + month3_mall_branch[1]
)
sum_quater3_mall_branch = (
    month1_mall_branch[2] + month2_mall_branch[2] + month3_mall_branch[2]
)
sum_quater4_mall_branch = (
    month1_mall_branch[3] + month2_mall_branch[3] + month3_mall_branch[3]
)
Quaterly_Sales_mall_branch = [
    sum_quater1_mall_branch,
    sum_quater2_mall_branch,
    sum_quater3_mall_branch,
    sum_quater4_mall_branch,
    "",
    "",
]
Quaters_mall_branch = ["Quater 1", "Quater 2", "Quater 3", "Quater 4", "Montly Sales"]
print("\t\tMall Branch")
print("\t\tMonth 1\tMonth 2\tMonth 3\tQuarterly Sales")
for value in range(0, 5, 1):
    print(
        str(Quaters_mall_branch[value])
        + "\t"
        + str(month1_mall_branch[value])
        + "\t"
        + str(month2_mall_branch[value])
        + "\t"
        + str(month3_mall_branch[value])
        + "\t"
        + str(Quaterly_Sales_mall_branch[value])
    )
print("\n\tAnnual monthly sales = 800000")
