keyword_c=['main','char','int','float','return']
sym_ind=0
symtab=[None]*100
for i in range(100):
    symtab[i]=[None]*2
#######################################################################################################################
#printdatatype
def print_dtype(variable):
    for i in range(sym_ind):
        if(symtab[i][0]==variable):
            if(symtab[i][1]=="char"):
                return "%c"
            elif (symtab[i][1] == "int"):
                return "%d"
            elif (symtab[i][1] == "float"):
                return "%f"
            elif (symtab[i][1] == "double"):
                return "%f"
#######################################################################################################################
def isKeyword(variable):
    for i in range(len(keyword_c)):
        if(keyword_c[i]==variable):
            return 1
    return 0
#######################################################################################################################
def space(variable):
    if ' ' in variable:
        return 1
    return 0
#######################################################################################################################
def isVariable(variable):
    if(variable[0].isdigit()):
        return 1
    if (space(variable)):
        return 1
    return 0
#######################################################################################################################
def isExisting(variable):
    global symtab
    global sym_ind
    for i in range(sym_ind):
        if(variable==symtab[i][0]):
            return 1
    return 0
#######################################################################################################################
def insertintoSymTab(variable_arr,dtype):
    #print variable_arr
    #print dtype
    global symtab
    global sym_ind
    if(isExisting(variable_arr))==0:
        if(isVariable(variable_arr))==0:
            if(isKeyword(variable_arr))==0:
                symtab[sym_ind][0]=variable_arr
                symtab[sym_ind][1]=dtype
                sym_ind=sym_ind+1
    #print symtab






#testing portion
#testing="sachin"
#datatype="int"
#insertintoSymTab(testing,datatype)
#print symtab