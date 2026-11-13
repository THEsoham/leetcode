/*
Enter your query here.
*/
SELECT NAME
FROM STUDENTS AS S
WHERE S.MARKS > 75
ORDER BY RIGHT(S.NAME, 3), S.ID ASC;


-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna