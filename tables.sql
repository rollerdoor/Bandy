CREATE TABLE account(
   id INTEGER,
   group_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE
   PRIMARY KEY (contact_id, group_id),
--    FOREIGN KEY (contact_id) 
--       REFERENCES contacts (contact_id) 
--          ON DELETE CASCADE 
--          ON UPDATE NO ACTION,
--    FOREIGN KEY (group_id) 
--       REFERENCES groups (group_id) 
--          ON DELETE CASCADE 
--          ON UPDATE NO ACTION
);