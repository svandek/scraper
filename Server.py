# initials
srvNr = 0
# globals
serverList = []
projectList = []
drawServers = []
drawConnections = []

class Server:
    # attributes
    srvName = ''
    srvRoles = []
    addSrvs = []
    addRoles = []
    projects = []

    def _init_(self, srvName, srvRoles, addSrvs, addRoles, project):
        # sets attribute values
        self.srvName = srvName
        self.srvNr += 1
        self.srvRoles.append(srvRoles)
        self.addSrvs.append(addSrvs)
        self.addRoles.append(addRoles)
        self.projects.append(project)

        projectList.append(project)
        serverList.append(srvName)

        # removes duplicate values
        rolesChecker(srvRoles)
        addsChecker(addSrvs, addRoles)
        projectsChecker(projects)
        
        # appends values to the draw arrays
        serverDrawer(srvName, srvNr, srvRoles, projects)
        for add in addSrvs:
            if add in serverList:
                srvPos = serverList.index(add)
                connectionDrawer(srvNr, srvPos, addRoles)
            else:
                indexPos = addSrvs.index(add)
                newInstance = Server(add, addRoles[indexPos], '', '', project)
                connectionDrawer(srvNr, newInstance.srvNr, addRoles[indexPos])
        return     

    def serverDrawer(self, srvName, srvNr, srvRoles, projects):
        # appends the server to the drawServers array
        self.drawServers.append((str(srvNr), {'label': srvName + '\n' + projects + '\n' + srvRoles}))
        return self.drawServers

    def connectionDrawer(self, origin, destination, role):
        # appends all connections to be drawn to the drawConnections array
        self.drawConnections.append(((str(origin), str(destination)), {'label': role}))
        return self.drawConnections

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

    def serverUpdater(self, srvRoles, addSrvs, addRoles, project):
        # appends additional values to attributes and removes duplicate values
        srvRolesUpdater(srvRoles)
        addUpdater(addSrvs, addRoles)
        projectsUpdater(project)
        return self.srvRoles, self.addSrvs, self.addRoles, self.projects

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