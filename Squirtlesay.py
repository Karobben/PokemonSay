#!/usr/bin/env python3
'''
This script is for samply keep typing a
Squirtel on you terminal
Please Enjoy it
'''
import os, time, sys
from pyparsing import *

INPUT =  sys.argv[1]
Squirt_list1 = ['     AAAA         AAA', '    ADDDDAA      ADDDA', '   ADDDDDDDAA   ADDDDDA', '   ADDDDDDDABAA ADDDADA', '  ABDDDDDDDDBBBADDDADDA', '  ADDDDFADDDFBBBADDADDA', '  ADDDDABDDDFBBBADAAAA', '   ADDDABDDDAFBBBAA', '    AADDDDAADDFBBA', '    ADAAAADDDDFBBA', '     AACCADDDAFBBA', '       ACCAAAAFBBA', '      ADACCCCCAFA', '       AAAACCDAFA', '          AAADAA', '           ADDDA', '            AAA']
Squirt_list2 = ['', '    AAAA           AAA', '   ADDDDAA        ADDDA', '  ADDDDDDDDAA    ADDDDDA', '  ADDDDDDDDABAA  ADDDADA', ' ADDDDDDDDDDBBBAADDDADDA', ' ADDDDFADDDDFBBBADDADDA', ' ADDDDABDDDDFBBBADAAAA', '  ADDDABDDDDAFBBBAA', '   AADDDDDAADDFBBA', '     AACCADDDAFBBA', '       ACCAAAAFBBA', '      ADACCCCCAFA', '       AAAACCDAFA', '          AAADAA', '           ADDDA', '            AAA']


Squir_patern = {" ":"  ",
'A':'\x1b[7;30;40mAA\x1b[0m'  , 'B':'\x1b[7;31;41mB\u2580\x1b[0m',
"C":"\x1b[6;33;43mCC\x1b[0m"  , "D":"\x1b[6;34;44mDD\x1b[0m",
'E':'\x1b[30;0;2mEE\x1b[0m'   , 'F':'\x1b[7;37;47mEE\x1b[0m'  }

def Squrt_pos(Num):
    S_dict = {0:Squirt_list1, 1:Squirt_list2}
    return S_dict[Num%2]

def Squrt(Num):
  Result = ""
  for i in Squrt_pos(Num):
    Line_tmp = ""
    for ii in i:
      Line_tmp += Squir_patern[ii]
    Result += Line_tmp + "\n"
  #os.system("clear")
  return Result

def tailN_rm(String):
  String = String+"\n+_____tag"
  return String.replace("\n\n+_____tag",'')

def len_UC(String):
  ESC = Literal('\x1b')
  integer = Word(nums)
  escapeSeq = Combine(ESC + '[' + Optional(delimitedList(integer,';')) +
                  oneOf(list(alphas)))
  nonAnsiString = lambda s : Suppress(escapeSeq).transformString(s)
  unColorString = nonAnsiString(String)
  return(len(unColorString))

def Comple(TB):
  N_sp = 0
  line_T = len(TB.split("\n"))
  for i in range(line_T):
    if len_UC(TB.split("\n")[i]) > N_sp:
      N_sp = len_UC(TB.split("\n")[i])
  result = ""
  for i in range(line_T):
    result += TB.split("\n")[i]+" "*(N_sp-len_UC(TB.split("\n")[i]))+'\n'
  result = tailN_rm(result)
  return result

def Easy_Com(A_l,A_r,N_blank=2):
  result = ''
  Ll = len(A_l.split('\n'))
  Lr = len(A_r.split('\n'))
  for i in range(Ll):
    if i > (Lr-1):
      AR = len_UC(A_r.split('\n')[0])*" "
    else:
      AR = A_r.split('\n')[i]
    result += A_l.split('\n')[i] +N_blank*" " +AR + "\n"
  result += "\n======="
  return result.replace("\n\n=======",'')

def Saysomething(something):
    Num_input = len(something.encode('gbk'))
    T_rows, T_columns = os.popen('stty size', 'r').read().split() # get window size
    Num_T  = int(T_columns)
    Num_T = Num_T -20
    Line_w = int(Num_input / (Num_T+1))
    if Line_w > 0:
        #slice
        A = ""
        Result = []
        tmp = ""
        for i in range(len(something)):
            if len(tmp.encode('gbk')) < Num_T:
                tmp += something[i]
            else:
                Result +=[tmp]
                tmp = something[i]
        Result += [tmp]
        for i in Result:
            BN_N = Num_T - len(i.encode('gbk')) +1
            A += '\x1b[33;7;6m' + i +" " *BN_N+'\x1b[0m'+'\n'
    else:
        A ='\x1b[6;31;44m' + str(something) + '\x1b[0m'+'\n'
    A += '\x1b[33;34;6m\u2588\x1b[0m\x1b[33;34;6m\u2580\x1b[0m'
    return str(A)

Num = 0
while 1 == 1:
    Num += 1
    Words = Saysomething(INPUT)
    W_pop = Comple(" \n"*(len(Words.split("\n")) - 1)+tailN_rm(Squrt(Num)))
    W_pop = Easy_Com(W_pop,Words,0)
    os.system("clear")
    print(W_pop)
    time.sleep(0.6)

    #Squrt(Squirt_list1)
    ##Squrt(Squirt_list2)
    #time.sleep(0.5)
