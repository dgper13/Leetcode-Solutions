SELECT employee_id, department_id
FROM employee
WHERE employee_id IN (
    SELECT employee_id
    FROM employee
    GROUP BY employee_id
    HAVING primary_flag = 'Y' OR COUNT(*) = 1
);
