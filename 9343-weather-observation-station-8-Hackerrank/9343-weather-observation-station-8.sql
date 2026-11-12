/*
Enter your query here.
*/

SELECT DISTINCT CITY
FROM STATION 
WHERE (
        CITY LIKE "A%"
    OR CITY LIKE "E%"
    OR CITY LIKE "I%"
    OR CITY LIKE "O%"
    OR CITY LIKE "U%"
  
) AND
(
    CITY LIKE "%A"
    OR CITY LIKE "%E"
    OR CITY LIKE "%I"
    OR CITY LIKE "%O"
    OR CITY LIKE "%U"

)


-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna