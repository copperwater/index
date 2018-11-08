drop table if exists documents;
drop table if exists index;

-- Document data store.
create table documents (
  id int constraint documents_pk primary key,
  -- 2000 characters in a url is the maximum needed for widespread support
  url varchar(2000),
  pagerank numeric(7,6),
  title varchar(1024),
  sect_headings text[],
  body text[]
);

-- Inverted index relation.
create table index (
  ngram varchar(256) constraint index_pk primary key,
  docid int not null,
  in_title boolean not null,
  in_description boolean not null,
  in_keywords boolean not null,
  freq_headings numeric(7,6) not null,
  freq_text numeric(7,6) not null,

  constraint doc_fk foreign key (docid) references documents(id)
);
