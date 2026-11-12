/*
Enter your query here.
*/
SELECT CITY,  LENGTH(CITY)  
FROM STATION 
ORDER BY LENGTH(CITY) ASC, CITY ASC
LIMIT 1;

SELECT CITY,  LENGTH(CITY)  
FROM STATION 
ORDER BY LENGTH(CITY) DESC, CITY DESC
LIMIT 1;


-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna