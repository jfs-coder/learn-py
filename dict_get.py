# trying out the dict.get() function. it takes a key as a argument and also a value for a default.

muh_dict = {"playstation": "PS5", "xbox": "Xbox Series X", "switch": "Nintendo Switch"}

def jarvis(s):
	return muh_dict.get(s.lower(), "Dreamcast")

print(jarvis("Playstation"))
print(jarvis("XboX"))
print(jarvis("Sega"))

