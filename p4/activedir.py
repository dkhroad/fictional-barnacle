import pdb
USERS = {}

class User(object):
    def __init__(self,_name,_group = None ):
        self.name = _name
        self.groups = set()
        if _group:
            self.add_group(_group)


    def add_group(self,group):
        self.groups.add(group.name)

    def is_user_in_group(self,group):
        return group.name in self.groups

class Group(object):
    def __init__(self,_name):
        self.name = _name
        self.groups = list()
        self.users = list()

   
    def get_all_users(self):
        all_users = list()
        
        def _all_users(group):
            for grp in group.groups:
                _all_users(grp) # O(ngroups * nusers)
                for u in grp.users:
                    all_users.append(u)

            for user in group.users:
                all_users.append(user)

        _all_users(self)
        return all_users


    def add_group(self,group):

        self.groups.append(group) # o(1)
        for user in self.get_all_users(): # o(g*n)
            user.add_group(self) # o(g)

    def add_user(self,user): # o(n)
        u = User(user,self)
        USERS[user]=u
        self.users.append(u) 
        

    def get_groups(self):
        return self.groups

    def get_name(self):
        return self.name
        

        



def is_user_in_group(user,group):
    """
    Return True if user is in the group, False otherwise

    Args:
        user(str): user name/id
        group(class:group): group to check user membership against
    """
    try:
        u = USERS[user] # O(nusers)
        return u.is_user_in_group(group) # O(ngroups) + O(nusers)
    except KeyError:
        return False



