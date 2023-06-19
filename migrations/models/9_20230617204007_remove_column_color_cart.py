from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "selected_product" DROP COLUMN "color";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "selected_product" ADD "color" VARCHAR(255) NOT NULL;"""
