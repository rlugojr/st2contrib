from lib.actions import BaseAction


class InserTesttAction(BaseAction):
    def run(self, description):
        entry_values = ('Short Description', description)
        response = self.client.create('TESTE_RENAN', entry_values)  # pylint: disable=no-member
        return response
