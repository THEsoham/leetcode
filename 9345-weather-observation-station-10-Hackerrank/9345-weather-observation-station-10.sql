/*
Enter your query here.
*/
SELECT DISTINCT CITY
FROM STATION
WHERE CITY NOT LIKE "%A"
    AND CITY NOT LIKE "%E"
    AND CITY NOT LIKE "%I"
    AND CITY  NOT LIKE "%O"
    AND CITY NOT LIKE "%U";


-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna