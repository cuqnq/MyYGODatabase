-- Yu-Gi-Oh Collection Tracker
-- Database schema for the `cards` table
-- Run this against a fresh PostgreSQL database to recreate the project's structure.

CREATE TABLE cards (
    id SERIAL PRIMARY KEY,
    card_name VARCHAR(100) NOT NULL,
    set_code VARCHAR(10) NOT NULL,
    rarity VARCHAR(30) NOT NULL,
    card_type VARCHAR(10) NOT NULL,
    monster_type VARCHAR(25),

--Card effect or flavor text pulled from YGOPRODeck by import_cards.py (TEXT has no length limit)
    description TEXT,

--There are many monster summoning mechanics in Yu-Gi-Oh! Each has their own unique ruling that cannot intertwine.
--Pendulum are exceptions to this ruling.
    is_normal BOOLEAN NOT NULL DEFAULT FALSE,
    is_effect BOOLEAN NOT NULL DEFAULT FALSE,
    is_fusion BOOLEAN NOT NULL DEFAULT FALSE,
    is_synchro BOOLEAN NOT NULL DEFAULT FALSE,
    is_xyz BOOLEAN NOT NULL DEFAULT FALSE,
    is_link BOOLEAN NOT NULL DEFAULT FALSE,
    is_ritual BOOLEAN NOT NULL DEFAULT FALSE,
    is_pendulum BOOLEAN NOT NULL DEFAULT FALSE,

--Monster subtypes (the 3rd slot of the type line, ex: [Dragon / Synchro / Tuner / Effect])
    is_tuner BOOLEAN NOT NULL DEFAULT FALSE,
    is_flip BOOLEAN NOT NULL DEFAULT FALSE,
    is_gemini BOOLEAN NOT NULL DEFAULT FALSE,
    is_spirit BOOLEAN NOT NULL DEFAULT FALSE,
    is_toon BOOLEAN NOT NULL DEFAULT FALSE,
    is_union BOOLEAN NOT NULL DEFAULT FALSE,

--Main Deck vs Extra Deck
    extra_deck BOOLEAN NOT NULL DEFAULT FALSE,
--

    spell_trap_type VARCHAR(20),
    level_rank INTEGER,
    monster_attribute VARCHAR(20),

--Link monsters only have Link Rating (1-6) and arrow directions. Empty (NULL) for every other card.
--Also does not have a DEF stat.
    link_rating INTEGER,
    link_arrows VARCHAR(100),
    CONSTRAINT link_has_no_def CHECK (is_link = FALSE OR (defense IS NULL AND unknown_def = FALSE)),

    pendulum_scale INTEGER,
    attack INTEGER,
    defense INTEGER,
    unknown_atk BOOLEAN NOT NULL DEFAULT FALSE,
    unknown_def BOOLEAN NOT NULL DEFAULT FALSE,

--Cosmetic Extras
    alternative_art BOOLEAN NOT NULL DEFAULT FALSE,
    overframe BOOLEAN NOT NULL DEFAULT FALSE,
--
--Quantity can never be negative. Cards that reach 0 are deleted by change_quantity().
    quantity INT NOT NULL DEFAULT 1 CONSTRAINT quantity_not_negative CHECK (quantity >= 0),

--Card art URL pulled from YGOPRODeck by import_cards.py
    image_url VARCHAR(255));