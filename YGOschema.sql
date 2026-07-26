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

--Main Deck vs Extra Deck
	extra_deck BOOLEAN NOT NULL DEFAULT FALSE,
--

	spell_trap_type VARCHAR(20),
	level_rank INTEGER,
	mon_attribute VARCHAR(20),
	link_arrows VARCHAR(100),
	pendulum_scale INTEGER,
	attack INTEGER,
	defense INTEGER,
	unknown_atk BOOLEAN NOT NULL DEFAULT FALSE,
	unknown_def BOOLEAN NOT NULL DEFAULT FALSE,

--Cosmetic Extras
	alternative_art BOOLEAN NOT NULL DEFAULT FALSE,
	overframe BOOLEAN NOT NULL DEFAULT FALSE,
--
	quantity INT NOT NULL DEFAULT 0
);
