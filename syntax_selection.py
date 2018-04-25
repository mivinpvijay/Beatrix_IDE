#type print
def type_print(lang,c,var,type):
    if(lang=='c'and type==0):
        return 'printf(\"'+c+'",'+var+');'
    elif (lang == 'c' and type == 1):
        return 'printf(\"' + c + '"'+ ');'
    elif(lang=='cpp'and type==0):
        return 'cout<<'+var+';'
    elif(lang=='cpp'and type==1):
        return 'cout<<"'+c+'";'
#######################################################################################################################
def type_for(lang,v,l1,l2,state):
    if((lang=="c")or(lang=="cpp")):
        if(state==1):
            return 'for('+v+'='+l1+';'+v+'>'+l2+';'+v+'--)\n{'
        elif(state==2):
            return 'for('+v+'='+l1+';'+v+'<'+l2+';'+v+'++)\n{'
##################################################################################################
#type read
def type_read(lang,c,var):
    if(lang=='c'):
        return 'scanf(\"'+c+'",'+var+');'
    elif(lang=='cpp'):
        return 'cin>>'+var+';'
##################################################################################################

def start(datatype,endname,parameters,j):
    req_par=''
    i=0
    if(parameters[0][0]==None):
        return datatype+" "+endname+"(){\n"
    else:
        while (i<j-1):
            req_par=req_par+parameters[i][0]+' '+parameters[i][1]+','
            i=i+1
        req_par=req_par+parameters[i][0]+' '+parameters[i][1]
        return datatype+" "+endname+"("+req_par+"){\n"

def call(datatype,endname,parameters,j):
    req_par = ''
    i = 0
    if (parameters[0][0] == None):
        return datatype + " " + endname + "(){\n"
    else:
        while (i < j - 1):
            req_par = req_par + parameters[i][0]+ ','
            i = i + 1
        req_par = req_par + parameters[i][0] + ' ' + parameters[i][1]
        return endname + "(" + req_par + "){\n"
