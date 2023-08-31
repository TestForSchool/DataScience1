pirates_data_1 = {
                "Name":["Edward Teach", "Anne Bonny", "John Rackham", "Cheung Po Tsai", "Grace O'Malley", "Mary Read", "Sayyida al Hurra", "Zheng Yi Sao", "Francis Drake", "Jean Lafitte"],
                "Year_Started": [1716, 1718, 1718, 1798, 1564, 1708, 1515, 1801, 1563, 1810],
                 "Year_Ended": [1718, 1720, 1720, 1810, 1595, 1721, 1545, 1810, 1596, 1823],
                 "Sailed" : ["Caribbean", "Caribbean", "Caribbean", "South China Sea", "British Isles", "Caribbean", "Mediterranean", "South China Sea", "Caribbean", "Gulf of Mexico"],
                 "Alias" : ["Blackbeard", None, "Calico Jack", "The Kid", "Queen of Ireland", "Mark", "Hakimat Titwan", "Ching Shih", "Sir Francis Drake", "Terror of the Gulf"]}


pirates_data_2 = {
 "Edward Teach" : [1716, 1718, "Caribbean", "Blackbeard"],
 "Anne Bonny" : [1718, 1720, "Caribbean", None],
 "John Rackham" : [1718, 1720, "Caribbean", "Calico Jack"],
 "Cheung Po Tsai" : [1798, 1810, "South China Sea", "The Kid"],
 "Grace O'Malley" : [1564, 1595, "British Isles", "Queen of Ireland"],
 "Mary Read" : [1708, 1721, "Caribbean", "Mark"],
 "Sayyida al Hurra" : [1515, 1545, "Mediterranean", "Hakimat Titwan"],
 "Zheng Yi Sao" : [1801, 1810, "South China Sea", "Ching Shih"],
 "Francis Drake" : [1563, 1596, "Caribbean", "Sir Francis Drake"],
 "Jean Lafitte" : [1810, 1823, "Guluf of Mexico", "Terror of the Gulf"]}

pirates = [
    {"name": "Pirate", "sex": "M", "death_age": "40",
        "height": "6.4", "skull_cross": "F"},
    {"name": "BlackBeard", "sex": "F", "death_age": "24",
        "height": "5.6", "skull_cross": "T"},
    {"name": "Anne_Bonny", "sex": "M", "death_age": "37",
        "height": "5.6", "skull_cross": "T"},
    {"name": "Calico_Jack", "sex": "M", "death_age": "39",
        "height": "5.3", "skull_cross": "F"},
    {"name": "Cheung_Po_Tsai", "sex": "F", "death_age": "73",
        "height": "5.0", "skull_cross": "F"},
    {"name": "Grace O'Malley", "sex": "F", "death_age": "36",
        "height": "5.1", "skull_cross": "T"},
    {"name": "Mary_Read", "sex": "F", "death_age": "75",
        "height": "", "skull_cross": "F"},
    {"name": "Sayyida_al_Hurra", "sex": "F", "death_age": "69",
        "height": "5.3", "skull_cross": "F"},
    {"name": "Ching_Shih", "sex": "M", "death_age": "56",
        "height": "5.5", "skull_cross": "F"},
    {"name": "Sir_Francis_Drake", "sex": "M",
        "death_age": "46", "height": "6.2", "skull_cross": "F"},
    {"name": "Jean Lafitte", "sex": "M", "death_age": "NA",
        "height": "", "skull_cross": "F"}
]


caribbean_18th_century_pirates = [
    pirate_data for pirate, pirate_data in pirates_data_2.items()
    if pirate_data[2] == "Caribbean" and 1700 < pirate_data[0] <= 1800
]

num_caribbean_18th_century_pirates = len(caribbean_18th_century_pirates)
print("Number of pirates who sailed the Caribbean during the 18th century:",
      num_caribbean_18th_century_pirates)

longest_career_pirate = None
longest_career_duration = 0

for pirate, years in pirates_data_2.items():
    start_year, end_year = years[0], years[1]
    career_duration = end_year - start_year
    if career_duration > longest_career_duration:
        longest_career_duration = career_duration
        longest_career_pirate = pirate

print("Pirate with the longest career:", longest_career_pirate)
print("Longest career duration:", longest_career_duration, "years")

total_career_duration = 0
num_pirates = len(pirates_data_2)

for years in pirates_data_2.values():
    start_year, end_year = years[0], years[1]
    career_duration = end_year - start_year
    total_career_duration += career_duration

average_career_length = total_career_duration / num_pirates

print("Average career length:", average_career_length, "years")
 