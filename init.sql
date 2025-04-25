-- This script runs when PostgreSQL initializes for the first time
-- The main database user/role is already created from POSTGRES_USER environment variable

-- Create additional roles if needed
-- CREATE ROLE some_other_role WITH LOGIN PASSWORD 'secure_password';

-- Create extensions if needed
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "hstore";

-- Additional configuration
ALTER ROLE ${POSTGRES_USER} SET client_encoding TO 'utf8';
ALTER ROLE ${POSTGRES_USER} SET default_transaction_isolation TO 'read committed';
ALTER ROLE ${POSTGRES_USER} SET timezone TO 'UTC';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE ${POSTGRES_DB} TO ${POSTGRES_USER};