-- updating multiple tables for one action from your application
-- can generate issue: network disconnection, crash etc... to keey your
-- data in shape, let MySQL do it for you!
-- This script creates a trigger that decreases the quantity of an item after
-- adding a new order
DELIMITER $$

CREATE TRIGGER after_order_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$

DELIMITER ;
