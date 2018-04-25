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
fun_name="main"
stopstate=1
#######################################################################################################################
#find intent
def find_intent(b):
    global intent
    c = 0
    length=len(b)
    #print(length)
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
    global intent
    print intent
    if(intent=="read"):
        b.remove("read")

    var=""
    init_var=""
    c = 0
    for j in range(1, len(b)):
        var_count=var_count+1
        variable[c] = b[j]
        c = c + 1
        if (j + 1 != len(b)):
            init_var = init_var + "," + b[j + 1]
    if(b[1]=='read'):
        init_var='a'+init_var
    else:
        init_var=b[1]+init_var
    #print init_var
    if(lang=="c" and intent=="print"):
        var=init_var

    elif(lang=="cpp"and intent=="print"):
        var=init_var.replace(",","<<")

    elif(lang=="cpp"and intent=="read"):
        var = init_var.replace(",", ">>")

    elif(lang == "c" and intent == "read"):
        var = init_var.replace(",",",&")
        var="&"+var
    print variable
#######################################################################################################################
#works if the intent is declaration
def declaration(b,length):
    global var_count
    global program
    #print "declaration working"
    global d
    global init_var
    global datatype
    global fun_name

    for i in range(length):
        if(b[i][0]=="variable"):
            get_variable(b[i])
            d = d + 1
        if (b[i][0] == "datatype"):
            datatype = b[i][1]
            d = d + 1
    if(variable[0]==None):
        hello(response.getrespo(1))
    #print datatype
    if(datatype==None):
        hello(response.getrespo(2))
    if(d==2):
        #print (variable, datatype)
        #print var_count
        for i in range(var_count):
            a=variable[i]
            symbol_table.insertintoSymTab(a, datatype,fun_name)
        s= datatype+" "+init_var+";"
        #print s
        program=program+"\n"+s
        print program
        d=0
        var=""
        init_var=""
        var_count=0
        datatype=None

#######################################################################################################################
#works if the intent is initialization
def initialization(b, length):
    global program
    global d
    global a
    #print a
    #print "initialization"
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
        #print(var+";")
        v,lim=var.split("=")
        symbol_table.insertval(v,lim)
        program = program + var+";\n"
        var=""
        #print program
        d=0
#######################################################################################################################
#works if the intent is print
def print_st(b,length):

    global intent
    global program
    j=0
    c=""
    flag=0
    global variable
    global var_count
    global var
    global d_type
    global fun_name
    for i in range(length):
        if (b[i][0] == "variable"):
            get_variable(b[i])
        elif(b[i][0]=="p_string"):
            c =b[i][1]
            flag=1

    if(flag==0):
        for i in range(var_count):
            if j<var_count-1:
                c=c+symbol_table.print_dtype(variable[i],fun_name)+","
                j=j+1
            else:
                c=c+symbol_table.print_dtype(variable[i],fun_name)

    k=syntax_selection.type_print(lang, c, var,flag)

    program = program + k +"\n"
    print program
    var=""
    var_count=0
    datatype=None
#######################################################################################################################
#read fn
def read(b,length):
    global a
    global intent
    global program
    j = 0
    c = ""
    global variable
    global var_count
    global var
    global d_type
    global fun_name
    for i in range(length):
        if (b[i][0] == "variable"):
            get_variable(b[i])
            print var+"variable"
    for i in range(var_count):
        if j < var_count - 1:
            c = c + symbol_table.print_dtype(variable[i],fun_name)
            j = j + 1
        else:
            c = c + symbol_table.print_dtype(variable[i],fun_name)
    k = syntax_selection.type_read(lang, c, var)
    program = program + k + "\n"
    print program
    var_count = 0
    datatype = None
###############################################################################################################
#works if the intent is for
def for_st(b,length):
    global a
    global program
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
            program=program+syntax_selection.type_for(lang, v, l1, l2, 1)+"\n"
        else:
            program=program+syntax_selection.type_for(lang, v, l1, l2, 2)+"\n"
    else:
        if not l2.isdigit():
            test=symbol_table.checkval(l2)
            if test!=None:

                if l1 > test:
                    program = program + syntax_selection.type_for(lang, v, l1, l2, 1) + "\n"
                else:
                    program = program + syntax_selection.type_for(lang, v, l1, l2, 2) + "\n"
        if not l1.isdigit():
            test=symbol_table.checkval(l1)
            if test!=None:

                if test > l2:
                    program = program + syntax_selection.type_for(lang, v, l1, l2, 1) + "\n"
                else:
                    program = program + syntax_selection.type_for(lang, v, l1, l2, 2) + "\n"


#######################################################################################################################
#works if the intent is if_statement
def if_st(b,length):
    global a
    global program
    cond=a
    elim=['if','then','(',')']
    for i in range(len(elim)):
        cond=cond.replace(elim[i],"")
    cond.strip(" ")
    #print cond
    program=program+"if("+cond+")\n{\n"
#######################################################################################################################
#works if the intent is while_statement
def while_st(b,length):
    global a
    global program
    cond=a
    elim=['while','do','(',')']
    for i in range(len(elim)):
        cond=cond.replace(elim[i],"")
    cond.strip(" ")
    #print cond
    program=program+"while("+cond+")\n{\n"
############################################################################################################
def end_fn(b,length):
    global program
    global fun_name
    global stopstate
    program = program + "\n"
    stopstate=1
    if(length==1):
        print program
    fun_name="main"



#######################################################################################################################
def start_fn(b,length):
    global program
    global stopstate
    global fun_name
    if stopstate==0:
        print "Error:function inside function is not availabe"
    else:
        stopstate=0
        parameters=[None]*10
        for j in range (10):
            parameters[j]=[None]*2
        fun_name=b[1][1]
        print("enter the datatype")
        datatype=raw_input()
        s=input("is there any parameters 0 for yes 1 for no ")
        if(s==0):
            print("enter the parameters in the format datatype variablename")
        i=0
        while(s==0):
            parameters[i][0]=raw_input("Datatype")
            parameters[i][1] = raw_input("Variable Name")
            symbol_table.insertintoSymTab(parameters[i][1],parameters[i][0],fun_name)
            i=i+1
            s=input("do you want to continue 0 to continue or 1 to exit")
        program=program+syntax_selection.start(datatype,fun_name,parameters,i)
        print program
        i=0
        s=0

#########################################################################
#invokes when intent is found
def call_fn(b, length):
    func_name=b[1][1]
    parameters = [None] * 10
    for j in range(10):
        parameters[j] = [None] * 2
    fun_name = b[1][1]
    print("enter the datatype")
    datatype = raw_input()
    s = input("is there any parameters 0 for yes 1 for no ")
    if (s == 0):
        print("enter the parameters in the format datatype variablename")
    i = 0
    while (s == 0):
        parameters[i][0] = raw_input("Datatype")
        parameters[i][1] = raw_input("Variable Name")
        symbol_table.insertintoSymTab(parameters[i][1], parameters[i][0], fun_name)
        i = i + 1
        s = input("do you want to continue 0 to continue or 1 to exit")
    program = program + syntax_selection.start(datatype, fun_name, parameters, i)
    print program
    i = 0
    s = 0




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
    elif(intent == "start"):
        start_fn(b, length)
    elif (intent == "func_call"):
        call_fn(b, length)
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


