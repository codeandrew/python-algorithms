def markdownparser(markdown):
  print(markdown)
  arr = list(markdown)
  number = 0
  word =""
  [number += 1 if i is "#" else word += i for i in arr: ]
    # if i is "#" :
    # else: word += i


  # h = [i is " " for i,k in range(len(markdown)]
  # test = set([  c for c in range(len(markdown)) if '#' == c ])
  # print test
  w = word.strip()
  if w == "Invalid": return markdown

  return "<h{0}>{1}</h{0}>".format(int(number),w)

markdownparser("## test")
