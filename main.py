print("=== Your Adventure simulator ===")
print("""You'll be asked a bunch of questions then we'll make you up an amazing story with YOU as the star! """)
print()
name = input ("Your name: ")
enemy = input("Your worst enemy's name: ")
superpower = input("Your superpower: ")
print()
print("Our story begins as our hero name approaches a foreboding castle...")
print("Suddenly a bolt of lighting striked the ground at the feet of", name)
print("'Our final battle begins!' shouts the evil", enemy, "clearly missing the fact that", name, "has the power of", superpower, "which means they'll win quite easily")
print("\033[31m'Our final battle begins!'\033[0m shouts the evil", enemy, "clearly missing the fact that", name, "has the power of\033[35m", superpower, "\033[0mwhich means they'll win quite easily")

