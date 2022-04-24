# a = "Roshni"
# b = "rosh_ch"
# c = "2Rosh"
# d = "Roshni Chauhan"

# print(a.isidentifier())
# print(b.isidentifier())
# print(c.isidentifier())
# print(d.isidentifier())

iden=input("Enter identifier")
if iden[0].isdigit():
    print("False")
elif " " in iden:
    print("False")
else:
   print("True")
