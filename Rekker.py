import math
def Solver(teller, nevner, teller_operator,operasjons_tall_teller, nevner_operator,operasjons_tall_nevner, iterasjoner):
    midlertidig_resultat = teller/nevner
    for i in range (0 , iterasjoner):
        match teller_operator:
            case "*":
                teller = teller * (operasjons_tall_teller)
            case "/":
                teller = teller / (operasjons_tall_teller)
            case "+":
                teller = teller + (operasjons_tall_teller)
            case "-":
                teller = teller - (operasjons_tall_teller)

        match nevner_operator:
            case "*":
                nevner = nevner * (operasjons_tall_nevner)
            case "/":
                nevner = nevner / (operasjons_tall_nevner)
            case "+":
                nevner = nevner + (operasjons_tall_nevner)
            case "-":
                nevner = nevner - (operasjons_tall_nevner)
            case "!":
                nevner = nevner * (i+operasjons_tall_nevner)
        midlertidig_resultat += teller/nevner
    return midlertidig_resultat


#5.26
#  Løsning = Solver(1, 3, "+" , 2 , "+" , 2 , 48)

#5.27
#Løsninger = []
#for n in range (1,11):
#    print(4* Solver(1,1,"*",-1,"+",2,n*10000))

#5.28
for n in range (1,11):
    print(f"{Solver(1,1,'+',0,'!',1,n*10000):.100f}")
