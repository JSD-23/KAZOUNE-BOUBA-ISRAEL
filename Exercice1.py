def lengthOfLastWord(s):
  mots = ['0' if s =="" else s.split(" ")]
  print(len(mots[-1][-1]))