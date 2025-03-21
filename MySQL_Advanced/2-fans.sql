-- Classement des origines des groupes par le nombre de fans

-- Récupère les origines des groupes et le nombre total de fans
SELECT origin, SUM(fans) AS nb_fans -- Somme des fans par origine
FROM metal_bands -- Table des groupes de métal
GROUP BY origin -- Regroupe par origine
ORDER BY nb_fans DESC; -- Trie par nombre de fans, du plus grand au plus petit
