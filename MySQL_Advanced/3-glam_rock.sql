-- Liste des groupes de Glam rock classés par longévité

-- Récupère les groupes de Glam rock et calcule leur longévité
SELECT band_name, 
       (IFNULL(split, YEAR(CURDATE())) - formed) AS lifespan -- Calcule la longévité en années
FROM metal_bands -- Table des groupes de métal
WHERE style LIKE '%Glam rock%' -- Filtre pour le style Glam rock
ORDER BY lifespan DESC; -- Trie par longévité, du plus grand au plus petit
