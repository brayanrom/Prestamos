class temporal:
    
    def removeObject(self,indice=None,name=None):
        if(indice!=None):
            self.list.pop(indice)
            return True
        elif(name!=None):
            c=0
            for element in self.list:
                if(element.name==name):
                    self.list.pop(c)
                    return True
                c+=1
        return False

    def updateObject(self,indice,persona):
        self.list[indice]=persona

    def get(self):
        return self.name,self.dato1
