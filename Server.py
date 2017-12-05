import itertools
counter = itertools.count()

serverList = []
projectList = []
rolesList = []
drawServers = []
drawConnections = []
connectionRememberer = []

class Server:
    # attributes
    srvName = ''
    srvRoles = []
    addSrvs = []
    addRoles = []
    projects = []
    
    def __init__(self, srvName, srvRoles, addSrvs, addRoles, project):
        # sets attribute values
        self.srvName = srvName
        self.srvNr = next(counter)
        self.srvRoles = srvRoles
        self.addSrvs.append(addSrvs)
        self.addRoles.append(addRoles)
        self.projects.append(project)
        projectList.append(project)
        serverList.append(srvName)
        rolesList.append(srvRoles)
        # removes duplicate values
        Server.rolesChecker(self.srvRoles)
        self.addsChecker(self.addSrvs, self.addRoles)
        self.projectsChecker(self.projects)
        print self.srvNr, self.srvName, self.addSrvs, self.addRoles
        # appends values to the draw arrays
        self.serverDrawer(self.srvName, self.srvNr, self.srvRoles, project)
        for add in addSrvs:
            indexPos = addSrvs.index(add)
            if add in serverList:
                srvPos = serverList.index(add)
                Server.connectionDrawer(self.srvNr, srvPos, addRoles[indexPos], project)
            else:
                newAdd = ['propter.tgsrv.nl\n']
                newRole = ['[backup]\n']
                newInstance = Server(add, addRoles[indexPos], newRole, newAdd, project)
                Server.connectionDrawer(self.srvNr, newInstance.srvNr, addRoles[indexPos], project)
        return     

    @staticmethod
    def serverDrawer(srvName, srvNr, srvRoles, projects):
        # appends the server to the drawServers array
        projectString = ''
        roleString = ''
        for project in projects:
            projectString += project
        for role in srvRoles:
            roleString += role       
        drawServers.append((str(srvNr), {'label': srvName + '\n' + projectString + '\n' + roleString}))
        return drawServers
    
    @staticmethod
    def connectionDrawer(origin, destination, role, project):
        # appends all connections to be drawn to the drawConnections array
        rememberString = str(origin) + '-' + str(destination)            
        if not rememberString in connectionRememberer:
            drawConnections.append(((str(origin), str(destination)), {'label': role + project}))
            connectionRememberer.append(rememberString)
        return drawConnections

    @staticmethod
    def rolesChecker(srvRoles):
        # removes duplicate roles
        roles = []
        for role in srvRoles:
            if not role in roles:
                roles.append(role)
        return roles

    def projectsChecker(self, projects):
        # removes duplicate projects
        pjts = []
        for project in projects:
            if not project in pjts:
                pjts.append(project)
        self.projects = pjts
        return self.projects

    def addsChecker(self, addSrvs, addRoles):
        # removes duplicate additional servers and appends it's roles
        servers = []
        dels = []
        x = 0
        for add in addSrvs:
            if add == '':
                dels.append(x)
            elif not add in servers:
                servers.append(add)
            else:
                for y in range(0, len(servers)):
                    if servers[y] == add:
                        self.addRoles[y] = self.addRoles[y] + self.addRoles[x]
                        dels.append(x)
            x += 1               
        if len(dels) > 0:
            for i in reversed(dels):
                del(self.addRoles[i])
                del(self.addSrvs[i])

        return self.addSrvs, self.addRoles 

    @staticmethod
    def serverUpdater(srvName, srvRoles, addSrvs, addRoles, project):
        # appends additional values to attributes and removes duplicate values
        srvIndex = serverList.index(srvName)
        old_projects = projectList[srvIndex]
        old_roles = rolesList[srvIndex]
        
        for role in old_roles:
            srvRoles.append(role)
        
        new_roles = Server.rolesChecker(srvRoles)
        rolesList[srvIndex] = new_roles
        projectList[srvIndex] = old_projects + project
        projectString = ''
        roleString = ''
        
        for pjt in old_projects:
            projectString += pjt
        for role in new_roles:
            roleString += role       
        
        projectString += project
        drawServers[srvIndex] = (str(srvIndex), {'label': srvName + '\n' + projectString + '\n' + roleString})
      
        for add in addSrvs:
            indexPos = addSrvs.index(add)
            if add in serverList:
                srvPos = serverList.index(add)
                Server.connectionDrawer(srvIndex, srvPos, addRoles[indexPos], project)       
            else:
                newInstance = Server(add, addRoles[indexPos], '', '', project)
                Server.connectionDrawer(srvIndex, newInstance.srvNr, addRoles[indexPos], project)
        return 

    def srvRolesUpdater(self, srvRoles):
        srvRoles.append(srvRoles)
        rolesChecker(srvRoles)
        return self.srvRoles

    def addsUpdater(self, addSrvs, addRoles):
        self.addSrvs.append(addSrvs)
        self.addRoles.append(addRoles)
        rolesChecker(addSrvs, addRoles)
        return self.addSrvs, self.addRoles

    def projectsUpdater(self, project):
        self.projects.append(project)
        projectsChecker(projects)
        return self.projects

    @staticmethod
    def getServers():
        print drawServers
        return drawServers

    @staticmethod
    def getConnections():
        print drawConnections
        return drawConnections

    @staticmethod
    def getSrvID(srvName):
        srvID = serverList.index(srvName)
        return srvID

    @staticmethod
    def serverExists(srvName):
        if srvName in serverList:
            return True
        else:
            return False
