#Daniel E Salazar Gomez
#CMP-131-86520
#Week 9 
#Lab 01
#Assigment 9
#11/12/2026
def main():
    m=float(input(""))
    v=float(input(""))
    ke= KineticEnergy(m,v)
    display(ke)
main()
def kineticenergy(m,v):
    Ke=0.5*m*v*v
    return Ke
def Display (ke):
    print("",ke)
