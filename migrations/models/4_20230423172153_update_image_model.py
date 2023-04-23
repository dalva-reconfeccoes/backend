from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "image" RENAME COLUMN "name" TO "filename";
        ALTER TABLE "image" RENAME COLUMN "path" TO "content_type";
        ALTER TABLE "image" ALTER COLUMN "uuid" TYPE VARCHAR(120) USING "uuid"::VARCHAR(120);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "image" RENAME COLUMN "content_type" TO "path";
        ALTER TABLE "image" RENAME COLUMN "filename" TO "name";
        ALTER TABLE "image" ALTER COLUMN "uuid" TYPE VARCHAR(32) USING "uuid"::VARCHAR(32);"""
