from lib.actions import BaseAction


class InsertAction(BaseAction):
    def run(self, schema, entry_values):
        response = self.create(schema, entry_values)  # pylint: disable=no-member
        return response
