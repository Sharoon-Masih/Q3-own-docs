# match case -> its same like a switch case in JS/TS. or python 

def http_status(status):
    match status:
        case 200:
            return 'OK'
        case 404:
            return 'Not Found'
        case 500:
            return 'Internal server error'
        case _: # iska mtlb haka agr uper walay case false hojayeingay toh yeh by default case return hojayega.
            return 'Unknown status'
        
print(http_status(200)) # agr case '200' hoga toh 'OK' return hojayega.
print(http_status(404))