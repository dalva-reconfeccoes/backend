from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "product" DROP COLUMN "quantity";
        ALTER TABLE "product" ALTER COLUMN "sub_type" TYPE VARCHAR(11) USING "sub_type"::VARCHAR(11);
        CREATE TABLE IF NOT EXISTS "quantity" (
            "id" SERIAL NOT NULL PRIMARY KEY,
                "uuid" VARCHAR(32) NOT NULL,
                "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
                "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
                "size" VARCHAR(3) NOT NULL,
                "available" INT   DEFAULT 0,
                "purchased" INT   DEFAULT 0,
                "product_id" INT NOT NULL REFERENCES "product" ("id") ON DELETE CASCADE
            );
        COMMENT ON COLUMN "quantity"."size" IS 'SIZE_PP: PP\nSIZE_P: P\nSIZE_M: M\nSIZE_G: G\nSIZE_GG: GG\nSIZE_EXG: EXG';
        """


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "product" ADD "quantity" INT NOT NULL;
        ALTER TABLE "product" ALTER COLUMN "sub_type" TYPE VARCHAR(11) USING "sub_type"::VARCHAR(11);
        DROP TABLE IF EXISTS "quantity";"""
