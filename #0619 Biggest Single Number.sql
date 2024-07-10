SELECT 
    CASE 
        WHEN COUNT(*) = 0 THEN NULL
        ELSE MAX(num)
    END AS num
FROM (
    SELECT 
        num
    FROM 
        mynumbers
    GROUP BY 
        num
    HAVING 
        COUNT(*) = 1
) AS unique_nums;
