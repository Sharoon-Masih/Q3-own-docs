s = set()
s.add(20); 
s.add(20.0); 
s.add('20'); 

print("set: ",s,"\t its length: ",len(s)) # iski length 2 iss lia ayi hai bcuz jo 20.0 hai and 20 hai wo same consider honga iss lia set ma jo element hongay that are {20,'20'}, han agr 20.1 hota toh wo same consider nhi hota.