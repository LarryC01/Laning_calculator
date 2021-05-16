#!/usr/bin/python

# this is the main function

# def success(me, opponent):
#     if attack(me) >= defense(opponent):
#         print "can win"
#     else:
#         print "can not win, sorry"
#     return
#
# # this is attack function
#
# def attack(me):
#     return basic_attack(me)
#class My_attack():


# def __init__(name, level):
#     self.name = name
#     self.level = level
        # self.q_attack = q_attack
        # self.w_attack = w_attack
        # self.e_attack = e_attack
        # self.r_attack = r_attack

    # ''' No dragon, no buffs, no attacking speed. '''
def __Attack__(name,level):
        # '''return __basicAttack__(level) + __Conqueror__(level) + ... '''
    basic = __basicAttack__(name,level)
    runes = __Conqueror__(name, level) + __AF__(name)
    c_items = __BC__(name) + __TF__(name)
    p_items = __DB__(name) + __LS__(name) + __P__(name)
    crit = __Crit__(name)
    auto_attack = (basic + runes + c_items + p_items) * (1 + crit)
    str_a = "For every auto attack, {0:s} have {1:.2f} damage at level {2}. \n"
    print(str_a.format(name, auto_attack, level))
    return auto_attack

def __basicAttack__(name,level):
        # '''self.level = level'''
    lv_b = float(level)
    lv_ad = 66 + 4.5 * lv_b
    str_b = "The basic attack of {0:s} at level {1} is: {2:.2f}\n"
    print (str_b.format(name, level, lv_ad))
    return lv_ad

def __Conqueror__(name,level):
        #''' Assume: 10 stacks already. '''
    lv_c = float(level)
    C_ad = (10.941 + 1.059 * lv_c) * haveConqueror(name)
    str_C = "The Conqueror attack of {0:s} at level {1} is: {2:.2f}\n"
    print (str_C.format(name, level, C_ad))
    return C_ad

def haveConqueror(name):
        input_runes = input("Enter yes if you take Conqueror rune: \n")
        if input_runes.lower() == "yes":
            return 1
        else:
            print ("You don't have Conqueror runes.\n")
            return 0

def __AF__(name):
        input_num_AF = int(input("Enter numbers of Adaptive Force you have: \n"))
        if ((input_num_AF < 0) or (input_num_AF > 2)):
            print ("Sorry, invalid numbers.\n")
            return 0
        else:
            res = float(5.4 * input_num_AF)
            str_AF = "AD gained by Adaptive Force in your runes is: {0:.2f}\n"
            print(str_AF.format(res))
            return res

def __P__(name):
        input_phage = input("Enter yes if you take Phage: \n")
        if input_phage.lower() != "yes":
            return 0
        else:
            return 15
def __LS__(name):
        input_ls = input("Enter yes if you take Long Sward: \n")
        if input_ls.lower() != "yes":
            return 0
        else:
            return 10
def __DB__(name):
        '''No life steal at the moment. '''
        input_db = input("Enter yes if you take Doran Blade: \n")
        if input_db.lower() != "yes":
            return 0
        else:
            return 8

def __BC__(name):
        input_bc = input("Enter yes if you take Black Cleaver: \n")
        if input_bc.lower() != "yes":
            return 0
        else:
            return 40
    #
    # def __BC__(self):
    #     input_bc = input("Enter yes if you take Black Cleaver: \n")
    #     if input_bc.lower() != "yes":
    #         return 0
    #     else:
    #         return 40

def __TF__(name):
        '''Brief model of TF. '''
        input_tf = input("Enter yes if you take Trinity Force: \n")
        if input_tf.lower() != "yes":
            return 0
        else:
            return 20

def __Crit__(name):
        input_crit = int(input("Enter number of the percentage of critical damage: \n"))
        return float(input_crit / 100)

'''So here is test case 0. '''





#myChampion = My_attack(n,l)
# print(n)
# print(l)
# print(__Attack__(n,l))

def q_attack(name, level):
    if int(level) < 1:
        return 0
    elif (1 <= int(level) < 8):
        return 0.3
    elif (8 <= int(level) < 10):
        return 0.6
    elif (10 <= int(level) < 12):
        return 0.9
    elif int(level) == 12:
        return 1.2
    else:
        return 1.5

# print("The attack coefficient by Q for {0:s} to auto_attack is {1:.1f} at current level {2}\n ".format(n, float(q_attack(n,l)), l))

def w_attack(name, level):
    if name.lower() == "garen":
        print("Garen can not attack by his W.\n")
    else:
        print("More champions would be added in the future. Looking forward to updates!")
    return 0

# print(w_attack(n,l))

def e_attack(name, level):
    print("Assume 6 spins and only 1 opponent on laning phase. ")
    if int(level) < 2:
        return 0
    elif (2 <= int(level) < 4):
        return 30
    elif (4 <= int(level) < 5):
        return 60
    elif (5 <= int(level) < 7):
        return 90
    elif (7 <= int(level) < 9):
        return 120
    else:
        return 150

