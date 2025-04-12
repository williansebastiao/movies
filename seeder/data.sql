truncate users, categories, movies, ratings, movie_categories cascade ;

insert into users (first_name, last_name, email, uuid, created_at, updated_at) values ('John', 'Doe', 'john.doe@any.com', gen_random_uuid(), now(), now());
insert into users (first_name, last_name, email, uuid, created_at, updated_at) values ('Jane', 'Doe', 'jane.doe@any.com', gen_random_uuid(), now(), now());

insert into categories (category, slug, uuid, created_at, updated_at) values ('ACTION', 'action', gen_random_uuid(), now(), now());
insert into categories (category, slug, uuid, created_at, updated_at) values ('TERROR', 'terror', gen_random_uuid(), now(), now());
insert into categories (category, slug, uuid, created_at, updated_at) values ('MUSICAL', 'musical', gen_random_uuid(), now(), now());
insert into categories (category, slug, uuid, created_at, updated_at) values ('COMEDY', 'comedy', gen_random_uuid(), now(), now());

insert into movies (name, synopsis, slug, uuid, created_at, updated_at)
values (
    'Baby Driver',
    'O jovem e talentoso motorista Baby confia na batida pessoal de sua trilha sonora preferida para ser o melhor no mundo do crime. Quando ele conhece a garota de seus sonhos, Baby vê uma',
    'baby-driver',
    gen_random_uuid(),
    now(),
    now()
);

insert into movies (name, synopsis, slug, uuid, created_at, updated_at)
values (
    'Mad Max: Estrada da Fúria',
    'Em um mundo pós-apocalíptico, Max se une a Furiosa para fugir de um tirano e seu exército em uma perseguição alucinante pelo deserto.',
    'mad-max-fury-road',
    gen_random_uuid(),
    now(),
    now()
);


insert into movies (name, synopsis, slug, uuid, created_at, updated_at)
values (
    'John Wick',
    'Após a morte de seu cachorro, presente de sua falecida esposa, o ex-assassino John Wick retorna ao submundo do crime em busca de vingança.',
    'john-wick',
    gen_random_uuid(),
    now(),
    now()
);


insert into movies (name, synopsis, slug, uuid, created_at, updated_at)
values (
    'Velozes e Furiosos 7',
    'A equipe de corredores enfrenta um assassino vingativo enquanto lida com desafios pessoais e missões perigosas.',
    'fast-and-furious-7',
    gen_random_uuid(),
    now(),
    now()
);

INSERT INTO movie_categories (movie_uuid, category_uuid, uuid, created_at, updated_at)
SELECT
    m.uuid,
    c.uuid,
    gen_random_uuid(),
    now(),
    now()
FROM movies m
         JOIN categories c ON c.slug = 'action'
WHERE m.slug = 'baby-driver';

INSERT INTO movie_categories (movie_uuid, category_uuid, uuid, created_at, updated_at)
SELECT
    m.uuid,
    c.uuid,
    gen_random_uuid(),
    now(),
    now()
FROM movies m
         JOIN categories c ON c.slug = 'action'
WHERE m.slug = 'mad-max-fury-road';

INSERT INTO movie_categories (movie_uuid, category_uuid, uuid, created_at, updated_at)
SELECT
    m.uuid,
    c.uuid,
    gen_random_uuid(),
    now(),
    now()
FROM movies m
         JOIN categories c ON c.slug = 'action'
WHERE m.slug = 'john-wick';

INSERT INTO movie_categories (movie_uuid, category_uuid, uuid, created_at, updated_at)
SELECT
    m.uuid,
    c.uuid,
    gen_random_uuid(),
    now(),
    now()
FROM movies m
         JOIN categories c ON c.slug = 'action'
WHERE m.slug = 'fast-and-furious-7';


-----

insert into movies (name, synopsis, slug, uuid, created_at, updated_at)
values (
    'A Entidade',
    'Um escritor encontra filmes caseiros que retratam assassinatos horríveis em sua nova casa, colocando sua família em perigo.',
    'a-entidade',
    gen_random_uuid(),
    now(),
    now()
);

insert into movies (name, synopsis, slug, uuid, created_at, updated_at)
values (
    'Hereditário',
    'Após a morte da matriarca da família, eventos sobrenaturais começam a assombrar seus descendentes, revelando segredos sombrios.',
    'hereditario',
    gen_random_uuid(),
    now(),
    now()
);


