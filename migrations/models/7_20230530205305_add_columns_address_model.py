from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "address" (
            "id" SERIAL NOT NULL PRIMARY KEY,
            "uuid" VARCHAR(32) NOT NULL,
            "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
            "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
            "district" VARCHAR(128),
            "cep" VARCHAR(128),
            "city" VARCHAR(128),
            "street" VARCHAR(128),
            "uf" VARCHAR(128),
            "complement" VARCHAR(128),
            "neighborhood" VARCHAR(128),
            "number" INT,
            "is_active" BOOL NOT NULL  DEFAULT False,
            "client_id" INT NOT NULL REFERENCES "client" ("id") ON DELETE CASCADE
        );
    """


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "address";"""
