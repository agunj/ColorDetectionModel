-- Create the table for the colors (without the type column)
CREATE TABLE broad_colors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    color_name TEXT NOT NULL,
    min_h INTEGER DEFAULT -1,
    max_h INTEGER DEFAULT -1,
    min_s INTEGER DEFAULT -1,
    max_s INTEGER DEFAULT -1,
    min_v INTEGER DEFAULT -1,
    max_v INTEGER DEFAULT -1
);

INSERT INTO broad_colors (color_name, min_h, max_h, min_s, max_s, min_v, max_v)
VALUES
    -- Saturation based colors:
    ('Pink', 300, 350, 20,49, 10, 89),
    ('Gold-Brown', 35, 60, 10, 35, 10, 60),
    ('Orange-Brown', 15, 35, 20, 50, 10, 89),
    ('Red-Brown', 350, 360, 20,49, 10, 89),
    ('Red-Brown', 0, 15, 20,49, 10, 89),
    ('Beige', 0, 60, 8, 20, 85, 89),
    
    --B&W
    ('Black', 0, 360, 0, 100, 0, 10),
    ('White', 0, 360, 0, 5, 50, 100),

    --Hue Based
    ('Red', 0, 15, 5, 100, 10, 89),
    ('Red-Orange', 15, 30, 5, 100, 10, 89),

    ('Orange', 30, 35, 50, 100, 10, 89),
    ('Yellow-Orange', 35, 55, 35, 100, 10, 89),
    ('Yellow', 55, 60, 35, 100, 50, 89),
    ('Yellow-Green', 60, 90, 5, 100, 10, 89),
    ('Green', 90, 120, 5, 100, 10, 89),

    ('Cold Green', 120, 150,5, 100, 10, 89),
    ('Cyan-Green', 150, 165,5, 100, 10, 89),
    ('Cyan', 165, 180,5, 100, 10, 89),

    ('Blue', 180, 240 ,5, 100, 10, 89),
    ('Blue-Violet', 240, 260, 5, 100, 10, 89),
    
    ('Violet', 260, 270, 5, 100, 10, 89),
    ('Violet-Magenta', 270, 285, 5, 100, 10, 89),
    ('Magenta', 285, 300, 5, 100, 10, 89),
    ('Magenta-Red', 300, 350, 5, 100, 10, 89),

    ('Red', 350, 360, 5, 100, 10, 89);