insert into movies (name, synopsis, slug, uuid, created_at, updated_at)
values (
    'O Chamado',
    'Uma fita de vídeo amaldiçoada causa a morte de quem a assiste em sete dias, levando uma jornalista a investigar sua origem.',
    'o-chamado',
    gen_random_uuid(),
    now(),
    now()
);


insert into movies (name, synopsis, slug, uuid, created_at, updated_at)
values (
    'Atividade Paranormal',
    'Um casal instala câmeras em casa para capturar atividades sobrenaturais que os têm perturbado durante a noite',
    'atividade-paranormal',
    gen_random_uuid(),
    now(),
    now()
);

INSERT INTO movie_categories (movie_uuid, category_uuid, uuid, created_at, updated_at)
SELECT
    m.uuid,
    c.uuid,
    gen_random_uuid(),
    now(),
    now()
FROM movies m
         JOIN categories c ON c.slug = 'terror'
WHERE m.slug = 'a-entidade';

INSERT INTO movie_categories (movie_uuid, category_uuid, uuid, created_at, updated_at)
SELECT
    m.uuid,
    c.uuid,
    gen_random_uuid(),
    now(),
    now()
FROM movies m
         JOIN categories c ON c.slug = 'terror'
WHERE m.slug = 'hereditario';

INSERT INTO movie_categories (movie_uuid, category_uuid, uuid, created_at, updated_at)
SELECT
    m.uuid,
    c.uuid,
    gen_random_uuid(),
    now(),
    now()
FROM movies m
         JOIN categories c ON c.slug = 'terror'
WHERE m.slug = 'o-chamado';

INSERT INTO movie_categories (movie_uuid, category_uuid, uuid, created_at, updated_at)
SELECT
    m.uuid,
    c.uuid,
    gen_random_uuid(),
    now(),
    now()
FROM movies m
         JOIN categories c ON c.slug = 'terror'
WHERE m.slug = 'atividade-paranormal';

----

insert into movies (name, synopsis, slug, uuid, created_at, updated_at)
values (
    'La La Land: Cantando Estações',
    'Um pianista de jazz e uma aspirante a atriz se apaixonam enquanto perseguem seus sonhos em Los Angeles.',
    'la-la-land-cantando-estacoes',
    gen_random_uuid(),
    now(),
    now()
);

insert into movies (name, synopsis, slug, uuid, created_at, updated_at)
values (
    'Os Miseráveis',
    'Na França do século XIX, um ex-prisioneiro tenta recomeçar a vida enquanto é perseguido por um inspetor implacável.',
    'os-miseraveis',
    gen_random_uuid(),
    now(),
    now()
);


insert into movies (name, synopsis, slug, uuid, created_at, updated_at)
values (
    'O Rei do Show',
    'Inspirado na história real de P.T. Barnum, o filme conta como ele criou um espetáculo que virou sensação mundial.',
    'o-rei-do-show',
    gen_random_uuid(),
    now(),
    now()
);


insert into movies (name, synopsis, slug, uuid, created_at, updated_at)
values (
    'Mamma Mia!',
    'Uma jovem prestes a se casar convida três ex-namorados de sua mãe para descobrir qual deles é seu pai.',
    'mamma-mia',
    gen_random_uuid(),
    now(),
    now()
);

INSERT INTO movie_categories (movie_uuid, category_uuid, uuid, created_at, updated_at)
SELECT
    m.uuid,
    c.uuid,
    gen_random_uuid(),
    now(),
    now()
FROM movies m
         JOIN categories c ON c.slug = 'musical'
WHERE m.slug = 'la-la-land-cantando-estacoes';

INSERT INTO movie_categories (movie_uuid, category_uuid, uuid, created_at, updated_at)
SELECT
    m.uuid,
    c.uuid,
    gen_random_uuid(),
    now(),
    now()
FROM movies m
         JOIN categories c ON c.slug = 'musical'
WHERE m.slug = 'os-miseraveis';

INSERT INTO movie_categories (movie_uuid, category_uuid, uuid, created_at, updated_at)
SELECT
    m.uuid,
    c.uuid,
    gen_random_uuid(),
    now(),
    now()
FROM movies m
         JOIN categories c ON c.slug = 'musical'
WHERE m.slug = 'o-rei-do-show';

INSERT INTO movie_categories (movie_uuid, category_uuid, uuid, created_at, updated_at)
SELECT
    m.uuid,
    c.uuid,
    gen_random_uuid(),
    now(),
    now()
FROM movies m
         JOIN categories c ON c.slug = 'musical'
WHERE m.slug = 'mamma-mia';
