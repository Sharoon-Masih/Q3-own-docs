# FROM may jo baseimage di hai wo 'node' iss lia di hai bcuz humna JS ki file run krni hai. and '20-alpine' yeh version hai node ka joka bilkul lightweight hai.
FROM node:20-alpine      

# now basic yeh jo working directory set krtay hain yeh iss lia hoti hai kay Docker Image may jo humari application hogi wo '/app' ka andar hogi taka later on agr humay kuch ADD, DELETE, COPY. kuch be krna hai toh hum usi directory ko follow kreinga like /app/hello-docker.js . So isi lia yebi zarori nhi kay '/app' (its convention) hi name rakhay hum kuch be name set krsktay hain like '/main ' but name yaad rakhna hai takay subsequent instruction jab pass krni ho toh easily working directory ma krdein.
WORKDIR /app 

# Now yeh COPY command iss lia use hoti hai takay localSystem say files/directories copy krkay then Docker image may filesystem may paste krdey.
# source -> 1st parameter isme wo source define krna hai jaha sa file copy krni hai.
# destination -> 2nd parameter isme wo path btana hai jaha par yeh sb file/directory jo copy ki hain paste hongi.
# But yaha nichay menay '. .' krdia what does mean by it ? iska mtlb basic yeh hai jo first '.' hai uska mtlb hai right now machine may or we can say vscode may ma jis level pa hun uspa jitni be files hai sab ko copy krlo. 
# second '.' ka mtlb hai Docker Image jis current directory may hain waha paste krdo, Ab kiu kay humnay uper WORKDIR may /app set hai toh its mean currently we are in '/app' ab agr hum '.' ki jagah '/app' be krdeinga toh wobi same hi bt hai.extra: But agr hum chahtay hain kay jo humari files hain wo direct '/app' may nhi paste hon balkay '/app' may koi folder ma hojaye store so we can define it like this as well: '/app/files/' yehi benefit hai WORKDIR define krnay ka.
COPY . .

# Now ab hum ek default command add krdeingay takay jasa hi humara container start ho toh wo command chl jaye.
# here we have used 'shell form' syntax, we can also use executeable form syntax as well.
CMD node hello-docker.js 
