def analyze_email(email_address):
    at_pos = email_address.find('@')
    if at_pos == -1:
        print('Невірний email')
        return
    login = email_address[:at_pos]
    domain = email_address[at_pos+1:]
    result = f"Email, {login}, {domain}"
    print(result)
    
    print('Email', login, domain, sep='|')


if __name__ == '__main__':
    analyze_email('student.mykhajlo_PI22@lpnu.com')
