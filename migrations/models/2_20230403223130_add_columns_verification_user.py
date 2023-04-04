from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "client" ADD "email_is_verified" BOOL NOT NULL  DEFAULT False;
        ALTER TABLE "client" ADD "expiration_code_time" TIMESTAMPTZ;
        ALTER TABLE "client" ADD "verification_code" VARCHAR(6);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "client" DROP COLUMN "email_is_verified";
        ALTER TABLE "client" DROP COLUMN "expiration_code_time";
        ALTER TABLE "client" DROP COLUMN "verification_code";"""
