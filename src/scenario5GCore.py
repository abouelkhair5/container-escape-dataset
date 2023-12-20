import command_line

class Scenario5GCore:

    def __init__(self):
        self._name = '5G Core'
        self._composeTemplate = None

    def getName(self):
        """
        Gets the name of the scenario.
        """
        return self._name

    def init(self, scheduler, experimentSeconds, annotationFile):
        """
        Setup any resources for the scenario.
        Logging is not active.
        """
        # Start the container for unauthorized executing shell on host.
        # Presumes cwd is container-escape-dataset, uses relative path
        self._composeTemplate = '../containers/open5gs-k8s/open5gs'

        #self.execute( 'sudo docker-compose -f ' + self._composeTemplate +  ' build' )
        self.execute('kubectl apply -k open5gs -n open5gs')

        # We have no escape/attack events but need to "annotate" the experiment
        annotationFile.annotateName( self._name )

        print( 'Scenario ' + self.getName() + ': initialized' )

    def start(self):
        """
        May be called multiple times during experiment.
        Logging is active.
        """

    def onEvent(self):
        """
        Event occurred.  Logging is active.
        """


    def stop(self):
        """
        May be called multiple times during experiment.
        Logging is active.
        """

    def destroy(self):
        """
        Tears down the scenario, for example, stop container.
        Logging is not active
        """
        self.execute( 'kubectl delete -k open5gs -n open5gs')

    def execute( self, command ):
        """
        Convenience to call execute and print out results.
        """
        result = command_line.execute( command )
        for line in result:
            print( 'Scenario ' + self._name + ': ' + line)
