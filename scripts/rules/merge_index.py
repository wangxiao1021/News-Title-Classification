line_dict = dict()
with open("tech_index", "r") as file:
    for line in file:
        index, cate = line.strip().split("\t")
        line_dict[index] = cate

write_file = open("tech_index", "w")
for line in line_dict:
    write_file.write("%s\t%s\n" % (line, line_dict[line]))

write_file.close()
