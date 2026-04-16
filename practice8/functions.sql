-- 1. Function: search contacts by pattern
CREATE OR REPLACE FUNCTION get_contacts_by_pattern(p_pattern TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.name, p.phone
    FROM phonebook p
    WHERE p.name ILIKE '%' || p_pattern || '%'
       OR p.phone ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;


-- 2. Function: paginated query
CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.name, p.phone
    FROM phonebook p
    ORDER BY p.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;