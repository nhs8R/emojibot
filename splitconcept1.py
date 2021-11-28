






def split(whole,maxl):
    sendable=[]
    for i in range((len(whole)//maxl)+1):
        temparray=[]
        for index in range(maxl):
            try:
                temparray.append(whole[index+(i*maxl)])
            except:
                pass
        sendable.append(''.join(temparray))
    return sendable



