FROM node:20-alpine

WORKDIR /app

# now here you can see that we provide this path 'second-Docker-img/src' for copying file but its not correct bcuz jo path for copying files/directory ka liya dena hai that shoould relative to dockerfile so kiu kay humari dockerfile hi second-docker-img may hai toh iss lia agr humay 'src' toh just we will put 'src'.

# COPY second-Docker-img/src /app/source
COPY ./src /app/source

# ab yaha nichay JSON array jo mena path define kia hai isme 2nd parameter ma direct jo file execute krni hai uska name nhi likha that is 'main.js' blka pura path define kia hai, wo iss liya bcuz agar uper COPY ki command may destination-path dekhay toh usmay jo humari '/app' hai usme ek or directory '/source' ma hum sari files store krwa rahay hain jo './src' say copy ki hain. isi lia "/app/source/main.js" wala path waha define kia hai.
# ab yaha ek sawal haka agar humnay destination-path '/app/source' rakha hai toh its mean jo humari './src' wo '/app/source' iss destination pay paste hogi toh phr toh humay nichay execute may "/app/source/src/main.js" iss tarah sa define krna chaiya tha, But asa nhi hota bcuz basically jo humna './src' di hai wo isko copy nhi krega blkay iskay andar jitni be files hain un sab ko copy krega or '/app/source' iss destination pa store krdega.
CMD ["node","/app/source/main.js"] 