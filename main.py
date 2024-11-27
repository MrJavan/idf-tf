import json
import math

#file 1
files = ["data/file1.txt","data/file2.txt","data/file3.txt","data/file4.txt"]

f1 = open("data/file1.txt" , "r" , encoding="utf-8")
word1 = f1.read().split()

word_count = {}
tword = 0

for  x in word1:
    cleaned_word = x.replace('.','').replace('،', '')
    if len(cleaned_word) >= 3:
        tword += 1

# print(tword)

for word in word1:
        cleaned_word = word.replace('.', '').replace('،', '')
        if len(cleaned_word) >= 3:
            if cleaned_word not in word_count:
                word_count[cleaned_word] = {"Total" : 1 ,"Count" : 1 , "TF-ALG" : 0, "IDF-ALG" : 0, "IDF-TF" : 0}
            else:
                
                word_count[cleaned_word]["Count"] += 1
                # word_count[cleaned_word]["TF-ALG"] = word_count[cleaned_word]["Count"] / tword

for word in word1:
        cleaned_word = word.replace('.', '').replace('،', '')
        if len(cleaned_word) >= 3:
            if cleaned_word in word_count:
                word_count[cleaned_word]["TF-ALG"] = word_count[cleaned_word]["Count"] / tword



for file in files:
    f = open(file , 'r' , encoding="utf-8")
    words = f.read().split()
    for item in words:
        cleaned_word = item.replace('.', '').replace('،', '')
        if len(cleaned_word) >=3:
            if cleaned_word in word_count:
                word_count[cleaned_word]["Total"] +=1
                word_count[cleaned_word]["TF-ALG"] = word_count[cleaned_word]["Count"] / tword
                word_count[cleaned_word]["IDF-ALG"] = math.log(word_count[cleaned_word]["Total"] / word_count[cleaned_word]["Count"] + 1)
                word_count[cleaned_word]["IDF-TF"] = word_count[cleaned_word]["IDF-ALG"] * word_count[cleaned_word]["TF-ALG"]

#file2-----


f2 = open("data/file2.txt" , "r" , encoding="utf-8")
word2 = f2.read().split()

word_count = {}
tword = 0

for  x in word2:
    cleaned_word = x.replace('.','').replace('،', '')
    if len(cleaned_word) >= 3:
        tword += 1

# print(tword)

for word in word2:
        cleaned_word = word.replace('.', '').replace('،', '')
        if len(cleaned_word) >= 3:
            if cleaned_word not in word_count:
                word_count[cleaned_word] = {"Total" : 1 ,"Count" : 1 , "TF-ALG" : 0, "IDF-ALG" : 0, "IDF-TF" : 0}
            else:
                
                word_count[cleaned_word]["Count"] += 1
                # word_count[cleaned_word]["TF-ALG"] = word_count[cleaned_word]["Count"] / tword

for word in word2:
        cleaned_word = word.replace('.', '').replace('،', '')
        if len(cleaned_word) >= 3:
            if cleaned_word in word_count:
                word_count[cleaned_word]["TF-ALG"] = word_count[cleaned_word]["Count"] / tword



for file in files:
    f = open(file , 'r' , encoding="utf-8")
    words = f.read().split()
    for item in words:
        cleaned_word = item.replace('.', '').replace('،', '')
        if len(cleaned_word) >=3:
            if cleaned_word in word_count:
                word_count[cleaned_word]["Total"] +=1
                word_count[cleaned_word]["TF-ALG"] = word_count[cleaned_word]["Count"] / tword
                word_count[cleaned_word]["IDF-ALG"] = math.log(word_count[cleaned_word]["Total"] / word_count[cleaned_word]["Count"] + 1)
                word_count[cleaned_word]["IDF-TF"] = word_count[cleaned_word]["IDF-ALG"] * word_count[cleaned_word]["TF-ALG"]



with open("outputs/output_file2.json", "w", encoding="utf-8") as outfile:
    json.dump(word_count, outfile, ensure_ascii=False, indent=4)


