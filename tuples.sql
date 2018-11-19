delete from index;
delete from documents;

insert into documents values (1, 'http://tropicalfish.com', 0.87, 0.51,
  'Freds Tropical Fish Store',
  'The best tropical fish!',
  array['finest fish', 'fishy fish', 'freds fish'],
  array['fish fish fish fish fish', 'fish fish fish', 'fish fish fish fish fish fish fish', 'fish fish'],
  '2018-04-06',
  '2018-01-15'
);
insert into documents values (2, 'http://example.com', 1.12, 0.77,
  'Example Domain',
  null,
  array['Example Domain'],
  array['this domain is established to be used for illustrative examples in documents you may use this domain in examples without prior coordination or asking for permission', 'more information'],
  '2018-12-25',
  '2011-07-21'
);

-- 1-grams...
insert into index values ('fish', 1, true, true, true, 0.6666, 1.0000);
insert into index values ('tropical', 1, true, true, true, 0, 0);
insert into index values ('freds', 1, true, false, false, 0.1666, 0);
insert into index values ('store', 1, true, true, false, 0, 0);
insert into index values ('best', 1, false, true, false, 0, 0);
insert into index values ('finest', 1, false, false, false, 1.6666, 0);
insert into index values ('fishy', 1, false, false, false, 1.6666, 0);
-- 2-grams, document headings
insert into index values ('freds tropical', 1, true, false, false, 0, 0);
insert into index values ('tropical fish', 1, true, true, true, 0, 0);
insert into index values ('fish store', 1, true, false, false, 0, 0);
insert into index values ('best tropical', 1, false, true, false, 0, 0);
-- 2-grams, section headings
insert into index values ('finest fish', 1, false, false, false, 0.3333, 0);
insert into index values ('fishy fish', 1, false, false, false, 0.3333, 0);
insert into index values ('freds fish', 1, false, false, false, 0.3333, 0);
-- 2-grams, body text
insert into index values ('fish fish', 1, false, false, false, 0, 1.0000);
-- 3-grams, document headings
insert into index values ('freds tropical fish', 1, true, false, false, 0, 0);
insert into index values ('tropical fish store', 1, true, false, false, 0, 0);
insert into index values ('best tropical fish', 1, false, true, false, 0, 0);
-- 3-grams, body text (none in section headings for this document)
insert into index values ('fish fish fish', 1, false, false, false, 0, 1.0000);
-- 4- and 5-grams, body text
insert into index values ('fish fish fish fish', 1, false, false, false, 0, 1.0000);
insert into index values ('fish fish fish fish fish', 1, false, false, false, 0, 1.0000);
