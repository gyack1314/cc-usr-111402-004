"""关系完整性和已有候选目录发布的读取。"""
from .relations import validate
from .table import Table

def unique_rows(rows,columns):
    seen=set()
    for row in rows:
        key=tuple(row[c] for c in columns)
        if any(v is None for v in key):raise ValueError('必选唯一键含null')
        if key in seen:raise ValueError('唯一键冲突')
        seen.add(key)
    return True

def inspect(data,storage,root):
    validate(data['source']);validate(data['target']);unique_rows(data['target'],data['unique'])
    table=Table(storage,root/'table');head=table.stage(data['target'],{'shipment':'str','mass':'int','active':'bool'})
    table.publish('facts',None,head)
    return {'target_snapshot':head,'target_rows':table.snapshot(head),'source_rows':len(data['source']),'unique':data['unique']}
