
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [         
         {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": "Jackson",
                "age": "33 Years old",
                "Lucky Numbers": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name":  "Jackson",
                "age": "35 Years old",
                "Lucky Numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name":  "Jackson",
                "age": "5 Years old",
                "Lucky Numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return --> para agregar en Python --> <lista>.append(<elemento>)
        self._members.append(member)
        return None

    def delete_member(self, id):
        # fill this method and update the return:
        # for i, item in enumerate(self._members, start= 0):
        #     if self._members[i]["id"] == id:
        #         self._members.pop(i)
        #         return None
        status = False
        for i, item in enumerate(self._members, start=0):
            if item["id"] == id:
                self._members.pop(i)
                status = True

    def get_member(self, id):
        # fill this method and update the return --> con loops 
        for x in self._members:
            if x['id'] == int(id):
                return x
        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
