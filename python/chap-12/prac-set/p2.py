list = [1,3,5,6,7,4,8,7]

for idx,n in enumerate(list): # yaha idx varaible may index number lia.
    match idx+1: # yaha on the basis of index num match kreinga.
        case 3: # yaha cases define krdia kay inme say kisi case say match hoga toh display hoga otherwise kuch be nhi hoga.
            print(f"Found {n} at position {idx+1}")
        case 5:
            print(f"Found {n} at position {idx+1}")
        case 7:
            print(f"Found {n} at position {idx+1}")