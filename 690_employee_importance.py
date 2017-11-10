"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        d={}
        for e in employees:
            d[e.id]={'val':e.importance,'subs':e.subordinates}
        
        q_subs = d[id]['subs']
        total_val = d[id]['val']
        
        while len(q_subs) > 0:
            s = q_subs.pop()
            total_val += d[s]['val']
            for sub in d[s]['subs']:
                q_subs.append(sub)
        
        return total_val
