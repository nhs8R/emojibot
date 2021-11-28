
def getreddit(link):

    import re

    def locateall(needle,haystack):
        return ([m.start() for m in re.finditer(r'(?={})'.format(re.escape(needle)), haystack)])



    def stop():
        while True:
            pass


    pastelength = 24

    if ('send') in link:
        print('send in link')
        link=list(link)
        for i in range(5):
            link.pop(0)
        link=''.join(link)

    from urllib.request import Request, urlopen



    import requests
    print('start','using link',link)

    from urllib import request

    response = request.urlopen(link)

    page_source = response.read().decode('utf-8')
    #print(page_source)

    webpage = page_source

    webpage = str(webpage)
    #print(webpage)
    print('end')
    unit='[{"e":"text"'

    where=locateall(unit,webpage)
    #print((where))

    end=webpage.find("profileCommentsPage")
    print(end)

    old=where
    new=[]

    for i in range(len(old)):
        if old[i]<end:
            new.append(old[i])
        

    where=new



    #print(where)




    whole=[]


    for i in range(len(where)):
        run=True
        currentarray=[]
        index=0
        while run==True:
            focus=index+(where[i])
            currentarray.append(webpage[focus])
            if webpage[focus]=='"':
                #print('1')
                if webpage[focus+1]=='}':
                    #print('2')
                    if webpage[focus+2]==']':
                        #print('3')
                        run=False
            index+=1

            
        whole.append(''.join(currentarray))
            
    notwanted=["'","[","]","{","}",'\\',unit]
    #print(whole)

    for i in range(len(whole)):
        whole[i]=((str(whole[i]).replace(unit,'')))
        whole[i]=((str(whole[i]).replace(',"t":','')))
    whole=''.join(whole)
    for i in range(len(notwanted)):
        whole.replace(notwanted[i],'')
    whole.replace('""','\n')
    return(whole)

#print(getreddit('https://www.reddit.com/r/AmItheAsshole/comments/qtibq3/aita_for_telling_my_dad_that_if_he_choses_to/'))


