class File:
    projectDir = '/home/ss/Projects/inventory/inventories/'
    fileExcludes = ['[staging:children]\n', '[production:children]\n', '[preview:children]\n', '[testing:children]\n', '[elk:children]\n', '[current:children]\n']
    def _init_(self, project, inventory):
        # sets attribute values
        self.project = project
        self.inventory = inventory
        self.srvName = ''
        self.srvRoles = []
        self.addSrvs = []
        self.addRoles = []
        fileReader(project, inventory)
        return self.srvName, self.srvRoles, self.addSrvs, self.addRoles, self.project   

    def fileReader(project, inventory):
        # read provided file and save content
        invFile = open(projectDir + project + '/' + inventory, 'r')
        lines = fp.readlines()
        self.srvName = lines[1]
        for line in lines:
            if lines[0] in fileExcludes:
                fp.close()
            # append file output to arrays
            if lines[1] == srvName:
                self.srvRoles.append(lines[0])         
            else:
                self.addRoles.append(lines[0])
                self.addSrvs.append(lines[1])
            # remove read lines
            if len(lines) > 2:
                del lines[2]   
            else:
                del lines[1]
                del lines[0]       
        fp.close()
        self.project = project + '-' + inventory
        return self.srvName, self.srvRoles, self.addSrvs, self.addRoles, self.project 

    def isFileValid(project, inventory):
        # check wether file is empty or not
        invFile = open(projectDir + project + '/' + inventory, 'r')
        lines = fp.readlines()
        if len(lines[1]) > 1:
            return True
        else:
            return False
        return