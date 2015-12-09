from lib.actions import BaseAction


class UpdateAction(BaseAction):
    def run(self, schema, entry_values, entry_id):
        response = self.client.update(schema, entry_values, entry_id)  # pylint: disable=no-member
        return response
