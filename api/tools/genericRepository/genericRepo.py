class GenericRepo:
    def __init__(self, session, table):
        self.session = session
        self.table = table

    def commit(self):
        """
        Commit the change session to the DB 
        """
        self.session.commit()
    
    def get_all(self):
        """
        Get All table \n 
        Return: list of rows
        """
        return self.session.query(self.table).all()

    def get_by_id(self, id):
        """
        Get one row by the ID \n 
        Parm: the ID (Primary key) \n
        Return: one row
        """
        return self.session.query(self.table).get(id)
    
    def get_all_filter(self, filter):
        """
        Get elements with a filter \n
        Param: the filter \n
        Return list of rows
        """
        return self.session.query(self.table).filter(filter)
    
    def get_first(self, filter):
        """
        Get the first element with a filter \n 
        Param: the filter \n
        Return: one row
        """
        return self.session.query(self.table).filter(filter).first()

    def count(self):
        """
        Count the all table \n
        Return: an integer
        """
        return self.session.query(self.table).count()

    def count_filter(self, filter):
        """
        Count the rows match with the filter \n
        Param: the filter \n
        Return an integer
        """
        return self.session.query(self.table).filter(filter).count()

    def insert(self, object, commit=True):
        """
        Insert in the table the now object \n
        Param: the new object \n
        \t commit (default `True`) \n
        Return: If commit is True, return the new object with the new ID \n
        \t else return null
        """
        self.session.add(object)
        if commit:
            self.session.commit()
            self.session.refresh(object)
            return object
        return None

    def delete(self, filter, commit=True):
        """
        Delete rows with filter \n
        Param: the filter \n
        \t commit (default `True`) \n
        Return: list if rows delete
        """
        del_ = self.session.query(self.table).filter(filter)
        for row in del_:
            self.session.delete(row)
        if commit:
            self.session.commit()
        return del_
    
    def delete_by_id(self, id, commit=True):
        """
        Delete rows with the ID \n
        Param: ID (Primary key)\n
        \t commit (default `True`) \n
        Return: Object will be deleted
        """
        object = self.get_by_id(id)
        self.session.delete(object)
        if commit:
            self.session.commit()
        return object

    def update(self, update, filter=None, commit=True):
        """
        Update the table with a filter \n
        Param: field to update \n
        \t the filter (can be null) \n
        \t the commit (default `True`) \n
        Return: list of rows update
        """
        if filter is None:
            up = self.session.query(self.table).all()
        else:
            up = self.session.query(self.table).filter(filter)
           
        for row in up:
            for key in update.keys():
                print(update[key])
                setattr(row, key.key, update[key])
            self.session.add(row)
        if commit:
            self.session.commit()
        return up
