post = input('write a post here: ')
rawPostList = post.lower().split(' ') # yaha par zarori nhi kay pehlay string ko list ma convert krein or then 'in' ka through check krein bcuz jo 'in' keyword hai wo string ma say be check krleta hai. 
if 'harry' in rawPostList:
    print('yes in this post you are talking about harry')
else:
    print('no you are not talking about harry')
