create table Endereco (
    endereco_id UUID primary key,
    CEP VARCHAR(10) not null,
    numero VARCHAR(10),
    endereco VARCHAR(255) not null,
    complemento VARCHAR(255),
    bairro VARCHAR(255) not null,
    cidade VARCHAR(255) not null,
    UF VARCHAR(2) not null,
    tipo VARCHAR(10) not null,
    check(tipo in ('Matriz', 'Filial', 'Candidato'))
);
-- Criação da tabela Usuário
create table Usuario (
    usuario_id UUID primary key,
    email VARCHAR(255) not null,
    senha VARCHAR(255) not null,
    acesso VARCHAR(10) not null,
    check (acesso in ('Matriz', 'Filial'))
);
-- Criação da tabela Empresa
create table Empresa (
    empresa_id UUID primary key,
    nome_empresa VARCHAR(255) not null,
    descricao text,
    telefone VARCHAR(20),
    email VARCHAR(255),
    endereco_id UUID,
    tipo VARCHAR(10) not null,
    check(tipo in ('Matriz', 'Filial')),
    usuario_id UUID not null,
    foreign key (usuario_id) references Usuario(usuario_id),
    foreign key (endereco_id) references Endereco(endereco_id)
);
-- Criação da tabela Candidato
create table Candidato (
    candidato_id UUID primary key,
    nome_candidato VARCHAR(255) not null,
    telefone VARCHAR(20),
    email VARCHAR(255),
    exp_profissional text,
    formacao_academica text,
    habilidades text,
    linguas_faladas text,
    endereco_id UUID,
    usuario_id UUID not null,
    foreign key (endereco_id) references Endereco(endereco_id),
    foreign key (usuario_id) references Usuario(usuario_id)
);

-- Criação da tabela Vaga
create table Vaga (
    vaga_id UUID primary key,
    cargo VARCHAR(255),
    salario DECIMAL(10,
2),
    empresa_id UUID not null,
    regime_contratacao VARCHAR(255),
    nome_empresa VARCHAR(255),
    nivel_exp VARCHAR(255),
    regime_trabalho VARCHAR(255),
    status VARCHAR(20) not null,
    check (status in ('Disponível','Banco de Talentos','Fechada')),
    beneficios text,
    descricao text,
    foreign key (empresa_id) references Empresa(empresa_id)
);
-- Criação da tabela Candidatura
create table Candidatura (
    candidatura_id UUID primary key,
    vaga_id UUID not null,
    candidato_id UUID not null,
    foreign key (vaga_id) references Vaga(vaga_id),
    foreign key (candidato_id) references Candidato(candidato_id)
);
create table Endereco (
    endereco_id UUID primary key,
    CEP VARCHAR(10) not null,
    numero VARCHAR(10),
    endereco VARCHAR(255) not null,
    complemento VARCHAR(255),
    bairro VARCHAR(255) not null,
    cidade VARCHAR(255) not null,
    UF VARCHAR(2) not null,
    tipo VARCHAR(10) not null,
    check(tipo in ('Matriz', 'Filial', 'Candidato'))
);
-- Criação da tabela Usuário
create table Usuario (
    usuario_id UUID primary key,
    email VARCHAR(255) not null,
    senha VARCHAR(255) not null,
    acesso VARCHAR(10) not null,
    check (acesso in ('Empresa', 'Candidato', 'Admin'))
);
-- Criação da tabela Empresa
create table Empresa (
    empresa_id UUID primary key,
    nome_empresa VARCHAR(255) not null,
    descricao text,
    telefone VARCHAR(20),
    email VARCHAR(255),
    endereco_id UUID,
    tipo VARCHAR(10) not null,
    check(tipo in ('Matriz', 'Filial')),
    usuario_id UUID not null,
    foreign key (usuario_id) references Usuario(usuario_id),
    foreign key (endereco_id) references Endereco(endereco_id)
);
-- Criação da tabela Candidato
create table Candidato (
    candidato_id UUID primary key,
    nome_candidato VARCHAR(255) not null,
    telefone VARCHAR(20),
    email VARCHAR(255),
    exp_profissional text,
    formacao_academica text,
    habilidades text,
    linguas_faladas text,
    endereco_id UUID,
    usuario_id UUID not null,
    foreign key (endereco_id) references Endereco(endereco_id),
    foreign key (usuario_id) references Usuario(usuario_id)
);

-- Criação da tabela Vaga
create table Vaga (
    vaga_id UUID primary key,
    cargo VARCHAR(255),
    salario DECIMAL(10,
2),
    empresa_id UUID not null,
    regime_contratacao VARCHAR(255),
    nome_empresa VARCHAR(255),
    nivel_exp VARCHAR(255),
    regime_trabalho VARCHAR(255),
    status VARCHAR(20) not null,
    check (status in ('Disponível','Banco de Talentos','Fechada')),
    beneficios text,
    descricao text,
    foreign key (empresa_id) references Empresa(empresa_id)
);
-- Criação da tabela Candidatura
create table Candidatura (
    candidatura_id UUID primary key,
    vaga_id UUID not null,
    candidato_id UUID not null,
    foreign key (vaga_id) references Vaga(vaga_id),
    foreign key (candidato_id) references Candidato(candidato_id)
);
