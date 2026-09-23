print("\t\t\t\t\tTV REMOTE")
print("1.ENTER CHANNEL NUMBER:")
print("2.NEXT CHANNEL")
print("3.BEFORE CHANNEL")
print("4.PENDRIVE PLAY")
print("5.VOLUME")
print("6.ON/OF")
volume=50
def channel_no():
    ch_no=int(input("\t\t\t\t\tENTER YOUR CHANNEL NUMBER:"))
    print("\t\t\t\t\tTHE CHANNEL",ch_no," IS DISPLAYING................") 
def next_channel():
    cur_ch=int(input("\t\t\t\t\tENTER YOUR CURRENT CHANNEL NUMBER:"))
    print("\t\t\t\t\tNEXT CHANNEL",cur_ch+1,"IS DISPLAYING....")
def before_channel():
    cur_ch=int(input("\t\t\t\t\tENTER YOUR CURRENT CHANNEL NUMBER:" ))
    print("\t\t\t\t\tBEFORE CHANNEL",cur_ch-1,"IS DISPLAYING..............")     
def pendrive_play():
    op=input("\t\t\t\t\tDO YOU INSERT YOUR PENDRIVE IN THE TV SOCKET(Y/N):")
    if op=="Y":
        print("\t\t\t\t\tDISPLAYING THE DETAILS IN THE DRIVE..............")
    else:
        print("\t\t\t\t\tYOU DID'T INSERT YOUR DRIVE!!!!!!")
def volume_i_d():
    v=input("\t\t\t\t\tDO YOU WANT TO INCREASE THE VOLUME OR DEGREASE(V+/V-):")
    if v=="V+":
        print("\t\t\t\t\tvolume:",volume+1,".........")
    else:
        print("\t\t\t\t\tVOLUME:",volume-1,"..........")                
def on_of():
    op=input("\t\t\t\t\tDO YOU WANT TO TURN ON OR OF(ON/OF):")
    if op=="ON":
        print("\t\t\t\t\tTV LOADING.............")
    else:
        print("\t\t\t\t\tTV POWER OFF...........")    
#FRONT END CODE.......
w="Y"
while w=="Y":
    tv_op=int(input("enter your option:"))
    if tv_op==1:
        print(channel_no())
    elif tv_op==2:
        print(next_channel())
    elif tv_op==3:
        print(before_channel())        
    elif tv_op==4:
        print(pendrive_play())    
    elif tv_op==5:
        print(volume_i_d())
    elif tv_op==6:
        print(on_of())
    else:
        print("INVALIED OPTION.............\nCONTACT YOUR CABIL OPERATOR..........\n ") 
w=input("DO YOU  WANT TO DO AGAIN(Y/N): ")


         

