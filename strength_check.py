import re

def password_check_length(password):
	strength=0
	recomm=[]
	
	if len(password) >= 8:
		strength+=1
	else:
		recomm.append("increase your password length at least 8 characters")
	if len(password) >= 12:
		strength+=1
		
	if re.search(r"[A-Z]", password):
		strength+=1
	else:
		recomm.append("for more strong password add uppercase letters 🔠")
	if re.search(r"[a-z]", password):
		strength+=1
	else:
		recomm.append("for more strong password add lowercase letters 🔡")	
	if re.search(r"[0-9]", password):
		strength+=1
	else:
		recomm.append("for more strong password add digits 🔢")
	if re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=]", password):
		strength+=1
	else:
		recomm.append("for more strong password add special cases 🔣")
		
	strength=min(strength, 5)
	return strength, recomm
	
