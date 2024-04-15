import random as r
import unicodeit as uni

def select_ques(selected,dic):
    ques = r.choice(dic)
    if(ques in selected):
        ques = select_ques(selected,dic)
        
    return ques
def print_ques_comb(dic1,dic2,opt1,opt2,sc):
    sel_ques = []
    dic_ques = list(dic1)+list(dic2)
    for i in range(10):
        print()
        try:
            sel_ques.append(select_ques(sel_ques,dic_ques))
            ques = sel_ques[len(sel_ques)-1]
            if(ques in opt1):
                print(f"Q{i+1}.{ques}\n{opt1[ques]}")
                c = int(input("Select Your Choice : "))
                if(c == dic1[ques]):
                    print("Correct Answer !! +5 points.")
                    sc +=5
                else:
                    print(f"Wrong Answer !!\n Correct Answer is Option {dic1[ques]}")
            elif(ques in opt2):
                print(f"Q{i+1}.{ques}\n{opt2[ques]}")
                c = int(input("Select Your Choice : "))
                if(c == dic2[ques]):
                    print("Correct Answer !! +5 points.")
                    sc +=5
                else:
                    print(f"Wrong Answer !!\n Correct Answer is Option {dic2[ques]}")
        except Exception as e:
            print(e)
    return sc
def print_ques(dic1,opt1,sc):
    sel_ques = []
    for i in range(10):
        print()
        try:
            sel_ques.append(select_ques(sel_ques,list(dic1)))
            ques = sel_ques[len(sel_ques)-1]
            print(f"Q{i+1}.{ques}\n{opt1[ques]}")
            c = int(input("Select Your Choice : "))
            if(c == dic1[str(ques)]):
                print("Correct Answer !! +5 points.")
                sc +=5
            else:
                print(f"Wrong Answer !!\n Correct Answer is Option {dic1[ques]}")
        except Exception as e:
            print(e)
            return
    return sc            
def main():
    score = 0

    gs_q = {"What is the chemical symbol for the element Gold ?":1,"What is the process by which plants convert light energy into chemical energy ?":2,"Which Planet is known as Red Planet ?":2,"What is the pH value of Pure Water ?":2,"What is the function of Human Respiratory System ?":1,"Which process involves the conversion of a solid directly into a gas without passing through the liquid state?":2,"What is the main function of the nervous system?":3,"Which of the following is a Green House Gas ?":2,"What is the SI unit of Current ?":3,"What is the main function of the kidneys in the human body?":1,"Which of the is NOT a primary colour of light ?":4}
    gs_opt = {"What is the chemical symbol for the element Gold ?":"1. Au\n2. Ag\n3. Gd\n4. Gr","What is the process by which plants convert light energy into chemical energy ?":"1. Respiration\n2. Photosynthesis\n3. Transpiration\n4. Fermentation","Which Planet is known as Red Planet ?":"1. Venus\n2. Mars\n3. Jupiter\n4. Saturn","What is the pH value of Pure Water ?":"1. 5\n2. 7\n3. 9\n4. 10","What is the function of Human Respiratory System ?":"1. Transportation of Oxygen in the blood\n2. Digestion of Food\n3.Pumping blood to the body\n4. Excretion of waste products","Which process involves the conversion of a solid directly into a gas without passing through the liquid state?":"1. Evaporation\n2. Sublimation\n3. Condensation\n4. Melting","What is the main function of the nervous system?":"1. Regulation of Body Temperature\n2. Movement of Muscles\n3. Control and Coordination of Body Activities\n4. Digeston of Food","Which of the following is a Green House Gas ?":f"""1. Oxygen (O{uni.replace("2")})\n2. Carbon Dioxide (CO{uni.replace("2")})\n3. Nitrogen (N{uni.replace("2")})\n4. Hydrogen (H{uni.replace("2")})""","What is the SI unit of Current ?":"1. Watt\n2. Ohm\n3. Ampere\n4.Volt","What is the main function of the kidneys in the human body?":"1. Regulation of blood sugar levels\n2. Filtration of blood and waste removal\n3. Production of digestive enzymes\n4. Regulation of body temperature","Which of the is NOT a primary colour of light ?":"1.Red\n2. Blue\n3. Yellow\n4. Green"}


    comp_ques = {"Which of the following is the correct abbreviation of COMPUTER?":4,"Who is the father of Computers?":2,"Which of the following language does the computer understand?":3,"Which of the following computer language is written in binary codes only?":2,"Which of the following is the smallest unit of data in a computer?":1,"Which of the following unit is responsible for converting the data received from the user into a computer understandable format?":2,"Which of the following is not a type of computer code?":1,"Which of the following is designed to control the operations of a computer?":3,"Which of the following device use positional notation to represent a decimal number?":2,"Which of the following defines the assigned ordering among the characters used by the computer?":3}
    comp_opt = {"Which of the following is the correct abbreviation of COMPUTER?":"1. Commonly Occupied Machines Used in Technical and Educational Research\n2. Commonly Operated Machines Used in Technical and Environmental Research\n3. Commonly Oriented Machines Used in Technical and Educational Research\n4. Commonly Operated Machines Used in Technical and Educational Research","Who is the father of Computers?":"1. James Gosling\n2. Charles Babbage\n3. Dennis Ritchie\n4. Bjarne Stroustrup","Which of the following language does the computer understand?":"1. Computer understands only C Language\n2. Computer understands only Assembly Language\n3. Computer understands only Binary Language\n4. Computer understands only BASIC","Which of the following computer language is written in binary codes only?":"1. pascal\n2. machine language\n3. C\n4. C#","Which of the following is the smallest unit of data in a computer?":"1. Bit\n2. KB\n3. Nibble\n4. Byte","Which of the following unit is responsible for converting the data received from the user into a computer understandable format?":"1. Output Unit\n2. Input Unit\n3. Memory Unit\n4. Arithmetic & Logic Unit","Which of the following is not a type of computer code?":"1. EDIC\n2. ASCII\n3. BCD\n4. EBCDIC","Which of the following is designed to control the operations of a computer?":"1. User\n2. Application Software\n3. System Software\n4. Utility Software","Which of the following device use positional notation to represent a decimal number?":"1. Pascaline\n2. Abacus\n3. Computer\n4. Calculator","Which of the following defines the assigned ordering among the characters used by the computer?":"1. Accumulation\n2. Sorting\n3. Collating Sequence\n4. Unicode"}
    
    print("""****************** QUIZ GAME ******************""")
    name = input("Enter You Good Name : ")
    print(f"Welcome {name} !")
    c = input("Please Select fields of Questions :- \n1. General Knowledge \n2. Computer \nYou can select multiple queestions !\n").split(" ")
    if(len(c)==1 and c[0]=="1"):
        score = print_ques(gs_q,gs_opt,score)
    elif(len(c)==1 and c[0]=="2"):
        score = print_ques(comp_ques,comp_opt,score)
    elif(len(c)==2 and c[1]=="2"):
        score = print_ques_comb(comp_ques,gs_q,comp_opt,gs_opt,score)
    print(score)
    c = input("Would you like to Try Again ? \n Press (Y/N) :")
    if(c == "y" or c == "Y"):
        main()
    else:
        print(f"Thanks For Playing the Game !! \nHave a great day {name}")
if __name__ == "__main__":
    main()