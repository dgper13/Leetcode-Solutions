SELECT 
    End.machine_id, 
    ROUND(AVG(End.timestamp - Start.timestamp), 3) AS processing_time 
FROM 
    Activity AS End
    INNER JOIN Activity AS Start ON End.machine_id = Start.machine_id
WHERE 
    End.activity_type = 'end' 
    AND Start.activity_type = 'start'
    AND End.process_id = Start.process_id
GROUP BY 
    End.machine_id;