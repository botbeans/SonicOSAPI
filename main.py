from sonicapi import *

def create_tenant() -> bool:
    """ Ask the user if a new tenant will need to be created for
      the firewall prior to calling the API call"""
    
    choice = input("Would you like to create a new Tenant? (Y/N)")
    while choice.lower() not in ("y", "n"):
        choice = input("Invalid response. Please enter 'Y/N'")
    
    return choice.lower() == "y"
    
    

def main():
    default_username = "admin"
    default_password = input("Enter in login password...")
    s = sonicapi("192.168.168.168", default_username, default_password)
    print(s.auth())
    #print(s.tenant_count())
    #print("Connection to NSM API successfull")

    

if __name__ == "__main__":
    main()