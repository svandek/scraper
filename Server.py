import itertools
counter = itertools.count()

serverList = []
projectList = []
rolesList = []
drawServers = []
drawConnections = []

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
        self.rolesChecker(self.srvRoles)
        self.addsChecker(self.addSrvs, self.addRoles)
        self.projectsChecker(self.projects)
        
        # appends values to the draw arrays
        self.serverDrawer(self.srvName, self.srvNr, self.srvRoles, project)
        for add in addSrvs:
            indexPos = addSrvs.index(add)
            if add in serverList:
                srvPos = serverList.index(add)
                self.connectionDrawer(self.srvNr, srvPos, addRoles[indexPos])
            else:
                newInstance = Server(add, self.addRoles[indexPos], '', '', project)
                self.connectionDrawer(self.srvNr, newInstance.srvNr, addRoles[indexPos])
        return     

    def serverDrawer(self, srvName, srvNr, srvRoles, projects):
        # appends the server to the drawServers array
        projectString = ''
        roleString = ''
        for project in projects:
            projectString += project
        for role in srvRoles:
            roleString += role       
        drawServers.append((str(srvNr), {'label': srvName + '\n' + projectString + '\n' + roleString}))
        return drawServers

    def connectionDrawer(self, origin, destination, role):
        # appends all connections to be drawn to the drawConnections array
        drawConnections.append(((str(origin), str(destination)), {'label': role}))
        print 'SERVER CONNECTIONS: ', drawConnections
        return drawConnections

    def rolesChecker(self, srvRoles):
        # removes duplicate roles
        roles = []
        for role in srvRoles:
            if not role in roles:
                roles.append(role)
        self.srvRoles = roles
        return self.srvRoles

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
    def serverUpdater(srvName, srvRoles, project):
        # appends additional values to attributes and removes duplicate values
        srvIndex = serverList.index(srvName)
        old_projects = projectList[srvIndex]
        old_roles = rolesList[srvIndex]
        projectString = ''
        oldRolesString = ''
        newRolesString = ''
        roleString = ''
        for pjt in old_projects:
            projectString += pjt
        for role in old_roles:
            oldRolesString += role    
        for role in srvRoles:
            newRolesString += role
        roleString = oldRolesString = newRolesString    
        projectString += project
        print 'ROLESTRING: ',roleString
        print 'PROJECTSTRING',projectString 
        drawServers[srvIndex] = (str(srvIndex), {'label': srvName + '\n' + projectString + '\n' + roleString})
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
    def serverExists(srvName):
        if srvName in serverList: 
            print 'ERROR: SERVER EXISTS'
            return True
        else:
            return False
