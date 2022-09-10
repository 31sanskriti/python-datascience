#keywords arguments - kwargs



def saveinfo(file ='info.txt',**kwargs):
    with open(file,'a')as f:
        for k,v in kwargs.items():
            f.write(f'{k}->{v}\n')

saveinfo(mobile='motorola',price = 20000,expiry = 2023,
         features = 'kuch khas ni')

