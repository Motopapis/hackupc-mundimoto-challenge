class ApiMode():
    __instance = None
    __production = "development"

    @staticmethod
    def get_instance():
        """ Access Instance """
        if ApiMode.__instance == None:
            ApiMode()
        return ApiMode.__instance
    
    def __init__(self):
      """ Virtually private constructor. """
      if ApiMode.__instance != None:
         raise Exception("Already initialised")
      else:
         ApiMode.__instance = self
    
    def get_production(self):
        """ Get the production mode """
        return self.__production
    
    def set_production(self, production):
        """ Set the production mode """
        self.__production = production