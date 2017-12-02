# importing modules
import graphviz as gv
import functools
import re
# importing files
import servertype
import functions
import Server
import File

# variables
digraph = functools.partial(gv.Digraph, format='svg') 
projectDir = '/home/ss/Projects/inventory/inventories/'

projects = functions.projectRetriever(projectDir)

for project in projects:
    inventories = functions.invRetriever(projectDir, project)
    for inventory in inventories:
        if functions.fileIsValid(projectDir, project, inventory):    
            obj = File(project, inventory)
            srvName = obj.getSrvName()
            srvRoles = obj.getSrvRoles()
            addSrvs = obj.getAddSrvs()
            addRoles = obj.getAddRoles()
            pjt = obj.getProject()
 
g1 = functions.add_edges(
    functions.add_nodes(digraph(),
        Server.drawServers
    ),    
    Server.drawConnections
)

g1 = functions.apply_styles(g1, servertype.web)
g1.render('img/g2')




# g1 = functions.add_edges(
#     functions.add_nodes(graph(), [
#         ('1', {'label': functions.read_inventory('xoras','inventory')}),
#         ('2', {'label': functions.read_inventory('tekenjetuin','staging')}),
#         ('3', {'label': functions.read_inventory('tekenjetuin','production')}),
#         ('4', {'label': functions.read_inventory('pas-reform','staging')}),
#         ('5', {'label': functions.read_inventory('pas-reform','preview')}),
#         ('6', {'label': functions.read_inventory('biblio','inventory')}),
#         ('7', {'label': functions.read_inventory('jambo','testing')}),
#         ('8', {'label': functions.read_inventory('yetu','production')}),
#         ('9', {'label': functions.read_inventory('planviewer','test')}),
#     ]),
#     [
#         # (('1', '2'), {'label': 'Label 1'}),
#         # (('1', '3'), {'label': 'Label 2'}),
#         # ('2', '3')
#     ] 
# )

# g2 = functions.add_edges(
#     add_nodes(digraph(), [
#         ('5', {'label': 'chafu\n-psql\n(tjt-production)'})
#     ]),
#     [
#         (('4', '5'), {'label': 'Edge 3'}),
#         ('4', '5')
#     ]
# )

# g3 = functions.add_edges(
#     add_nodes(digraph(), [
#         ('7', {'label': 'Helix'}),
#         ('8', {'label': 'Ises'}),
#         ('9', {'label': 'Organ'})
#     ]),
#     [
#         (('7', '8'), {'label': 'Edge 5'}),
#         (('7', '9'), {'label': 'Edge 6'}),
#         ('8', '9')
#     ]
# )
#g3 = functions.apply_styles(g3, servertype.database)
#g1.subgraph(g3)
#g1.edge('2', '8', color='red', weight='2')

# g2 = functions.apply_styles(g2, servertype.web)
# g1.subgraph(g2)
# g1.edge('2', '4', color='red', weight='2')



