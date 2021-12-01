strings = ['abc','xyz','cac','54325']
print("List string : ",strings)
counter = 0
for string in strings:
    if (len(string)>2) and (string[0]==string[len(string)-1]):
        print("- "+string)
        counter+=1
print("Terdapat "+str(counter)+" string yang memenuhi kriteria")