from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "product" (
            "id" SERIAL NOT NULL PRIMARY KEY,
            "uuid" VARCHAR(32) NOT NULL,
            "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
            "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
            "header" VARCHAR(255) NOT NULL,
            "color" VARCHAR(255) NOT NULL,
            "knitted" VARCHAR(255) NOT NULL,
            "price" DOUBLE PRECISION NOT NULL,
            "quantity" INT NOT NULL,
            "type" VARCHAR(8) NOT NULL,
            "sub_type" VARCHAR(11) NOT NULL,
            "sex" VARCHAR(9) NOT NULL,
            "status" VARCHAR(12) NOT NULL,
            "is_active" BOOL NOT NULL  DEFAULT True
        );
        COMMENT ON COLUMN "product"."type" IS 'T_SHIRT: Camiseta\nSWEATSHIRT: Moletom';
        COMMENT ON COLUMN "product"."sub_type" IS 'REGULAR: Comum\nPOLO: Polo\nLONG_SLEEVE: Manga Longa\nTANK_TOP: Regata\nRAGLAN: Raglan';
        COMMENT ON COLUMN "product"."sex" IS 'MALE: Masculino\nFEMALE: Faminino\nUNISEX: Unissex';
        COMMENT ON COLUMN "product"."status" IS 'AVAILABLE: Disponivel\nUNAVAILABLE: Indisponivel';;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "product";"""
