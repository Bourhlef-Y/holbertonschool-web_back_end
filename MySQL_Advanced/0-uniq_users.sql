-- Création d'une table 'users' avec des attributs uniques et non nuls

-- Vérifie si la table 'users' existe déjà
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, -- Identifiant unique de l'utilisateur
    email VARCHAR(255) NOT NULL UNIQUE, -- Adresse email unique
    name VARCHAR(255) -- Nom de l'utilisateur
);
