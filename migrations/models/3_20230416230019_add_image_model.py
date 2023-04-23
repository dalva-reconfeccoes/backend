from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "image" (
            "id" SERIAL NOT NULL PRIMARY KEY,
            "uuid" VARCHAR(32) NOT NULL,
            "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
            "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
            "name" VARCHAR(255) NOT NULL,
            "path" VARCHAR(255) NOT NULL,
            "bucket" VARCHAR(255) NOT NULL,
            "is_active" BOOL NOT NULL  DEFAULT True,
            "product_id" INT NOT NULL REFERENCES "product" ("id") ON DELETE CASCADE
        );"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "image";"""
