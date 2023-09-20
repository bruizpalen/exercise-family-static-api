
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
        #     {
        #     "id": self._generateId(),
        #     "first_name": "John",
        #     "last_name": last_name
        # }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        member_id = self._generateId()
        self._members.append({"id": member_id, "name": member})
        pass

    def update_member(self, id, updated_member):
        for member in self._members:
            if member["id"] == id:
                member.update(updated_member)
                return print('Member successfully removed')
        return print('There is not that member in the family')

    def delete_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return print('Member successfully removed')
        return print('There is not that member in the family')
        

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                return member["name"]
        return print('There is not that member in the family')

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
