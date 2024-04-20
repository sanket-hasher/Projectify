
class UNESCO:
    def __init__(self):
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
        year = int(input("Enter the year when {name} was established ".format(name=name)))
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
                print("{}  -  {}".format(key, value))

    def display_state(self, state):
        for sites in self.heritage_sites:
            for key, value in sites.items():
                if (state in value):
                    print("Name of the Heritage - ", sites['Name'])
                    return
        print("State or district not found")

    def display_site(self, site):
        for sites in self.heritage_sites:
            if (site == sites['Name']):
                for key, value in sites.items():
                    print("{0} - {1}".format(key, value))
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
print("Enter details 1")
h.add_sites()
print("Enter details 2")
h.add_sites()
"""
print("Enter details 3")
h.add_sites()"""
h.display()
session=2
for i in range(1,10):
    if session==0:
        break
    user = input(" Enter the username ")
    password = input(" Enter the password ")
    if (h.login(user, password) == 1):
        session-=1
        print(" You Are ADMIN ")
        print()
        command = input(" Enter 'a' to add and 's' to display and 'd' to delete site ")
        if (command == 'a'):

            while True:
                stp = input(" Enter 'Stop' to stop adding ")
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
        else:
            print(" Invalid Operation ")
    elif (h.login(user, password) == 2):
        session-=1
        print(" You Are VISITOR ")
        print()
        command = input(" Enter s to display by search and d to display all ")
        if (command == 's'):
            search_type = input(
                "Enter search type 's-site' to search by site or 'view-site' to see location of a site ")
            if (search_type == 's-site'):
                site = input(" Enter the site to display ")
                h.display_site(site)
            elif (search_type == 'view-site'):
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
            break


