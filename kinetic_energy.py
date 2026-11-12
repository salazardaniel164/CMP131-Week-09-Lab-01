#Daniel E Salazar Gomez
#CMP-131-86520
#Week 9 
#Lab 01
#Assigment 9
#11/12/2026
def kineticEnergy(m,v):
    Ke=0.5*m*v*v
    return Ke
def main():
    m=float(input("Enter the object's mass in kilograms:"))
    v=float(input("Enter the object's velocity in meters per second:"))
    if m < 0 or v < 0:
        print("Error: Mass and velocity cannot be negative.")
    else:
        kinetic_energy=kineticEnergy(m,v)
        print("Kinetic Energy Results")
        print("-------------------------")
        print("Mass:", m, "kg")
        print("Velocity:", v, "m/s")
        print("Kinetic Energy: {:.2f} joules".format(kinetic_energy))
main()

