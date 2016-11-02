from lib.actions import BaseAction


class GetListAction(BaseAction):
    def run(self, schema, qualifier, fields, offset, limit):
        # pylint: disable=no-member
        response = self.client.query(schema, qualifier, fields, offset, limit)
        # pylint: enable=no-member
        return response
