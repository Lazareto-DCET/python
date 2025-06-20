# Task 1.1
songs = ["Salamin Salamin", "Zero Pressure", "Secrets", "Cherry on Top", "Pantropiko"]
print(songs)

#Task 1.2
print(songs[0])  # First item
print(songs[-1]) # Last item
print(songs[2])  # Third item

#Task 2.1
songs.append("No Fear")         
songs.insert(1, "Huwag Muna Tayong Umuwi")               
print(songs)

#Task 2.2
songs.remove("Secrets")    # Remove by value
songs.pop(0)               # Remove by index
del songs[1]               # Delete specific index
print(songs)

#Task 2.3
songs[1] = "Blink Twice"
print(songs)

#Task 3.1
for song in songs:
    print(song)

#Task 3.2
for i in range(len(songs)):
    print(f"{i}: {songs[i]}")
    
numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)
print("Average:", average)

