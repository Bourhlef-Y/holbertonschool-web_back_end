-- Procédure pour ajouter une nouvelle correction pour un étudiant

DELIMITER //

CREATE PROCEDURE AddBonus(
    IN user_id INT,          -- ID de l'utilisateur
    IN project_name VARCHAR(255), -- Nom du projet
    IN score INT            -- Score de la correction
)
BEGIN
    DECLARE project_id INT;

    -- Vérifie si le projet existe déjà
    SELECT id INTO project_id
    FROM projects
    WHERE name = project_name;

    -- Si le projet n'existe pas, le créer
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID(); -- Récupère l'ID du nouveau projet
    END IF;

    -- Ajoute la correction
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END;
//

DELIMITER ; 