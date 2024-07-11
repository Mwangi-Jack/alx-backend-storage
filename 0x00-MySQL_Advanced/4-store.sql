-- updating multiple tables for one action from your application
-- can generate issue: network disconnection, crash etc... to keey your
-- data in shape, let MySQL do it for you!
-- This script creates a trigger that decreases the quantity of an item after
-- adding a new order

CREATE TRIGGER sub_order AFTER INSERT ON items
		FOR EACH ROW SET @number = @number - NEW.quantity;
