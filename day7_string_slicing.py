text = "Python"

print(text[0])     # P → first character
print(text[-1])    # n → last character (negative indexing)
print(text[1:4])   # yth → slice from index 1 to 3
print(text[:3])    # Pyt → from start to index 2
print(text[3:])    # hon → from index 3 to end

# ✅ String indexing 0 se start hoti hai
# ✅ Negative indexing -1 se start hoti hai (last character)
# ✅ Slicing mein last index exclusive hota hai


name = "himanshu khare"

print(name.upper())      # H... uppercase
print(name.lower())      # h... lowercase
print(name.title())      # Himanshu Khare
print(name.capitalize()) # Himanshu khare
print(name.find("shu"))  # Index where 'shu' starts
print(name.replace("khare", "coder"))  # replace word

# ✅ String methods original string ko modify nahi karte, new string return karte hain
