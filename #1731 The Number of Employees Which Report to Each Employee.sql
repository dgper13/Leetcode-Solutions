SELECT 
    m.employee_id,
    m.name,
    COUNT(*) AS reports_count,
    ROUND(AVG(e.age), 0) AS average_age
FROM employees AS m
INNER JOIN employees AS e ON m.employee_id = e.reports_to
GROUP BY m.employee_id, m.name
ORDER BY m.employee_id;