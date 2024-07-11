-- Context: Calculating/Computing something is always power intensive... better to distribute the load
-- Script that ranks country origins of bands orderd by the number of (non-unique) fans

SELECT origin, SUM(fans) AS nb_fans FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;
