from wit import Wit
access_token="RZ6SA6JECFJI7T4ORY3WDCW2NON3VXUH"
client=Wit(access_token=access_token)
#######################################################################################################################
def wit_response(message_text):
    resp=client.message(message_text)
    entity=None
    value=None
    i=0
    j=0
    entity_c = len(list(resp['entities']))
    q = [None] * entity_c

    try:

        while(i<entity_c):
            entity=list(resp['entities'])[i]
            value_c = len(resp['entities'][entity])
            q[i] = [None] * (value_c+1)
            q[i][0]=entity
            while(j<value_c):
                value=resp['entities'][entity][j]['value']
                q[i][j+1]=value
                j=j+1
            i=i+1
            j=0
    except:
        pass
    return q

