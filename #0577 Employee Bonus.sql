SELECT 
    employee.name, 
    eonus.bonus
FROM 
    employee
    LEFT JOIN bonus ON employee.empId = bonus.empId
WHERE 
    bonus.bonus IS NULL OR bonus.bonus < 1000;
    