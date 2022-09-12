user_feeling = input("How are you feeling? ")

good_emotions = ["ok","good","amazing","great","happy"]

good = False

for emotion in good_emotions:
    if emotion in user_feeling:
        print("thats great!")
        good = True
        break

if not good:
    print("oh")
 