# print(e_attack(n,l))
'''print("Accepted. Test case 0 completed.")'''



#om = float((o_armor + 100) / 100)

# def r_attack(name,level, ol):
#     l_ = int(level)
#     ol_ = float(ol)
#     if 1 < l_ < 6:
#         return 0
#     elif 6 <= l_ < 11:
#         return (ol_ + 750) / 6
#     elif 11 <= l_ < 16:
#         return (ol_ + 1200) / 5
#     else:
#         return (3 * ol_ + 4000) / 13
# print(r_attack(n, l, ol))

def spell(name, level):
    '''Some champions take ignites. '''
    check = str(input(("Enter your spell:\n")))
    i = float(level)
    i_damage = 50 + 20 * i
    if check.lower() == "ignite":
        return int(i_damage)
    else:
        return 0
# print(spell(n,l))

def combo(name,level,ol,o_armor):
    x = float(level)
    y = float(ol)
    z = float(100 / (o_armor + 100))
    print("For combo, we suppose that there exists A-->Q-->A-->E-->(ignite)-->R for garen in assumption case.\n")
    a = __Attack__(name, level)
    # print(str(a))
    pre_R = a + q_attack(name, level) * a + e_attack(name, level) + spell(name, level)
    # print(str(pre_R))
    # return pre_R
    real_pre_R = pre_R * (1 - z)
    # print(str(real_pre_R))
    # for_ult = float(y - real_pre_R)
    # print(str(for_ult))
    r_d = 0.0
    if x < 6:
        r_d = 0
    elif 6 <= x < 11:
        r_d = 150 + 0.2 * real_pre_R
    elif 11 <= x < 16:
        r_d = 300 + 0.25 * real_pre_R
    elif 16 < x:
        r_d = 450 + 0.3 * real_pre_R
    # print(str(r_d))
    return real_pre_R + r_d

#print(combo(n,l,ol, o_armor))
def can_win(name, level, ol, o_armor):
    c = float(combo(name,level,ol,o_armor))
    curr_o = float(ol)
    if c >= curr_o:
        return ("Congrats! You are able to win this 1v1 fight by combo.\n")
    else:
        return ("Sorry, the your damage is {0:.2f}, not enough. You need {1:.2f} damage.\nGlhf, try next time or ping for help.\n".format(c, curr_o - c))
# test!
print("***LOL (top lane) laning calculator launched.***\n")
n = str(input("Enter name of your champion: \n"))
    #print("Hello,")
print("Hello, the summoner of {0:s}\n".format(n))

if n.lower() != "garen":
    print("More functions for other champions coming soon as the program updates!\n")
    print("Meanwhile, only Garen can be tested.\n")
else:
    l = int(input("Enter current level of your champion: \n"))

    on = str(input("Enter name of your opponent's champion: \n"))

    ol = int(input("Enter health of {0:s}.\nShould be an integer: \n".format(on)))

    o_armor = int(input("Enter armor of {0:s}.\nShould be an integer: \n".format(on)))

    if (l < 0) or (l > 18) or (l - int(l) != 0) :
        print("Invalid inputs. Try again.\n")
    else:
        print(can_win(n, l, ol, o_armor))

print("***This just simulates the ideal cases in laning.***\n")
print("***Use it at your risk.***\n")
print("***Data from op.gg and lol wiki.***\n")
print("***In the possible future updated versions, more champions will come.***\n")
print("***For jungle, mid, adc, support champions, glad to hear your ideas.***\n")
print("***Will connected to API if possible (future versions). ***\n")
print("***Thanks for downloading my program. Suggestions are welcome.***\n")
print("***Version: 0.0***\n")
print("***Produced by Larry Chen***")
    # def __CdG__(self):
    #     input
    # def __itemsAttack__( itemsAD):
    #   str_w = "The items attack of {0:s} is: {1:f}\n"
    #   print (str_w.format(self.name, itemsAD))
    #   return itemsAD
    #
    # def __runesAttack__( runesAD):
    #   str_r = "The runes attack of {0:s} is: {1:f}\n"
    #   print (str_r.format(self.name, runesAD))
    #   return runesAD
    #
    # def __critAttack__( critAD):
    #   str_c = "The critical attack of {0:s} is: {1:f}\n"
    #   print (str_c.format(self.name, critAD / 100))
    #   return critAD



    #''' other functions comes '''

    # ''' this is the inner class, of q, w, e and r '''
    # class Q_ad:
    #     def inner_q( level, items, runes):
    #         self.level = level
    #         self.items = items
    #         self.runes = runes
    # class W_ad:
    #     def inner_w( level, items, runes):
    #         self.level = level
    #         self.items = items
    #         self.runes = runes
    # class E_ad:
    #     def inner_w( level, items, runes):
    #         self.level = level
    #         self.items = items
    #         self.runes = runes
