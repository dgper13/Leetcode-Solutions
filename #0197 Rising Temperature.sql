SELECT W.id
FROM Weather as W
LEFT JOIN Weather W_prev ON W.recordDate = DATE_ADD(W_prev.recordDate, INTERVAL 1 DAY)
WHERE W.temperature > W_prev.temperature;
