import random
alphabetslow="abcdefghijklmnopqrstuvwxyz"
alphabetshigh="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Numbers="0123456789"
specialsymbols="!@#$%^&*()_?:;"
all_characters=alphabetslow+alphabetshigh+Numbers+specialsymbols

password_length = 12
while True:
 password="".join(random.choices(all_characters,k =password_length))
 print(f" Your Password is: {password}")
 op=input("Again genrate password ? ('Y' for yes and 'Q' for quit)")
 if op in ["q","Q"]:
  break