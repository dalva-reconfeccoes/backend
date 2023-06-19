from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "cart" (
            "id" SERIAL NOT NULL PRIMARY KEY,
            "uuid" VARCHAR(32) NOT NULL,
            "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
            "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
            "step" INT   DEFAULT 0,
            "total_value" DOUBLE PRECISION,
            "is_finished" BOOL NOT NULL  DEFAULT False,
            "client_id" INT REFERENCES "client" ("id") ON DELETE CASCADE
        );
        CREATE TABLE IF NOT EXISTS "selected_product" (
            "id" SERIAL NOT NULL PRIMARY KEY,
            "uuid" VARCHAR(32) NOT NULL,
            "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
            "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
            "size" VARCHAR(3) NOT NULL,
            "color" VARCHAR(255) NOT NULL,
            "quantity" INT NOT NULL,
            "cart_id" INT NOT NULL REFERENCES "cart" ("id") ON DELETE CASCADE,
            "product_id" INT NOT NULL REFERENCES "product" ("id") ON DELETE CASCADE
        );
        COMMENT ON COLUMN "selected_product"."size" IS 'SIZE_PP: PP\nSIZE_P: P\nSIZE_M: M\nSIZE_G: G\nSIZE_GG: GG\nSIZE_EXG: EXG';
        """


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "cart";
        DROP TABLE IF EXISTS "selected_product";"""
