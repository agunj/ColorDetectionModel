-- Create a table for colors
CREATE TABLE IF NOT EXISTS Colors (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Auto-incrementing ID
    name TEXT NOT NULL,                   -- Name of the color
    r INTEGER NOT NULL,                   -- Red component (0-255)
    g INTEGER NOT NULL,                   -- Green component (0-255)
    b INTEGER NOT NULL                    -- Blue component (0-255)
);

-- Insert predefined colors
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('white', 255, 255, 255);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('maroon', 128, 0, 0);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('dark red', 139, 0, 0);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('brown', 165, 42, 42);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('firebrick', 178, 34, 34);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('crimson', 220, 20, 60);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('red', 255, 0, 0);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('tomato', 255, 99, 71);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('coral', 255, 127, 80);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('indian red', 205, 92, 92);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('light coral', 240, 128, 128);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('dark salmon', 233, 150, 122);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('salmon', 250, 128, 114);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('light salmon', 255, 160, 122);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('orange red', 255, 69, 0);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('dark orange', 255, 140, 0);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('orange', 255, 165, 0);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('gold', 255, 215, 0);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('dark golden rod', 184, 134, 11);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('golden rod', 218, 165, 32);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('pale golden rod', 238, 232, 170);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('dark khaki', 189, 183, 107);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('khaki', 240, 230, 140);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('olive', 128, 128, 0);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('yellow', 255, 255, 0);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('yellow green', 154, 205, 50);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('dark olive green', 85, 107, 47);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('olive drab', 107, 142, 35);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('lawn green', 124, 252, 0);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('chartreuse', 127, 255, 0);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('green yellow', 173, 255, 47);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('dark green', 0, 100, 0);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('green', 0, 128, 0);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('forest green', 34, 139, 34);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('lime', 0, 255, 0);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('lime green', 50, 205, 50);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('light green', 144, 238, 144);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('pale green', 152, 251, 152);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('dark sea green', 143, 188, 143);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('medium spring green', 0, 250, 154);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('spring green', 0, 255, 127);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('sea green', 46, 139, 87);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('medium aqua marine', 102, 205, 170);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('medium sea green', 60, 179, 113);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('light sea green', 32, 178, 170);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('dark slate gray', 47, 79, 79);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('teal', 0, 128, 128);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('dark cyan', 0, 139, 139);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('aqua', 0, 255, 255);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('cyan', 0, 255, 255);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('light cyan', 224, 255, 255);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('dark turquoise', 0, 206, 209);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('turquoise', 64, 224, 208);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('medium turquoise', 72, 209, 204);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('pale turquoise', 175, 238, 238);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('aqua marine', 127, 255, 212);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('powder blue', 176, 224, 230);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('cadet blue', 95, 158, 160);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('steel blue', 70, 130, 180);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('corn flower blue', 100, 149, 237);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('deep sky blue', 0, 191, 255);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('dodger blue', 30, 144, 255);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('light blue', 173, 216, 230);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('sky blue', 135, 206, 235);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('light sky blue', 135, 206, 250);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('midnight blue', 25, 25, 112);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('navy', 0, 0, 128);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('dark blue', 0, 0, 139);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('medium blue', 0, 0, 205);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('blue', 0, 0, 255);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('royal blue', 65, 105, 225);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('blue violet', 138, 43, 226);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('indigo', 75, 0, 130);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('dark slate blue', 72, 61, 139);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('slate blue', 106, 90, 205);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('medium slate blue', 123, 104, 238);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('medium purple', 147, 112, 219);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('dark magenta', 139, 0, 139);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('dark violet', 148, 0, 211);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('dark orchid', 153, 50, 204);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('medium orchid', 186, 85, 211);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('purple', 128, 0, 128);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('thistle', 216, 191, 216);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('plum', 221, 160, 221);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('violet', 238, 130, 238);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('magenta / fuchsia', 255, 0, 255);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('orchid', 218, 112, 214);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('medium violet red', 199, 21, 133);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('pale violet red', 219, 112, 147);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('deep pink', 255, 20, 147);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('hot pink', 255, 105, 180);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('light pink', 255, 182, 193);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('pink', 255, 192, 203);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('antique white', 250, 235, 215);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('beige', 245, 245, 220);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('bisque', 255, 228, 196);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('blanched almond', 255, 235, 205);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('wheat', 245, 222, 179);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('corn silk', 255, 248, 220);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('lemon sophia', 255, 250, 205);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('light golden rod yellow', 250, 250, 210);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('light yellow', 255, 255, 224);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('saddle brown', 139, 69, 19);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('sienna', 160, 82, 45);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('chocolate', 210, 105, 30);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('peru', 205, 133, 63);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('sandy brown', 244, 164, 96);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('burly wood', 222, 184, 135);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('tan', 210, 180, 140);
INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('rosy brown', 188, 143, 143);
-- INSERT OR IGNORE INTO Colors (name, r, g, b) VALUES ('moccasin', 255, 





