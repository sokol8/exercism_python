from sgf_parsing import parse, SgfTree

#expected = SgfTree(properties={'A': ['B']})
#print(expected)

input_string = '(;a[b])'
parse(input_string)
