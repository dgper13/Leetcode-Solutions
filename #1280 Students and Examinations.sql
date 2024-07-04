SELECT
    stu.student_id,
    stu.student_name,
    sub.subject_name,
    COUNT(exam.subject_name) AS attended_exams
FROM
    students AS stu
    INNER JOIN subjects AS sub
    LEFT JOIN examinations AS exam ON stu.student_id = exam.student_id AND exam.subject_name = sub.subject_name
GROUP BY
    stu.student_id,
    stu.student_name,
    sub.subject_name
ORDER BY
    stu.student_id,
    sub.subject_name;
    