from tabulate import tabulate
pirates = [
    {"name": "Pirate", "sex": "M", "death_age": 40,
        "height": 6.4, "skull_cross": "F"},
    {"name": "BlackBeard", "sex": "F", "death_age": 24,
        "height": 6.4, "skull_cross": "T"},
    {"name": "Anne_Bonny", "sex": "M", "death_age": 37,
        "height": "5.6", "skull_cross": "T"},
    {"name": "Calico_Jack", "sex": "M", "death_age": 39,
        "height": "5.6", "skull_cross": "F"},
    {"name": "Cheung_Po_Tsai", "sex": "F", "death_age": 73,
        "height": "5.3", "skull_cross": "F"},
    {"name": "Grace O'Malley", "sex": "F", "death_age": 36,
        "height": 5.0, "skull_cross": "T"},
    {"name": "Mary_Read", "sex": "F", "death_age": 75,
        "height": 5.1, "skull_cross": "F"},
    {"name": "Sayyida_al_Hurra", "sex": "F", "death_age": 69,
        "height": 5.3, "skull_cross": "F"},
    {"name": "Ching_Shih", "sex": "M", "death_age": 56,
        "height": 5.5, "skull_cross": "F"},
    {"name": "Sir_Francis_Drake", "sex": "M",
        "death_age": 56, "height": 6.2, "skull_cross": "F"},
    {"name": "Jean Lafitte", "sex": "M", "death_age": 46,
        "height": 6.2, "skull_cross": "F"}
]
#total number of Skull and cross bones
skull_cross_total = 0
for pirate in pirates:
    skull_cross = pirate['skull_cross']
    if skull_cross == 'T':
        skull_cross_total = skull_cross_total +1
print (skull_cross_total)

#Which sex lives longer?
male_death_age= 0
number_of_male_deaths = 0
number_of_female_deaths = 0
femail_death_age= 0
for pirate in pirates:
    sex = pirate['sex']
    age = pirate['death_age']
    if sex == 'M':
        male_death_age += int(age)
        number_of_male_deaths += 1
    elif sex == 'F':
        femail_death_age += int(age)
        number_of_female_deaths += 1
male_death_average = male_death_age/number_of_male_deaths 
femail_death_average = femail_death_age /number_of_female_deaths
print(male_death_average, femail_death_average)
if male_death_average > femail_death_age:
    print("Male pirates live longer than female pirates")
else:
    print("Female pirates live longer than male pirates")
