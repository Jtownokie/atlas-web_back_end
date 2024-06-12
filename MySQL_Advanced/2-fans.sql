-- Creates a view and selects from to get desired output

CREATE VIEW origin_fan_count AS
SELECT
    origin,
    SUM(nb_fans) AS nb_fans
FROM
    metal_bands
GROUP BY
    origin
ORDER BY
    nb_fans DESC;

SELECT * FROM origin_fan_count;
