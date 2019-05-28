Typically, the check - if for a user belongs to a group - is expected to occur more
frequently than the operation of adding a user to a group. Therefore, I choose
to add higher time complexity to the function `add_group` method. The
`add_group` method recursively loops through all the groups to find their
users, and it populates a hash maps that keeps track of all groups that a user
has. 

The worst case time complexity of `add_group` method is O(n*g), where: 
n - number of users
g - number of groups 


The worst case time complexity of `add_user` method is O(n), and average case
complexity is O(1) due to the use of hashmap data structure - USERS internally.

The main function `is_user_in_group` uses the hashmap USERS to determine if
user belong to a group or its sub-groups. The worst case time time complexity
of this function is same as Python dictionary - O(n)
