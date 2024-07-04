SELECT
    r.contest_id,
    ROUND((COUNT(r.user_id) / (SELECT COUNT(*) FROM users)) * 100, 2) AS percentage
FROM
    register AS r
LEFT JOIN
    users AS u ON r.user_id = u.user_id
GROUP BY
    r.contest_id
ORDER BY
    percentage DESC,
    r.contest_id ASC;
    