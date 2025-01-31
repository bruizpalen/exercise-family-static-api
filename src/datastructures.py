
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
            "first_name": 'John',
            "last_name": last_name,
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        },
                    {
            "id": self._generateId(),
            "first_name": 'Jane',
            "last_name": last_name,
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        },
                    {
            "id": self._generateId(),
            "first_name": 'Jimmy',
            "last_name": last_name,
            "age": 5,
            "lucky_numbers": [1]
        },


        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
            member_id = self._generateId()
            member["id"] = member_id
            member["last_name"] = self.last_name
            self._members.append(member)
            return member

    def update_member(self, id, updated_member):
        for member in self._members:
            if member["id"] == id:
                member["last_name"] = self.last_name
                member["first_name"] = updated_member.get("first_name", member["first_name"])
                member["age"] = updated_member.get("age", member["age"])
                member["lucky_numbers"] = updated_member.get("lucky_numbers", member["lucky_numbers"])
                return member
        return ('There is not that member in the family')

    def delete_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return ('Member successfully removed')
        return ('There is not that member in the family')
        

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            
            if member["id"] == id:
                return member["first_name"]
        return print('There is not that member in the family')

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        for member in self._members:
            print(member["id"])
        return self._members
