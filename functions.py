#invoking a function

def character_USP(l):
    if l=="joey":
        print("character_USP:Funniest!")
    elif l=="rachel":
        print("character_USP:American Dream")
    elif l=="chandler":
        print("character_USP:Sarcastic AF")
    elif l=="Phoebe":
        print("character_USP:Weird")
    elif l=="ross":
        print("character_USP:Nerdy")
    elif l=="monica":
        print("character_USP:Fastidious..")
    else:
        print("character_USP not found")
l=input("Name:")
character_USP(l)
input("Got your answer?")
