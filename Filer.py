import os
invExcludes = ['group_vars', 'host_vars']
projectExcludes = ['updates', 'base', 'servers', 'logs', 'planviewer', '.git']     

class Filer:
    projectDir = '/home/sander/Projects/ansible/inventory/inventories/'
    fileExcludes = ['[prometheus-exporters]\n','[staging:children]\n', '[production:children]\n', '[preview:children]\n', '[testing:children]\n', '[elk:children]\n', '[current:children]\n']
    
    def __init__(self, project, inventory):
        # sets attribute values
        self.project = project
        self.inventory = inventory
        self.srvName = ''
        self.srvRoles = []
        self.addSrvs = []
        self.addRoles = []
        self.fileReader(project, inventory)
          
    def fileReader(self, project, inventory):
        # read provided file and save content
        invFile = open(self.projectDir + project + '/' + inventory, 'r')
        lines = invFile.readlines()
        self.srvName = lines[1]
        for line in lines:
            if lines[0] in self.fileExcludes:
                invFile.close()
            # append file output to arrays
            if lines[1] == self.srvName:
                self.srvRoles.append(lines[0])         
            else:
                self.addRoles.append(lines[0])
                self.addSrvs.append(lines[1])
            # remove read lines
            if len(lines) > 2:
                del lines[2]   
            del lines[1]
            del lines[0]       
        invFile.close()
        return 

    @staticmethod
    def isFileValid(projectDir, project, inventory):
        # check wether file is empty or not
        invFile = open(projectDir + project + '/' + inventory, 'r')
        lines = invFile.readlines()
        if len(lines[1]) > 1:
            return True
        else:
            return False
        return lines

    # Retrieves all projects in specified path
    @staticmethod
    def projectRetriever(projectDir):
        projects = os.listdir(projectDir)
        deletes = []
        for project in projects:
            if project in projectExcludes:
                deletes.append(project)
        for item in reversed(deletes):
            del projects[projects.index(item)]
        # print projects
        return projects

    # Retrieves all inventories of provided project
    @staticmethod
    def invRetriever(projectDir, project):
        inventories = os.listdir(projectDir + project)
        deletes = []
        for inventory in inventories:
            if inventory in invExcludes:
                deletes.append(inventory)
        for item in reversed(deletes):        
            del inventories[inventories.index(item)]
        # print invs    
        return inventories
    
    def getSrvName(self):
        return self.srvName

    def getSrvRoles(self):
        return self.srvRoles

    def getAddSrvs(self):
        return self.addSrvs

    def getAddRoles(self):
        return self.addRoles

    def getProject(self):
        projectName = self.project + '-' + self.inventory 
        # print 'PROJECT: ',projectName
        return projectName   
