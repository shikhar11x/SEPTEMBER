dic ={"name": "shikhar",
      "phone no": "987654321",
      "email": "shikhar@gmail.com"}
work=input("what you want to do : \n"
           "add new contact -> add\n"
           "search contact -> src\n"
           "update contact -> upd\n"
           "view data -> show\n"
           "enter here ->> ")
if work=="add":
    n=input("enter the name")
    e=input("enter the email")
    p=input("enter the phone no")
    dic.update({"name": n})
    dic.update({"phone no": p})
    dic.update({"email": e})
    print(dic)