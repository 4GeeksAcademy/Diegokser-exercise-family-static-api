
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

        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        family_member = {
                "id": self._generateId(),
                "first_name": member.get("first_name"),
                "last_name" : self.last_name,
                "age" : member.get("age"),
                "lucky_number" : member.get("lucky_number")
        }
        self._members.append(family_member)

    def delete_member(self, id):
        for member in self._members:
            if member.get('id') == id:
                self._members.remove(member)

    def get_member(self, id):
         for member in self._members:
            if member.get("id") == id:
                return member

    def get_all_members(self):
        return self._members
