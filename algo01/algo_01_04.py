def SynchronizingTables(N, ids, salary):
    result = []
    map_ids_salary = dict(zip(sorted(ids), sorted(salary)))
    for id in ids:
        result.append(map_ids_salary[id])
    return result
