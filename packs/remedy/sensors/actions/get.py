from lib.actions import BaseAction

class GetAction(BaseAction):
    def run(self, schema, entry_id, fields):
        response = self.get(schema, entry_id, fields)  # pylint: disable=no-member
        return response
