Capital_dic = {
    "Cambodia": "Phnom Penh",
    "Thailand": "Bangkok",
    "China": "Bai Jing",
    "Vietnam": "Hanoy",
    "Lao": "Veang Chan"
}

value = input("Enter the name of City:  ")

result = {
    "Capital":Capital_dic[value]
}

for country in Capital_dic:
    print("{} has {}".format(country,Capital_dic[country]))