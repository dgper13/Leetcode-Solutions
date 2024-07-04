SELECT 
    e.machine_id, 
    ROUND(AVG(e.timestamp - s.timestamp), 3) AS processing_time 
FROM 
    activity AS e
    INNER JOIN activity AS s ON e.machine_id = s.machine_id
WHERE 
    e.activity_type = 'end' 
    AND s.activity_type = 'start'
    AND e.process_id = s.process_id
GROUP BY 
    e.machine_id;
    