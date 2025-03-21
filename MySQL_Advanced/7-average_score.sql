-- Procédure pour calculer et stocker la moyenne des scores d'un étudiant

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT           -- ID de l'utilisateur
)
BEGIN
    DECLARE avg_score FLOAT;

    -- Calcule la moyenne des scores pour l'utilisateur
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = user_id;

    -- Met à jour la moyenne des scores de l'utilisateur
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END;
//

DELIMITER ; 