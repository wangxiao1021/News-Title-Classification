res_tech = open("tech_index", "a+")

key_words = {"男装", "女装"}

with open("diff_file") as file:
    for line in file:
        diff, index, txt = line.strip().split("\t")
        if sum([1 if key_word in txt else 0 for key_word in key_words]) > 0:
            res_tech.write("%s\t%s\n" % (index, "时尚"))
