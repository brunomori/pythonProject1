def notas(*n, sit=False):
    r=dict()
    r['total']=len(n)
    r['Maior']=max(n)
    r['Menor']=min(n)
    r['Media']=len(n)/len(n)
    if sit:
        if r['Media']>=7:
            r['Situação']='Boa'
        if r['Media']>=5:
            r['Situação']='Media'
        else:
            r['Situação']='Ruim'
    return r

resp=notas(5.5,2.5,1.5,sit=True)
print(resp)