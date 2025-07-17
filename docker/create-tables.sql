CREATE TABLE "users" (
  "id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  "name" varchar(60) NOT NULL,
  "email" varchar(60) UNIQUE NOT NULL,
  "is_active" boolean DEFAULT TRUE,
  "created_at" timestamp DEFAULT now()
);

CREATE TABLE "equipments" (
  "id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  "name" varchar(60) UNIQUE NOT NULL,
  "current_status_id" uuid,
  "last_heartbeat" timestamp,
  "created_at" timestamp DEFAULT now()
);

CREATE TABLE "equipment_status_logs" (
  "id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  "status_id" uuid NOT NULL,
  "equipment_id" uuid NOT NULL,
  "details" varchar(300),
  "reported_at" timestamp DEFAULT now(),
  "created_at" timestamp DEFAULT now()
);

CREATE TABLE "equipment_statuses" (
  "id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  "name" varchar(60) UNIQUE NOT NULL,
  "created_at" timestamp DEFAULT now()
);

CREATE TABLE "reservation_statuses" (
  "id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  "name" varchar(60) UNIQUE NOT NULL,
  "created_at" timestamp DEFAULT now()
);

CREATE TABLE "commands" (
  "id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  "equipment_id" uuid NOT NULL,
  "payload" varchar(200),
  "created_at" timestamp DEFAULT now()
);

CREATE TABLE "reservations" (
  "id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  "user_id" uuid NOT NULL,
  "equipment_id" uuid NOT NULL,
  "start_time" timestamp NOT NULL,
  "end_time" timestamp NOT NULL,
  "status_id" uuid NOT NULL,
  "created_at" timestamp DEFAULT now()
);

CREATE TABLE "user_auth" (
  "id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  "username" varchar(60) UNIQUE NOT NULL,
  "password_hash" varchar(100) NOT NULL,
  "user_id" uuid NOT NULL,
  "created_at" timestamp DEFAULT now()
);

-- Definição de Chaves Estrangeiras
ALTER TABLE "equipments" ADD CONSTRAINT fk_equipments_status FOREIGN KEY ("current_status_id") REFERENCES "equipment_statuses" ("id");

ALTER TABLE "equipment_status_logs" ADD CONSTRAINT fk_status_logs_status FOREIGN KEY ("status_id") REFERENCES "equipment_statuses" ("id");

ALTER TABLE "equipment_status_logs" ADD CONSTRAINT fk_status_logs_equipment FOREIGN KEY ("equipment_id") REFERENCES "equipments" ("id");

ALTER TABLE "commands" ADD CONSTRAINT fk_commands_equipment FOREIGN KEY ("equipment_id") REFERENCES "equipments" ("id");

ALTER TABLE "reservations" ADD CONSTRAINT fk_reservations_user FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "reservations" ADD CONSTRAINT fk_reservations_equipment FOREIGN KEY ("equipment_id") REFERENCES "equipments" ("id");

ALTER TABLE "reservations" ADD CONSTRAINT fk_reservations_status FOREIGN KEY ("status_id") REFERENCES "reservation_statuses" ("id");

ALTER TABLE "user_auth" ADD CONSTRAINT fk_user_auth FOREIGN KEY ("user_id") REFERENCES "users" ("id");
