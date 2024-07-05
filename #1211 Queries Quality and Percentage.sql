SELECT
    query_name,
    ROUND(AVG(rating / position), 2) AS quality,
    ROUND((COUNT(CASE WHEN rating < 3 THEN 1 END) * 100.0 / COUNT(*)), 2) AS poor_query_percentage
FROM
    queries AS q
WHERE
    q.query_name IS NOT NULL
GROUP BY
    q.query_name;
    