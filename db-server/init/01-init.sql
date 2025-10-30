CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (name, email) VALUES
    ('Иван Иванов', 'ivan@example.com'),
    ('Мария Петрова', 'maria@example.com'),
    ('Алексей Сидоров', 'alexey@example.com'),
    ('Елена Козлова', 'elena@example.com'),
    ('Дмитрий Новиков', 'dmitry@example.com');

CREATE INDEX idx_users_email ON users(email);

SELECT 'Database initialized successfully!' as status;
SELECT COUNT(*) as total_users FROM users;