import random as rn

#creat subjects
subjects = [
    "Shahrukh khan",
    "Virat knoli",
    "Nirmala sitharaman",
    "A mumbai cat",
    " A group of Monkey",
    "Prime Minister modi",
    "balen",
    "Kp oli",
]

actions = [
    "lanuncesh",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "clebrates",
]

places_or_things = [
    " at Red Fort",
    "in Mumbai local train",
    "a plate of somosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate"
]

# start the headline generation loop

while True:
    subject = rn.choice(subjects)
    action = rn.choice(actions)
    place_or_thing = rn.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo you wnat another headline? (yes/no): ").strip().lower()

    if user_input == "no":
        break

print("\nThanks fro using the Fake news headline generator.Have a fun day")