#file3-----


f3 = open("data/file3.txt" , "r" , encoding="utf-8")
word3 = f3.read().split()

word_count = {}
tword = 0

for  x in word3:
    cleaned_word = x.replace('.','').replace('،', '')
    if len(cleaned_word) >= 3:
        tword += 1

# print(tword)

for word in word3:
        cleaned_word = word.replace('.', '').replace('،', '')
        if len(cleaned_word) >= 3:
            if cleaned_word not in word_count:
                word_count[cleaned_word] = {"Total" : 1 ,"Count" : 1 , "TF-ALG" : 0, "IDF-ALG" : 0, "IDF-TF" : 0}
            else:
                
                word_count[cleaned_word]["Count"] += 1
                # word_count[cleaned_word]["TF-ALG"] = word_count[cleaned_word]["Count"] / tword

for word in word3:
        cleaned_word = word.replace('.', '').replace('،', '')
        if len(cleaned_word) >= 3:
            if cleaned_word in word_count:
                word_count[cleaned_word]["TF-ALG"] = word_count[cleaned_word]["Count"] / tword



for file in files:
    f = open(file , 'r' , encoding="utf-8")
    words = f.read().split()
    for item in words:
        cleaned_word = item.replace('.', '').replace('،', '')
        if len(cleaned_word) >=3:
            if cleaned_word in word_count:
                word_count[cleaned_word]["Total"] +=1
                word_count[cleaned_word]["TF-ALG"] = word_count[cleaned_word]["Count"] / tword
                word_count[cleaned_word]["IDF-ALG"] = math.log(word_count[cleaned_word]["Total"] / word_count[cleaned_word]["Count"] + 1)
                word_count[cleaned_word]["IDF-TF"] = word_count[cleaned_word]["IDF-ALG"] * word_count[cleaned_word]["TF-ALG"]



with open("outputs/output_file3.json", "w", encoding="utf-8") as outfile:
    json.dump(word_count, outfile, ensure_ascii=False, indent=4)



#file4-----


file4 = open("data/file4.txt" , "r" , encoding="utf-8")
word4 = file4.read().split()

word_count = {}
tword = 0

for  x in word4:
    cleaned_word = x.replace('.','').replace('،', '')
    if len(cleaned_word) >= 3:
        tword += 1

# print(tword)

for word in word4:
        cleaned_word = word.replace('.', '').replace('،', '')
        if len(cleaned_word) >= 3:
            if cleaned_word not in word_count:
                word_count[cleaned_word] = {"Total" : 1 ,"Count" : 1 , "TF-ALG" : 0, "IDF-ALG" : 0, "IDF-TF" : 0}
            else:
                
                word_count[cleaned_word]["Count"] += 1
                # word_count[cleaned_word]["TF-ALG"] = word_count[cleaned_word]["Count"] / tword

for word in word4:
        cleaned_word = word.replace('.', '').replace('،', '')
        if len(cleaned_word) >= 3:
            if cleaned_word in word_count:
                word_count[cleaned_word]["TF-ALG"] = word_count[cleaned_word]["Count"] / tword



for file in files:
    f = open(file , 'r' , encoding="utf-8")
    words = f.read().split()
    for item in words:
        cleaned_word = item.replace('.', '').replace('،', '')
        if len(cleaned_word) >=3:
            if cleaned_word in word_count:
                word_count[cleaned_word]["Total"] +=1
                word_count[cleaned_word]["TF-ALG"] = word_count[cleaned_word]["Count"] / tword
                word_count[cleaned_word]["IDF-ALG"] = math.log(word_count[cleaned_word]["Total"] / word_count[cleaned_word]["Count"] + 1)
                word_count[cleaned_word]["IDF-TF"] = word_count[cleaned_word]["IDF-ALG"] * word_count[cleaned_word]["TF-ALG"]



with open("outputs/output_file4.json", "w", encoding="utf-8") as outfile:
    json.dump(word_count, outfile, ensure_ascii=False, indent=4)