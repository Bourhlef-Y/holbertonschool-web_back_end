-- Déclencheur pour diminuer la quantité d'un article après l'ajout d'une nouvelle commande

DELIMITER //

CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number -- Diminue la quantité de l'article
    WHERE name = NEW.item_name; -- Correspond à l'article commandé
END;
//

DELIMITER ;
