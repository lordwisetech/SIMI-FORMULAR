def speed():
    d = float(input("Enter distance (m): "))
    t = float(input("Enter time (s): "))
    print("Speed =", d / t, "m/s")

def force():
    m = float(input("Enter mass (kg): "))
    a = float(input("Enter acceleration (m/s²): "))
    print("Force =", m * a, "N")

def pressure():
    f = float(input("Enter force (N): "))
    A = float(input("Enter area (m²): "))
    print("Pressure =", f / A, "Pa")

def ohms_law():
    I = float(input("Enter current (A): "))
    R = float(input("Enter resistance (Ω): "))
    print("Voltage =", I * R, "V")

def kinetic_energy():
    m = float(input("Enter mass (kg): "))
    v = float(input("Enter velocity (m/s): "))
    print("Kinetic Energy =", 0.5 * m * (v ** 2), "J")

while True:
    print("\nChoose a formula:")
    print("1. Speed")
    print("2. Force")
    print("3. Pressure")
    print("4. Ohm's Law")
    print("5. Kinetic Energy")
    print("6. Exit")

    choice = input("Enter choice (1-6): ")

    if choice == "1":
        speed()
    elif choice == "2":
        force()
    elif choice == "3":
        pressure()
    elif choice == "4":
        ohms_law()
    elif choice == "5":
        kinetic_energy()
    elif choice == "6":
        print("Bye!")
        break
    else:
        print("Invalid option, try again!")
