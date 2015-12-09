from lib.actions import BaseAction


class GetNonStructuredAction(BaseAction):
    def run(self, schema, qualifier, fields, offset, limit):
        response = self.query(schema, qualifier, fields, offset, limit)  # pylint: disable=no-member
        return response
