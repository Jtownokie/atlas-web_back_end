-- Updates quantities in store when orders are made

DELIMITER $$

CREATE TRIGGER after_insert_orders
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    DECLARE item_quantity INT;
    SELECT quantity INTO item_quantity
    FROM items
    WHERE name = NEW.item_name;

    UPDATE items
    SET quantity = item_quantity - NEW.number
    WHERE name = NEW.item_name;
END $$

DELIMITER ;
