import regex as re

list_with_presents = ["HELLO","MOUSE","TRAIN"]

regex_string = "M...E"

r = re.compile(regex_string)

final_list = list(filter(r.match,list_with_presents))

print(final_list)