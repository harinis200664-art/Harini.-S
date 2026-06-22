print("*********************")
print("ELECTION VOTE COUNT")
print("*********************")
print("cndidates are..")
kn=input("1.ADMK \n2.DMK \n3.NTK")
n=int(input("enter the total number of votes:"))
votes=[]
for i in range(n):
      vote=input("enter your vote:")
      votes.append(vote)
admk=votes.count("admk")
dmk=votes.count("dmk")
ntk=votes.count("ntk")
print("votes in ADMK:",admk)
print("votes in DMK:",dmk)
print("votes in NTK:",ntk)
if admk>dmk and admk>ntk:
  print("admk win")
elif dmk>admk and dmk>ntk:
  print("dmk win")
elif ntk>admk and ntk>dmk:
  print("ntk win")
else:
  print("reelection")
