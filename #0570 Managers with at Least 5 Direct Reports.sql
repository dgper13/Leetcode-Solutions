SELECT manager.name
FROM employee
INNER JOIN employee AS manager ON manager.id = employee.managerId
GROUP BY manager.id
HAVING COUNT(employee.id) >= 5;
