from lib.actions import BaseAction


class GetAction(BaseAction):
    def run(self, schema, entry_id, fields):
        response = self.client.get(schema, entry_id, fields)  # pylint: disable=no-member
        return response
