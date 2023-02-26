from collections import defaultdict
def solve(names):
   dic = defaultdict(int)
   res = []
   for name in names:
      if name not in dic:
         dic[name] += 1
         res.append(name)
      else:
         newname = name +'(' + str(dic[name]) + ')'
         while newname in dic:
            dic[name] += 1
            newname = name +'(' + str(dic[name]) + ')'
         dic[newname] = 1
         res.append(newname)
   return res
names = ["doc", "doc", "image", "doc(1)", "doc"]
print(solve(names))