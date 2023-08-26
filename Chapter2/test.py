# Create the capital_dic dictionary
capital_dic = {
    "USA": "Washington, D.C.",
    "Canada": "Ottawa",
    "Germany": "Berlin",
    "France": "Paris",
    "Japan": "Tokyo",
    "South Korea": "Seoul"
}

# Create a dictionary to store results about Korea
korea_results = {
    "Capital": capital_dic["USA"],
    "Population": "51.64 million",
    "Language": "Korean",
    "Currency": "South Korean won (KRW)",
    "Continent": "Asia"
}

# Print the results
for key, value in korea_results.items():
    print(f"{key}: {value}")