naics = open("data/full_naics07.txt","r").readlines()
f = open("data/final_naics.txt","w+")
for line in naics:
    try:
        theseParts = line.split("\t")
        naics_code = (theseParts[1])
        if len(naics_code)==4:
            print naics_code
            f.write(naics_code+"\n")

    except:
        continue

