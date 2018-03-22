#type print
def type_print(lang,c,var):
    if(lang=='c'):
        return 'printf(\"'+c+'",'+var+');'
    elif(lang=='cpp'):
        return 'cout<<'+var+';'
#######################################################################################################################
def type_for(lang,v,l1,l2,state):
    if((lang=="c")or(lang=="cpp")):
        if(state==1):
            return 'for('+v+'='+l1+';'+v+'>'+l2+';'+v+'--)\n{'
        elif(state==2):
            return 'for('+v+'='+l1+';'+v+'<'+l2+';'+v+'++)\n{'


