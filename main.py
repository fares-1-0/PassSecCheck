from strength_check import password_check_length
from display_result import display_result
from check_common import check_common
from hash_pass import check_pwned_password

def audit_pass(password):
    print("=" * 50)
    print("Checking password..... wait.. 😪")
    print("=" * 50)
    
    #---Check 1: strength
    strength, recomm = password_check_length(password)
    display_result(strength, recomm)
    #---Check 2: common 
    if check_common(password):
        print("\n⚠️ Warning: this is one of the most common weak passwords!")
    else:
        print("\n✅ Password not found in the common passwords list")
    #---Check 3: breach database
    print("\n🌐 Checking against the breach database...")
    count, error = check_pwned_password(password)
    if error:
        print(error)
    elif count > 0:
        print(f"🔴 Serious warning: this password appeared {count:,} times in real data breaches!")
        print("   You should change it immediately if you use it anywhere.")
    else:
        print("✅ This password was not found in any known breach\n")

    print("=" * 50)

# entry point
if __name__ == "__main__":
    usr_password = input("Enter Password To Check It: ")
    audit_pass(usr_password)
    
