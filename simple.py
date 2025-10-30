# Simple Interest Calculator

# Input values
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (per year): "))
time = float(input("Enter the time (in years): "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Display the result
print(f"Simple Interest = {simple_interest}")
