import time
class UNESCO:
    def __init__(self):
        print(" WELCOME TO UNESCO.org ")
        print("-------------------------------")
        self.heritage_sites = []

    def login(self, user, password):
        au = 'admin'
        ap = 'govt@official'
        gu = 'public'
        gp = "visitor"
        if (au == user and ap == password):
            return 1
        elif (user == gu and gp == password):
            return 2
        else:
            return 0

    def add_sites(self):
        name = input(" Enter the name of the site ")
        state = input("Enter the State ")
        district = input('Enter the district ')
        year = input("Enter the year when {name} was established ".format(name=name))
        reason = input(" Why it was established ")
        website = input("Enter the website link of the {} ".format(name))
        details = dict()
        details = {
            'Name': name,
            'State': state,
            'District': district,
            'Year': year,
            'Info': reason,
            'Website': website
        }
        self.heritage_sites.append(details)

    def display(self):
        for sites in self.heritage_sites:
            for key, value in sites.items():
                print("{}  -  {}".format(key.upper(), value.upper()))
            print('--------------------------------------------')

    def display_state(self, state):
        found=[]
        for sites in self.heritage_sites:
            
            if (state in sites.values()):
                found.append(sites['Name'])
        if(found==[]):    
            print("State  not found")
        else:
            print('SITES FOUND in ',state )
            print(' , '.join(found))
        

    def display_site(self, site):
        for sites in self.heritage_sites:
            if (site == sites['Name']):
                for key, value in sites.items():
                    print("{0} - {1}".format(key.upper(), value.upper()))
                return

        print(" HERITAGE SITE NOT FOUND ")

    def delete_site(self, site):
        for sites in self.heritage_sites:
            if (site == sites['Name']):
                self.heritage_sites.remove(sites)
                return
        print("Site not found")


h = UNESCO()
attempts=3
print("Enter the username and password correctly 3 wrong attempts will lead to account block ")

session=99
for i in range(1,session):
    c=input("Enter 'c' to continue and 'end' to stop ")
    
    if(c=='end'):
        print('Session interrupted')
        break
    if session==0:
        break
    user = input(" Enter the username ")
    password = input(" Enter the password ")
    if (h.login(user, password) == 1):
        
        print(" You Are ADMIN ")
        print()
        command = input(" Enter 'a' to add and 's' to display and 'd' to delete site ")
        if (command == 'a'):

            while True:
                stp = input(" Enter 'Stop' to stop adding   PRESS ANY KEY TO CONTINUE ")
                if (stp == 'Stop'):
                    print("YOU CANNOT ENTER ANY MORE")
                    h.display()
                    break
                h.add_sites()
        elif (command == 's'):
            display_type = input(" Enter 'display full' to display all or 'search' for specific display ")
            if (display_type == 'display full'):
                h.display()
            elif (display_type == 'search'):
                site = input(" Enter the site to display ")
                h.display_site(site)
            else:
                print(" Invalid display type ")
        elif (command == 'd'):
            site = input(" Enter the site to delete ")
            h.delete_site(site)
            h.display()
        else:
            print(" Invalid Operation ")
    elif (h.login(user, password) == 2):
        
        print(" You Are VISITOR ")
        print()
        command = input(" Enter s to display by search and d to display all ")
        if (command == 's'):
            search_type = input("Enter search type 'v' to search by site or 'l' to see sites in the location ")
            if (search_type == 'v'):
                site = input(" Enter the site to display ")
                h.display_site(site)
            elif (search_type == 'l'):
                state = input("Enter the State ")
                h.display_state(state)
            else:
                print(' Invalid search operation ')
        elif (command == 'd'):
            h.display()
        else:
            print(" Invalid Command ")
    else:
        attempts-=1
        print("Wrong user id or password Re - login {} attempts left ".format(attempts))
        if attempts==0:
            print("Account blocked ")
            time.sleep(60)



