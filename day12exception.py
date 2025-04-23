# 1. User se 2 numbers lo, divide karo
# 2. Agar galti ho toh proper message do
while True: 
    try:
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        print("Result:", a / b)

    except ZeroDivisionError:
        print("❌ Cannot divide by zero.")
    except ValueError:
        print("❌ Only numbers are allowed.")
    except Exception as e:
        print("Unknown error occurred:", e)
        
#         Ham todi na jante hai ke ZeroDivisionError, ValueError program me aayega ya nahi..."
# 👉 Bilkul sahi! Program kab kis situation me kya error de de — wo runtime pe hi pata chalta hai.

# "...ya koi aur error bhi aa sakta hai..."
# 👉 Haan bhai! Ho sakta hai TypeError, FileNotFoundError, IndexError, etc.

# "...usko handle karne ke liye ham except Exception as e use karte hai"
# 👉 ✅ Sahi! Ye humara "last shield" hota hai — koi bhi error ho, program crash na ho!

    finally:
        print("Program ended.")
