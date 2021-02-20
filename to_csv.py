# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 23:33:22 2021

@author: YUvraj Dagur
"""
from json import load

DREAMERS = {
    "alta": "Alta: a detailed dreamer", "angie": "Angie: age 18 & 20", "arlie": "Arlie: a middle-aged woman", "b": "Barb Sanders", "b2": "Barb Sanders #2", "b-baseline": "Barb Sanders: baseline", "bay_area_girls_456": "Bay Area girls: Grades 4-6", "bay_area_girls_789": "Bay Area girls: Grades 7-9", "bea1": "Bea 1: a high school student", "bea2": "Bea 2: a college student", "blind-f": "Blind dreamers (F)", "blind-m": "Blind dreamers (M)", "chris": "Chris: a transvestite", "chuck": "Chuck: a physical scientist", "hall_female": "College women, late 1940s", "dahlia": "Dahlia: concerns with appearance", "david": "David: teenage dreams", "vonuslar.de": "Detlev von Uslar, auf Deutsch", "dorothea": "Dorothea: 53 years of dreams", "ed": "Ed: dreams of his late wife", "edna": "Edna: a blind woman", "elizabeth": "Elizabeth: a woman in her 40s", "emmas_husband": "Emma's Husband", "emma": "Emma: 48 years of dreams", "esther": "Esther: an adolescent girl", "german-f.de": "German dreams (F)", "german-m.de": "German dreams (M)", "norms-f": "Hall/VdC Norms: Female", "norms-m": "Hall/VdC Norms: Male", "jasmine1": "Jasmine 1: middle school", "jasmine2": "Jasmine 2: high school", "jasmine3": "Jasmine 3: college 1", "jasmine4": "Jasmine 4: college 2", "jeff": "Jeff: a lucid dreamer", "joan": "Joan: a lesbian", "kenneth": "Kenneth", "lawrence": "Lawrence, a young man", "mack": "Mack: A poor recaller", "madeline1-hs": "Madeline 1: High School", "madeline2-dorms": "Madeline 2: College Dorms", "madeline3-offcampus": "Madeline 3: Off-Campus", "madeline4-postgrad": "Madeline 4: After College", "mark": "Mark: a young boy", "melissa": "Melissa: a young girl", "melora": "Melora (Melvin's wife)", "melvin": "Melvin (Melora's husband)", "merri": "Merri: an artist", "miami-home": "Miami Home-Lab: Home", "miami-lab": "Miami Home-Lab: Lab", "midwest_teens-f": "Midwest teenagers (F)", "midwest_teens-m": "Midwest teenagers (M)", "nancy": "Nancy: Caring & headstrong", "natural_scientist": "The Natural Scientist", "norman": "Norman: a child molester", "pegasus": "Pegasus: a factory worker", "peru-m": "Peruvian men", "peru-f": "Peruvian women", "phil1": "Phil 1: teens", "phil2": "Phil 2: late 20s", "phil3": "Phil 3: retirement", "physiologist": "The Physiologist", "ringo": "Ringo: from the 1960s", "bosnak": "Robert Bosnak: A dream analyst", "samantha": "Samantha: in her 20s", "seventh_graders": "Seventh grade girls", "zurich-f.de": "Swiss children, auf Deutsch (F)", "zurich-m.de": "Swiss children, auf Deutsch (M)", "toby": "Toby: A friendly party animal", "tom": "Tom: An outgoing man", "ucsc_women": "UCSC women, 1996", "vickie": "Vickie: a 10-year-old girl", "vietnam_vet": "Vietnam Vet: 1970-2008 war dreams", "vietnam_vet2": "Vietnam Vet: 2015 dreams", "wedding": "Wedding dreams", "west_coast_teens": "West Coast teenage girls" }

dreamers = list(DREAMERS.keys())

dreams = []

for dreamer in dreamers:
    opener = f'dreams/{dreamer}.json'
    file = open(opener, encoding="UTF-8")
    dream_content = load(file)
    num_dreams = len(dream_content['dreams'])
    
    for i in range(num_dreams):
        dreams.append(dream_content['dreams'][i]['content'])
 
# Convert List to String and create a text file
def listToString(s):      
    # initialize an empty string 
    str1 = ""      
    # traverse in the string   
    for ele in s:  
        str1 += ele + '\n'
    # return string   
    return str1

dreams_string = listToString(dreams)

len(dreams_string)

with open("dreams.txt", "w", encoding="utf-8") as f:
    f.write(dreams_string)

import pandas as pd
# Convert list to dataframe and save as csv file format
dreams_dict = {'dreams': dreams}
df = pd.DataFrame(dreams_dict)

df.to_csv('dreams_final.csv')
