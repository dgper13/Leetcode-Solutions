SELECT
    Stu.student_id,
    Stu.student_name,
    Sub.subject_name,
    COUNT(Exam.subject_name) AS attended_exams
FROM
    Students AS Stu
    INNER JOIN Subjects AS Sub
    LEFT JOIN Examinations AS Exam ON Stu.student_id = Exam.student_id AND Exam.subject_name = Sub.subject_name
GROUP BY
    Stu.student_id,
    Stu.student_name,
    Sub.subject_name
ORDER BY
    Stu.student_id,
    Sub.subject_name;