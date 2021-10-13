from tools.genericRepository.genericRepo import GenericRepo

class UsersRepo(GenericRepo):
    def __init__(self, session, table):
        GenericRepo.__init__(self, session, table)