import request_wit_backend
import symbol_table
import syntax_selection
import response
lang="c"
var_count=0
program=""
a=""
d=0
statement=None
operator=[None]*5
variable = [None] * 5
datatype=None
intent=None
var=""
init_var=""
#######################################################################################################################
#find intent
def find_intent(b):
    global intent
    c = 0
    length=len(b)
    print(length)
    for i in range(length):
        if (b[i][0] == "intent"):
            #print(b[i][1])
            intent=b[i][1]
            switch_intent(b[i][1],b,length)
            c = 1
    if (c == 0):
        print("sorry not available")
#######################################################################################################################
#get variable
def get_variable(b):
    global lang
    global var_count
    global var
    global init_var
    var=""
    init_var=""
    c = 0
    for j in range(1, len(b)):
        var_count=var_count+1
        variable[c] = b[j]
        c = c + 1
        if (j + 1 != len(b)):
            init_var = init_var + "," + b[j + 1]
    init_var=b[1]+init_var
    print init_var
    if(lang=="c"):
        var=init_var
    elif(lang=="cpp"):
        var=init_var.replace(",","<<")
#######################################################################################################################
#works if the intent is declaration
def declaration(b,length):
    global var_count
    global program
    print "declaration working"
    global d
    global init_var
    global datatype

    for i in range(length):
        if(b[i][0]=="variable"):
            get_variable(b[i])
            d = d + 1
        if (b[i][0] == "datatype"):
            datatype = b[i][1]
            d = d + 1
    if(variable[0]==None):
        hello(response.getrespo(1))
    print datatype
    if(datatype==None):
        hello(response.getrespo(2))
    if(d==2):
        print (variable, datatype)
        print var_count
        for i in range(var_count):
            a=variable[i]
            symbol_table.insertintoSymTab(a, datatype)
        s= datatype+" "+init_var+";"
        print s
        program=program+"\n"+s
        print program
        d=0
        var=""
        var_count=0
        datatype=None

#######################################################################################################################
#works if the intent is initialization
def initialization(b, length):
    global program
    global d
    global a
    print a
    print "initialization"
    for i in range(length):
        if(b[i][0]=="variable"):
            d=d+1
        elif(b[i][0]=="operators"):
            d=d+1
        elif(b[i][0]=="intent"):
            d=d+1
        else:d=d+1
    if(d==3):
        var = a.replace("set ","")
        print(var+";")
        program = program + var+";"
        var=""
        print program
        d=0
#######################################################################################################################
#works if the intent is print
def print_st(b,length):
    global intent
    j=0
    c=""
    global variable
    global var_count
    global var
    global d_type
    for i in range(length):
        if (b[i][0] == "variable"):
            get_variable(b[i])
    for i in range(var_count):
        if j<var_count-1:
            c=c+symbol_table.print_dtype(variable[i])+","
            j=j+1
        else:
            c=c+symbol_table.print_dtype(variable[i])
    print(syntax_selection.type_print(lang, c, var))
#######################################################################################################################
#read fn
def read(b,length):
    global a
    print a

#works if the intent is for
def for_st(b,length):
    global a
    #print a
    cond=a
    elim=['for','to','do','(',')']
    for i in range(len(elim)):
        cond=cond.replace(elim[i],"")
    cond.strip(" ")
    v,lim=cond.split('=')
    v=v.replace(" ","")
    #l1 and l2 are the limits and v is the variable
    l1,l2=lim.split()
    #check for numeric non numeric functions
    if l1.isdigit() and l2.isdigit():
    #l1 and l2 comparisons
        if l1>l2:
            print(syntax_selection.type_for(lang,v,l1,l2,1))
        else:
            print(syntax_selection.type_for(lang,v,l1,l2,2))
    else:
        print("under construction")
#######################################################################################################################
#works if the intent is if_statement
def if_st(b,length):
    global a
    cond=a
    elim=['if','then','(',')']
    for i in range(len(elim)):
        cond=cond.replace(elim[i],"")
    cond.strip(" ")
    print cond
    print("if("+cond+")\n{")
#######################################################################################################################
#works if the intent is while_statement
def while_st(b,length):
    global a
    cond=a
    elim=['while','do','(',')']
    for i in range(len(elim)):
        cond=cond.replace(elim[i],"")
    cond.strip(" ")
    print cond
    print("while("+cond+")\n{")
############################################################################################################
def end_fn(b,length):
    print("}\n")



#######################################################################################################################
#invokes when intent is found
def switch_intent(intent,b,length):
    if(intent=="declaration"):
        declaration(b,length)
    elif(intent=="initialization"):
        initialization(b,length)
    elif(intent=="print"):
        print_st(b,length)
    elif (intent == "if statement"):
        if_st(b, length)
    elif(intent=="for statement"):
        for_st(b,length)
    elif(intent=="while statement"):
        while_st(b,length)
    elif (intent == "read"):
        read(b, length)
    elif (intent=="end"):
        end_fn(b,length)
    else:
        print("Under construction")
#######################################################################################################################


#main function
def hello(s):
    global a
    a=raw_input(s)
    b=request_wit_backend.wit_response(a)
    print(b)
    find_intent(b)

def demo_main():
    global a
    while(a!="stop"):
        hello("Enter the string")

demo_main()


