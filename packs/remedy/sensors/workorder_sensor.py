from st2reactor.sensor.base import PollingSensor


class WorkOrderSensor(PollingSensor):
    """
    * self._sensor_service
        - provides utilities like
            get_logger() for writing to logs.
            dispatch() for dispatching triggers into the system.
    * self._config
        - contains configuration that was specified as
          config.yaml in the pack.
    * self._poll_interval
        - indicates the interval between two successive poll() calls.
    """

    def setup(self):
        # Setup stuff goes here. For example, you might establish connections
        # to external system once and reuse it. This is called only once by the system.
        pass

    def poll(self):
        # pylint: disable=no-member
        entries = self.client.query(schema='TESTE_RENAN', qualifier='1=1',
                                    fields=['Request ID', 'Short Description', 'Status'],
                                    offset=0, limit=5)
        # pylint: enable=no-member

        for entry_id, entry_values in entries:

            # self.client.update()
            print('Entry ID: {}'.format(entry_id))
            print('-' * 80)
            for field, value in entry_values.items():
                print('{}: {}'.format(field, value))
        print()

        pass

    def cleanup(self):
        # This is called when the st2 system goes down. You can perform cleanup operations like
        # closing the connections to external system here.
        pass

    def add_trigger(self, trigger):
        # This method is called when trigger is created
        pass

    def update_trigger(self, trigger):
        # This method is called when trigger is updated
        pass

    def remove_trigger(self, trigger):
        # This method is called when trigger is deleted
        pass
