-- Déclencheur pour réinitialiser valid_email lorsque l'email a été modifié

DELIMITER //

CREATE TRIGGER reset_valid_email_on_email_change
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN -- Vérifie si l'email a changé
        SET NEW.valid_email = 0; -- Réinitialise valid_email à 0
    END IF;
END;
//

DELIMITER ;
