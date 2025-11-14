#Randomly selects a part of the number that is in the list, type, ....
def rend_number(n,t):
	rend={str(i) for i in range(n,t)}
	rend_list_number=list(rend)
	return int(rend_list_number[0])
#For a group of things
def rend_section(x):
	rendset=set(x)
	return list(rendset)
# For one thing
def rend_name(*nam):
	rendname=set(nam)
	return  list(rendname)
#Splitting the name and choosing a random part	
def rend_for(name):
	rendfor={fname for fname in name}
	rendlist_s=list(rendfor)
	return rendlist_s[0]
