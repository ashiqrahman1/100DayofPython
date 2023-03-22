sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Conver string to list
new_list = sentence.split(" ")

result = {word: len(word) for word in new_list}
print(result)
