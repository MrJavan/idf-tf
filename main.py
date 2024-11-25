import json



#file 1

f1 = open("data/file1.txt" , "r" , encoding="utf-8")
word1 = f1.read().split()

word_count = {}
files = ["data/file1.txt","data/file2.txt","data/file3.txt","data/file4.txt"]

for word in word1:
        cleaned_word = word.replace('.', '').replace('،', '')
        if len(cleaned_word) >= 3:
            if cleaned_word not in word_count:
                word_count[cleaned_word] = {"Total" : 1 ,"Count" : 1}
            else:
                word_count[cleaned_word]["Count"] += 1
                
for file in files:
    f = open(file , 'r' , encoding="utf-8")
    words = f.read().split()
    for item in words:
        cleaned_word = item.replace('.', '').replace('،', '')
        if len(cleaned_word) >=3:
            if cleaned_word not in word_count:
                word_count[cleaned_word] = {"Total" : 1 ,"Count" : 1}
            else:
                word_count[cleaned_word]["Total"] +=1


with open("outputs/output_file1.json", "w", encoding="utf-8") as outfile:
    json.dump(word_count, outfile, ensure_ascii=False, indent=4)


#file 2
word_count = {}

f2 = open("data/file2.txt" , "r" , encoding="utf-8")
word2 = f2.read().split()

for word in word2:
        cleaned_word = word.replace('.', '').replace('،', '')
        if len(cleaned_word) >= 3:
            if cleaned_word not in word_count:
                word_count[cleaned_word] = {"Total" : 1 ,"Count" : 1}
            else:
                word_count[cleaned_word]["Count"] += 1
                
for file in files:
    f = open(file , 'r' , encoding="utf-8")
    words = f.read().split()
    for item in words:
        cleaned_word = item.replace('.', '').replace('،', '')
        if len(cleaned_word) >=3:
            if cleaned_word not in word_count:
                word_count[cleaned_word] = {"Total" : 1 ,"Count" : 1}
            else:
                word_count[cleaned_word]["Total"] +=1


with open("outputs/output_file2.json", "w", encoding="utf-8") as outfile:
    json.dump(word_count, outfile, ensure_ascii=False, indent=4)

#file3

word_count = {}

f3 = open("data/file3.txt" , "r" , encoding="utf-8")
word3 = f3.read().split()

for word in word3:
        cleaned_word = word.replace('.', '').replace('،', '')
        if len(cleaned_word) >= 3:
            if cleaned_word not in word_count:
                word_count[cleaned_word] = {"Total" : 1 ,"Count" : 1}
            else:
                word_count[cleaned_word]["Count"] += 1
                
for file in files:
    f = open(file , 'r' , encoding="utf-8")
    words = f.read().split()
    for item in words:
        cleaned_word = item.replace('.', '').replace('،', '')
        if len(cleaned_word) >=3:
            if cleaned_word not in word_count:
                word_count[cleaned_word] = {"Total" : 1 ,"Count" : 1}
            else:
                word_count[cleaned_word]["Total"] +=1


with open("outputs/output_file3.json", "w", encoding="utf-8") as outfile:
    json.dump(word_count, outfile, ensure_ascii=False, indent=4)



#ifle 4

word_count = {}

f4 = open("data/file4.txt" , "r" , encoding="utf-8")
word4 = f4.read().split()

for word in word4:
        cleaned_word = word.replace('.', '').replace('،', '')
        if len(cleaned_word) >= 3:
            if cleaned_word not in word_count:
                word_count[cleaned_word] = {"Total" : 1 ,"Count" : 1}
            else:
                word_count[cleaned_word]["Count"] += 1
                
for file in files:
    f = open(file , 'r' , encoding="utf-8")
    words = f.read().split()
    for item in words:
        cleaned_word = item.replace('.', '').replace('،', '')
        if len(cleaned_word) >=3:
            if cleaned_word not in word_count:
                word_count[cleaned_word] = {"Total" : 1 ,"Count" : 1}
            else:
                word_count[cleaned_word]["Total"] +=1


with open("outputs/output_file4.json", "w", encoding="utf-8") as outfile:
    json.dump(word_count, outfile, ensure_ascii=False, indent=4)
