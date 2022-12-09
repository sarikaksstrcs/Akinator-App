database= [
	{"name":"Prithviraj Sukumaran", "Actor":True, "human":True, "Indian":True,"Writer":False,"Politics":False },
	{"name":"Tom Hanks", "Actor":True, "human":True, "Indian":False, "Writer":False,"Politics":False},
	{"name":"Barack Obama", "Actor":False, "human":True, "Indian":False,"Writer":False,"Politics":True},
	{"name":"Manu S Pillai", "Actor":False, "human":True, "Indian":True,"Writer":True,"Politics":False},
	{"name":"Sashi tharoor", "Actor":False, "human":True, "Indian":True,"Writer":True, "Politics":True},
	{"name":"Arnold Schawtsnagger ", "Actor":True, "human":True, "Indian":False, "Writer":False,"Politics":True}
]

def Try_chance(ppty,value):
	for d in database:
		if d[ppty]!= value:
			database.remove(d)
	
Qn = ["Actor","human","Indian","Writer","Politics"]

for i in Qn:
	
	ans = input("Is "+i+": ")
	if ans == 'n':
		Try_chance(i,False)
	else:
		Try_chance(i,True)

	if(len(database)==1):
		print(database[0]["name"])
