import requests

url1="https://api.adviceslip.com/advice"
url2="https://uselessfacts.jsph.pl/api/v2/facts/random"

op=input("----- What you want (an advice) or some (random fact) ? -----\n '1' for an advice\n '2' for a random fact \n")
if op=="1":
   while True:
    response1=requests.get(url1)
    if response1.status_code == 200:
     data=response1.json()
     advice=data["slip"]["advice"]
     print(f" Today's advice is : {advice}")
    else:
     print("Invalid API key!")
    op1=input("Wanna print one more? ('q' for quit)")
    if op1 in ["Q","q"]:
      break 
elif op=="2":
   while True:
    response2=requests.get(url2)
    if response2.status_code == 200: 
     data=response2.json()
     fact = data["text"]
     print(f"Today's Fact is : {fact}")
    else:
     print("Invalid API key!!") 
    op1=input("Wanna print one more? ('q' for quit)")
    if op1 in ["Q","q"]:
        break  