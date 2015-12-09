from lib.actions import BaseAction


class DeleteAction(BaseAction):
    def run(self, schema, entry_id):
        response = self.delete(schema, entry_id)  # pylint: disable=no-member
        return response
