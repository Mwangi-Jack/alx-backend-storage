-- Calculate lifespan, filter by style, and rank by longevity
SELECT
    band_name,
    IFNULL(
        IF(split IS NULL, 2022, split) - formed,
        2022 - formed
    ) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
