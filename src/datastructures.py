from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {"id": 3443, "first_name": "Tommy", "last_name": self.last_name, "age": 5, "lucky_numbers": [1]},
            {"id": 5678, "first_name": "John", "last_name": self.last_name, "age": 33, "lucky_numbers": [7, 13, 22]},
            {"id": 9101, "first_name": "Jane", "last_name": self.last_name, "age": 35, "lucky_numbers": [10, 14, 3]}
        ]

    def _generateId(self):
        return randint(1000, 9999)  # Generate a 4-digit random ID

    def add_member(self, member):
        if "age" not in member or not isinstance(member["age"], int) or member["age"] <= 0:
            return False  # Age must be an integer > 0

        if "lucky_numbers" in member:
            if not all(isinstance(num, int) for num in member["lucky_numbers"]):
                return False  # Ensure lucky numbers are integers

        member["id"] = member.get("id", self._generateId())  # Keep ID if given, otherwise generate
        member["last_name"] = self.last_name  # Always set last name as "Jackson"
        member["lucky_numbers"] = list(member.get("lucky_numbers", []))  # Ensure lucky_numbers is a list

        self._members.append(member)
        return True

    def get_member(self, member_id):
        for member in self._members:
            if member["id"] == member_id:
                return {
                    "first_name": member["first_name"],
                    "id": member["id"],
                    "age": member["age"],
                    "lucky_numbers": member["lucky_numbers"]
                }
        return None

    def delete_member(self, member_id):
        for i, member in enumerate(self._members):
            if member["id"] == member_id:
                del self._members[i]
                return True
        return False

    def get_all_members(self):
        return self._members
