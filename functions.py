import os

invExcludes = ['group_vars', 'host_vars']
projectExcludes = ['updates', 'base', 'servers', 'planviewer', '.git']     

# Draws a block
def add_nodes(digraph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            digraph.node(n[0], **n[1])
        else:
            digraph.node(n)
    return digraph

# Draws a line
def add_edges(digraph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            digraph.edge(*e[0], **e[1])
        else:
            digraph.edge(*e)
    return digraph

# Apply styles from the servertype.py to a node
def apply_styles(digraph, srv):
    digraph.graph_attr.update(
        ('digraph' in srv and srv['digraph']) or {}
    )
    digraph.node_attr.update(
        ('nodes' in srv and srv['nodes']) or {}
    )
    digraph.edge_attr.update(
        ('edges' in srv and srv['edges']) or {}
    )
    return digraph

# Retrieves all projects in specified path
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

def fileIsValid(projectDir, project, inventory):
        # check wether file is empty or not
        invFile = open(projectDir + '/' + project + '/' + inventory, 'r')
        lines = invFile.readlines()
        if len(lines[1]) > 1:
            return True
        else:
            return False
        return